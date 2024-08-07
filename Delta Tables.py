# Databricks notebook source
# MAGIC %md
# MAGIC ## Concept of delta tables 

# COMMAND ----------

# MAGIC %md
# MAGIC image.png 

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



# COMMAND ----------

# MAGIC %environment
# MAGIC "client": "1"
# MAGIC "base_environment": ""
