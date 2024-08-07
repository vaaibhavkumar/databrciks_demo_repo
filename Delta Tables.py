# Databricks notebook source
# MAGIC %md
# MAGIC ## Concept of delta tables 

# COMMAND ----------

# MAGIC %md
# MAGIC image.png 
# MAGIC
# MAGIC ### What are Delta Live Tables datasets?
# MAGIC - Delta Live Tables datasets are the streaming tables, materialized views, and views maintained as the results of declarative queries.
# MAGIC - https://docs.databricks.com/en/delta-live-tables/index.html
# MAGIC
# MAGIC ### Streaming table
# MAGIC > - A streaming table is a Delta table with extra support for streaming or incremental data processing. 
# MAGIC > - Streaming tables allow you to process a growing dataset, handling each row only once. Because most datasets grow continuously over time, streaming tables are good for most ingestion workloads. 
# MAGIC > - Streaming tables are optimal for pipelines that require data freshness and low latency. 
# MAGIC
# MAGIC ###Materialized view
# MAGIC - A materialized view is a view where the results have been precomputed. 
# MAGIC - Materialized views are refreshed according to the update schedule of the pipeline in which they’re contained. Materialized views are powerful because they can handle any changes in the input. 
# MAGIC
# MAGIC
# MAGIC ###Views
# MAGIC - All views in Databricks compute results from source datasets as they are queried, leveraging caching optimizations when available. 
# MAGIC - Delta Live Tables does not publish views to the catalog, so views can be referenced only within the pipeline in which they are defined. 
# MAGIC - Views are useful as intermediate queries that should not be exposed to end users or systems. 
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC image.png

# COMMAND ----------

# MAGIC %md
# MAGIC ### Advantages of delta Lake
# MAGIC 1. ACID transactions to object storage
# MAGIC 2. Audit trail of changes is pesent
# MAGIC 3. Industry standard  dat aformats are used: Parquet and JSON
# MAGIC 4. Handles Scalable Metadata

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC ### Creating a table 

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS employees;  
# MAGIC CREATE TABLE employees (id int, name string, salary double) ;

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC INSERT INTO EMPLOYEES VALUES 
# MAGIC   (1,"Adam", 3500)
# MAGIC   , (2,"Bob", 4000.5)
# MAGIC   , (3,"Cadey", 4500)
# MAGIC   , (4,"Donald", 3600)
# MAGIC   , (5,"Eric", 9500)
# MAGIC   , (6,"Fred", 2500)
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC #### Read the data

# COMMAND ----------

# MAGIC %sql
# MAGIC Select * from EMPLOYEES

# COMMAND ----------

# MAGIC %md
# MAGIC - Our cluster has 4 cores
# MAGIC - so 4 parallel paths would have got triggerred to Insert these 6 records

# COMMAND ----------

_sqldf.head(2)

# COMMAND ----------

# MAGIC %md
# MAGIC ### DESCRIBE DETAIL command

# COMMAND ----------

sql_query = "DESCRIBE DETAIL employees"
df_details = spark.sql(sql_query);


# COMMAND ----------

df_details[['location']].show()

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE DETAIL employees

# COMMAND ----------

# MAGIC %fs ls 'abfss://unity-catalog-storage@dbstorageyryifdjvviqpm.dfs.core.windows.net/1358913073911209/__unitystorage/catalogs/5545b94c-46ee-41c3-ae03-c264546b7714/tables/639de2ed-ea80-40d9-a120-beb4b2a9460f'

# COMMAND ----------

# MAGIC %md
# MAGIC ### Sample update operation and increasing salay by 100

# COMMAND ----------

# MAGIC %sql
# MAGIC update employees
# MAGIC set salary = salary+ 100
# MAGIC where name like 'a%' -- 0 records impacted 

# COMMAND ----------

# MAGIC %sql
# MAGIC update employees
# MAGIC set salary = salary+ 100
# MAGIC where name ilike 'a%' -- 1 records impacted -- so like is a case senstitive operation 

# COMMAND ----------

# MAGIC %sql
# MAGIC Select * from EMPLOYEES 
# MAGIC order by 1;

# COMMAND ----------

# MAGIC %md
# MAGIC image.png 

# COMMAND ----------



# COMMAND ----------

# MAGIC %sql
# MAGIC Select * from EMPLOYEES 
# MAGIC /*
# MAGIC the stages of this execution were: 
# MAGIC == Physical Plan ==
# MAGIC CollectLimit (5)
# MAGIC +- * Project (4)
# MAGIC    +- * Filter (3)
# MAGIC       +- * ColumnarToRow (2)
# MAGIC          +- Scan parquet demoworkspace.default.employees (1)
# MAGIC
# MAGIC (1) Scan parquet demoworkspace.default.employees
# MAGIC Output [4]: [id#5278, name#5279, salary#5280, _databricks_internal_edge_computed_column_skip_row#5309]
# MAGIC Batched: true
# MAGIC Location: PreparedDeltaFileIndex [abfss://unity-catalog-storage@dbstorageyryifdjvviqpm.dfs.core.windows.net/1358913073911209/__unitystorage/catalogs/5545b94c-46ee-41c3-ae03-c264546b7714/tables/639de2ed-ea80-40d9-a120-beb4b2a9460f]
# MAGIC ReadSchema: struct<id:int,name:string,salary:double,_databricks_internal_edge_computed_column_skip_row:boolean>
# MAGIC
# MAGIC (2) ColumnarToRow [codegen id : 1]
# MAGIC Input [4]: [id#5278, name#5279, salary#5280, _databricks_internal_edge_computed_column_skip_row#5309]
# MAGIC
# MAGIC (3) Filter [codegen id : 1]
# MAGIC Input [4]: [id#5278, name#5279, salary#5280, _databricks_internal_edge_computed_column_skip_row#5309]
# MAGIC Condition : if (isnotnull(_databricks_internal_edge_computed_column_skip_row#5309)) (_databricks_internal_edge_computed_column_skip_row#5309 = false) else isnotnull(raise_error(DELTA_SKIP_ROW_COLUMN_NOT_FILLED, map(keys: [], values: []), NullType))
# MAGIC
# MAGIC (4) Project [codegen id : 1]
# MAGIC Output [3]: [id#5278, name#5279, salary#5280]
# MAGIC Input [4]: [id#5278, name#5279, salary#5280, _databricks_internal_edge_computed_column_skip_row#5309]
# MAGIC
# MAGIC (5) CollectLimit
# MAGIC Input [3]: [id#5278, name#5279, salary#5280]
# MAGIC Arguments: 10001
# MAGIC
# MAGIC */

# COMMAND ----------

# MAGIC %sql
# MAGIC Select * from EMPLOYEES where name ilike 'a%'
# MAGIC /*
# MAGIC Databricks pools are a set of idle, ready-to-use instances. When cluster nodes are created using the idle instances, cluster start and auto-scaling times are reduced. If the pool has no idle instances, the pool expands by allocating a new instance from the instance provider in order to accommodate the cluster’s request.
# MAGIC When a cluster releases an instance, it returns to the pool and is free for another cluster to use. Only clusters attached to a pool can use that pool’s idle instances.
# MAGIC Databricks does not charge DBUs while instances are idle in the pool. Instance provider billing does apply. See pricing.
# MAGIC
# MAGIC */

# COMMAND ----------

# MAGIC %environment
# MAGIC "client": "1"
# MAGIC "base_environment": ""
