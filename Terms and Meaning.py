# Databricks notebook source


# COMMAND ----------

# MAGIC %md
# MAGIC # Some terms
# MAGIC - Source - https://docs.databricks.com/en/index.html#
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### What is a data lakehouse?
# MAGIC - A data lakehouse is a data management system that combines the benefits of data lakes and data warehouses. 
# MAGIC - https://docs.databricks.com/en/_images/lakehouse-diagram.png
# MAGIC
# MAGIC
# MAGIC
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### What are ACID guarantees on Databricks?
# MAGIC - https://docs.databricks.com/en/lakehouse/acid.html#what-are-acid-guarantees-on-databricks
# MAGIC
# MAGIC Databricks uses Delta Lake by default for all reads and writes and builds upon the ACID guarantees provided by the open source Delta Lake protocol. ACID stands for atomicity, consistency, isolation, and durability.
# MAGIC
# MAGIC - Atomicity means that all transactions either succeed or fail completely.
# MAGIC
# MAGIC - Consistency guarantees relate to how a given state of the data is observed by simultaneous operations.
# MAGIC
# MAGIC - Isolation refers to how simultaneous operations potentially conflict with one another.
# MAGIC
# MAGIC - Durability means that committed changes are permanent.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Delta tables vs. Delta Live Tables
# MAGIC - Delta table is a way to store data in tables, whereas Delta Live Tables allows you to describe how data flows between these tables declaratively. 
# MAGIC - Delta Live Tables is a declarative framework that manages many delta tables, by creating them and keeping them up to date. 
# MAGIC - In short, Delta tables is a data table architecture while Delta Live Tables is a data pipeline framework.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Delta Lake transaction log (AKA DeltaLogs)
# MAGIC A single source of truth tracking all changes that users make to the table and the mechanism through which Delta Lake guarantees atomicity. 

# COMMAND ----------

# MAGIC %md
# MAGIC ### Accounts and workspaces
# MAGIC In Databricks, a ***workspace*** is a Databricks deployment in the cloud that functions as an environment for your team to access Databricks assets. Your organization can choose to have either multiple workspaces or just one, depending on its needs.
# MAGIC
# MAGIC A ***Databricks account*** represents a single entity that can include multiple workspaces. Accounts enabled for Unity Catalog can be used to manage users and their access to data centrally across all of the workspaces in the account. Billing and support are also handled at the account level.
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Billing: Databricks units (DBUs)
# MAGIC Databricks bills based on Databricks units (DBUs), which are units of processing capability per hour based on VM instance type.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Authentication and authorization
# MAGIC - https://docs.databricks.com/en/getting-started/concepts.html#authentication-and-authorization
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Service principal
# MAGIC A service identity for use with jobs, automated tools, and systems such as scripts, apps, and CI/CD platforms. Service principals are represented by an application ID. See Manage service principals.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### Group
# MAGIC A collection of identities. Groups simplify identity management, making it easier to assign access to workspaces, data, and other securable objects. All Databricks identities can be assigned as members of groups. See Manage groups.
# MAGIC
# MAGIC ### Access control list (ACL)
# MAGIC A list of permissions attached to the workspace, cluster, job, table, or experiment. An ACL specifies which users or system processes are granted access to the objects, as well as what operations are allowed on the assets. Each entry in a typical ACL specifies a subject and an operation. See Access control lists.
# MAGIC
# MAGIC ### Personal access token (PAT)
# MAGIC A personal access token is a string used to authenticate REST API calls, Technology partners connections, and other tools. See Databricks personal access token authentication.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Data management
# MAGIC https://docs.databricks.com/en/getting-started/concepts.html#data-management

# COMMAND ----------

# MAGIC %md
# MAGIC ### Delta table
# MAGIC - https://docs.databricks.com/en/getting-started/concepts.html#delta-table
# MAGIC - By default, all tables created in Databricks are Delta tables. Delta tables are based on the Delta Lake open source project, a framework for high-performance ACID table storage over cloud object stores. A Delta table stores data as a directory of files on cloud object storage and registers table metadata to the metastore within a catalog and schema.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Metastore
# MAGIC The component that stores all of the structure information of the various tables and partitions in the data warehouse including column and column type information, the serializers and deserializers necessary to read and write data, and the corresponding files where the data is stored. See Metastores https://docs.databricks.com/en/data-governance/unity-catalog/index.html#metastore
# MAGIC
# MAGIC Every Databricks deployment has a central Hive metastore accessible by all clusters to persist table metadata. You also have the option to use an existing external Hive metastore.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Unity Catalog
# MAGIC - Unity Catalog is a unified governance solution for data and AI assets on Databricks that provides centralized access control, auditing, lineage, and data discovery capabilities across Databricks workspaces. 
# MAGIC
# MAGIC - https://docs.databricks.com/en/_images/with-unity-catalog.png
# MAGIC - https://docs.databricks.com/en/_images/object-model.png
# MAGIC
# MAGIC - https://docs.databricks.com/en/data-governance/unity-catalog/index.html
# MAGIC
# MAGIC - **_Define once, secure everywhere_**: Unity Catalog offers a single place to administer data access policies that apply across all workspaces.
# MAGIC
# MAGIC - _**Standards-compliant security model**_: Unity Catalog’s security model is based on standard ANSI SQL and allows administrators to grant permissions in their existing data lake using familiar syntax, at the level of catalogs, schemas (also called databases), tables, and views.
# MAGIC
# MAGIC - **_Built-in auditing and lineage_**: Unity Catalog automatically captures user-level audit logs that record access to your data. Unity Catalog also captures lineage data that tracks how data assets are created and used across all languages.
# MAGIC
# MAGIC - _**Data discovery**_: Unity Catalog lets you tag and document data assets, and provides a search interface to help data consumers find data.
# MAGIC
# MAGIC - _**System tables (Public Preview)**_: Unity Catalog lets you easily access and query your account’s operational data, including audit logs, billable usage, and lineage.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ## Computation management
# MAGIC This section describes concepts that you need to know to run computations in Databricks.
# MAGIC
# MAGIC https://docs.databricks.com/en/getting-started/concepts.html#computation-management
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### **Cluster**
# MAGIC - A set of computation resources and configurations on which you run notebooks and jobs. There are two types of clusters: all-purpose and job. See Compute.
# MAGIC
# MAGIC - You create an all-purpose cluster using the UI, CLI, or REST API. 
# MAGIC - You can manually terminate and restart an all-purpose cluster. 
# MAGIC - Multiple users can share such clusters to do collaborative interactive analysis.
# MAGIC
# MAGIC - The Databricks job scheduler creates a job cluster when you run a job on a new job cluster and terminates the cluster when the job is complete. You cannot restart an job cluster.
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### **Pool**
# MAGIC - A set of **_idle_**, **_ready-to-use instances_** that reduce cluster start and auto-scaling times. When attached to a pool, a cluster allocates its driver and worker nodes from the pool. See Pool configuration reference.
# MAGIC
# MAGIC - If the pool does not have sufficient idle resources to accommodate the cluster’s request, the pool expands by allocating new instances from the instance provider. 
# MAGIC - When an attached cluster is terminated, the instances it used are returned to the pool and can be reused by a different cluster.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Databricks runtime
# MAGIC The set of core components that run on the clusters managed by Databricks. See Compute. Databricks has the following runtimes:
# MAGIC
# MAGIC - Databricks Runtime includes Apache Spark but also adds a number of components and updates that substantially improve the usability, performance, and security of big data analytics. 
# MAGIC
# MAGIC - Databricks Runtime for Machine Learning is built on Databricks Runtime and provides prebuilt machine learning infrastructure that is integrated with all of the capabilities of the Databricks workspace. It contains multiple popular libraries, including TensorFlow, Keras, PyTorch, and XGBoost.
# MAGIC > - https://docs.databricks.com/en/_images/ml-diagram-model-development-deployment.png
# MAGIC > - 

# COMMAND ----------

# MAGIC %md
# MAGIC ### Workload
# MAGIC Workload is the amount of processing capability needed to perform a task or group of tasks. Databricks identifies **two types of workloads**: 
# MAGIC - data engineering (job) https://docs.databricks.com/en/workspace-index.html#databricks-data-engineering 
# MAGIC and 
# MAGIC - data analytics (all-purpose).
# MAGIC
# MAGIC Data engineering An (automated) workload runs on a job cluster which the Databricks job scheduler creates for each workload.
# MAGIC
# MAGIC Data analytics An (interactive) workload runs on an all-purpose cluster. Interactive workloads typically run commands within a Databricks notebook. However, running a job on an existing all-purpose cluster is also treated as an interactive workload.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Execution context
# MAGIC The state for a read–eval–print loop (REPL) environment for each supported programming language. The languages supported are Python, R, Scala, and SQL.

# COMMAND ----------

# MAGIC %md
# MAGIC

# COMMAND ----------

# MAGIC %environment
# MAGIC "client": "1"
# MAGIC "base_environment": ""
