# ☁️ Azure Network Intrusion Detection System

## ☁️ Cloud-Native Real-Time Network Intrusion Detection using Microsoft Azure

![Azure](https://img.shields.io/badge/Microsoft-Azure-0078D4?logo=microsoftazure&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white)
![PySpark](https://img.shields.io/badge/PySpark-3.x-E25A1C?logo=apachespark&logoColor=white)
![Databricks](https://img.shields.io/badge/Azure-Databricks-FF3621?logo=databricks&logoColor=white)
![Azure ML](https://img.shields.io/badge/Azure-Machine%20Learning-0078D4?logo=microsoftazure&logoColor=white)
![Azure SQL](https://img.shields.io/badge/Azure-SQL-CC2927?logo=microsoftsqlserver&logoColor=white)
![Event Hubs](https://img.shields.io/badge/Azure-Event%20Hubs-0078D4)
![Architecture](https://img.shields.io/badge/Architecture-End--to--End%20Cloud%20Pipeline-blueviolet)
![Status](https://img.shields.io/badge/Phase-5%20Completed-success)
![License](https://img.shields.io/badge/License-MIT-green)

---

# 📖 Project Overview

This project is the cloud-native implementation of my MSc dissertation:

> **Real-Time Network Intrusion Detection System using Big Data Technologies and Machine Learning**

The objective is to transform a traditional Network Intrusion Detection System (NIDS) into a scalable cloud-native cybersecurity solution using Microsoft Azure.

Instead of building a sample Azure application, this repository documents the migration of a real-world machine learning and big data project to Azure services phase by phase.

---

# 🎯 Project Objectives

- Build a cloud-native Network Intrusion Detection System (NIDS)
- Learn Microsoft Azure through hands-on implementation
- Replace local infrastructure with Azure cloud services
- Demonstrate cloud engineering and data engineering practices
- Build a production-ready cybersecurity portfolio project

---

# 🚀 Current Features

## ✅ Phase 1 – Azure Blob Storage

- Azure Resource Group
- Azure Storage Account
- Azure Blob Container
- Uploaded preprocessed CICIDS2018 dataset
- Secure environment configuration (.env)
- Azure Blob Storage SDK integration
- Load dataset directly from Azure Blob Storage

---

## ✅ Phase 2 – Azure SQL Database

- Azure SQL Server
- Azure SQL Database
- Firewall configuration
- Secure SQL authentication
- Python connectivity using ODBC Driver 18
- Automatic predictions table creation
- Insert intrusion detection predictions
- Retrieve stored predictions
- Verify records using Azure Query Editor

---

## ✅ Phase 3 – Azure Event Hubs

- Azure Event Hub Namespace
- Azure Event Hub
- Event Producer
- Event Consumer
- Real-time Network Traffic Streaming
- Machine Learning Prediction Pipeline
- Azure SQL Prediction Logging
- Persistent SQL Database Connection
- Improved SQL Schema
- Modular Production-Style Architecture

  ## ✅ Phase 4 – Azure Databricks

- Azure Databricks Workspace
- Unity Catalog
- Unity Catalog Schema
- Unity Catalog Volume
- PySpark Data Processing
- Data Validation
- Duplicate Removal
- Missing Value Handling
- Parquet Data Storage
- Distributed ETL Pipeline

## ✅ Phase 5 – Azure Machine Learning

- Azure Machine Learning Workspace
- Azure ML Studio
- Compute Instance
- Random Forest Classifier
- Model Training
- Model Evaluation
- Classification Report
- Confusion Matrix
- Model Serialization
- Model Registration
- Model Versioning
- Machine Learning Pipeline  

# 🏗 Current System Architecture

                          Microsoft Azure

+-------------------------------------------+
|         Azure Blob Storage                |
|      balanced_dataset.csv (Raw Data)      |
+-------------------+-----------------------+
                    |
                    ▼
+-------------------------------------------+
|         Azure Databricks                  |
|      Unity Catalog + PySpark ETL          |
|-------------------------------------------|
| • Read CSV from Unity Catalog Volume      |
| • Validate Schema                         |
| • Remove Duplicates                       |
| • Handle Missing Values                   |
| • Save Processed Dataset as Parquet       |
+-------------------+-----------------------+
                    |
                    ▼
+-------------------------------------------+
|     Processed Dataset (Parquet)           |
|      Unity Catalog Volume                 |
+-------------------+-----------------------+
                    |
                    ▼
+-------------------------------------------+
|          Azure Event Hubs                 |
|     Real-Time Network Event Streaming     |
+-------------------+-----------------------+
                    |
                    ▼
+-------------------------------------------+
|      Event Hub Consumer (Python)          |
|-------------------------------------------|
| • Reads Streaming Network Events          |
| • Performs ML Inference                   |
+-------------------+-----------------------+
                    |
                    ▼
+-------------------------------------------+
|      Azure Machine Learning               |
|-------------------------------------------|
| • Random Forest Classifier                |
| • Model Training                          |
| • Model Evaluation (94.5% Accuracy)       |
| • Model Registry (Version 2)              |
+-------------------+-----------------------+
                    |
                    ▼
+-------------------------------------------+
|        Azure SQL Database                 |
|-------------------------------------------|
| • Stores Prediction Logs                  |
| • Network Intrusion Predictions           |
+-------------------------------------------+

# 💻 Technologies Used

## Cloud

-Microsoft Azure
-Azure Blob Storage
-Azure SQL Database
-Azure Event Hubs
-Azure Databricks
-Unity Catalog

## Programming

- Python 3.13

## Python Libraries

- pandas
- pyodbc
- azure-storage-blob
- python-dotenv
- azure-eventhub
- scikit-learn
- joblib
- pyspark

## Database

- Azure SQL
- SQL Server

## Version Control

- Git
- GitHub

---

# 📂 Project Structure

```text
Big_Data_Pipeline/

│
├── azure_services/
│   ├── blob_storage.py
│   ├── eventhub_producer.py
│   ├── eventhub_consumer.py
│   ├── ml_predictor.py
│   ├── sql_database.py
│   ├── sql_logger.py
│   ├── view_prediction.py
│   └── __init__.py
│
├── databricks/
│   └── Phase4_Databricks_Preprocessing.ipynb
│
├── azure_ml/
│   └── Phase5_Model_Training.ipynb
│
├── models/
│   ├── best_ids_model.pkl
│   ├── feature_columns.pkl
│   └── scaler.pkl
│
├── tests/
│   ├── test_blob.py
│   ├── test_eventhub.py
│   ├── test_predictor.py
│   ├── test_stream_dataset.py
│   └── test_sql.py
│
├── screenshots/
│   ├── phase_1/
│   ├── phase_2/
│   ├── phase_3/
│   ├── phase_4/
│   └── phase_5/
│
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore

---

# 📊 Dataset Information

| Attribute | Value |
|-----------|-------|
| Dataset | CICIDS2018 |
| Records | 300,000 |
| Features | 80 |
| Storage | Azure Blob Storage |

---

# ▶️ Installation

## Clone Repository

```bash
git clone https://github.com/ANTOSOJAN/Azure-Network-Intrusion-System.git
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file:

```env
# Azure Blob Storage

AZURE_STORAGE_CONNECTION_STRING=YOUR_CONNECTION_STRING
CONTAINER_NAME=datasets
BLOB_NAME=balanced_dataset.csv

# Azure SQL Database

SQL_SERVER=YOUR_SERVER.database.windows.net
SQL_DATABASE=nids-db
SQL_USERNAME=YOUR_USERNAME
SQL_PASSWORD=YOUR_PASSWORD

# Azure Event Hub

EVENT_HUB_CONNECTION_STRING=
EVENT_HUB_NAME=
```

---

# ▶️ Running the Project

## Test Azure Blob Storage

```bash
python tests/test_blob.py

```

---

## Test Azure SQL Connection

```bash
python tests/test_sql.py
```

---

## Create Predictions Table

```bash
python -m azure.create_table
```

---

## Insert Sample Prediction

```bash
python -m azure.insert_prediction
```

---

## View Stored Predictions

```bash
python -m azure.view_predictions
```

```bash
python tests/test_eventhub.py
```

---

---

# Real time Workflow Section

Azure Blob Storage
        │
        ▼
Load Dataset
        │
        ▼
Stream Events
        │
        ▼
Azure Event Hub
        │
        ▼
Event Consumer
        │
        ▼
ML Prediction
        │
        ▼
Azure SQL Database


# 📸 Project Screenshots

---

# ✅ Phase 1 – Azure Blob Storage

### 1️⃣ Azure Resource Group

<img src="screenshots/phase_1/01-resource-group.png" width="900" alt="Azure Resource Group">

---

### 2️⃣ Create Azure Storage Account

<img src="screenshots/phase_1/02-create storage account.png" width="900" alt="Create Azure Storage Account">

---

### 3️⃣ Azure Storage Account Successfully Deployed

<img src="screenshots/phase_1/03-storage account successfully deployed.png" width="900" alt="Azure Storage Account Successfully Deployed">

---

### 4️⃣ Azure Blob Container

<img src="screenshots/phase_1/04-blob containers.png" width="900" alt="Azure Blob Container">

---

### 5️⃣ Dataset Uploaded to Azure Blob Storage

<img src="screenshots/phase_1/05-dataset uploaded.png" width="900" alt="Dataset Uploaded">

---

### 6️⃣ Project Structure (Phase 1)

<img src="screenshots/phase_1/06-python-structure.png" width="900" alt="Project Structure">

---

### 7️⃣ Dataset Successfully Loaded from Azure Blob Storage

<img src="screenshots/phase_1/07python-output.png" width="900" alt="Dataset Loaded Successfully">

---

# ✅ Phase 2 – Azure SQL Database

### 8️⃣ Updated Project Structure

<img src="screenshots/phase_2/08-project-structure-phase2.png" width="900" alt="Updated Project Structure">

---

### 9️⃣ Azure SQL Firewall Configuration

<img src="screenshots/phase_2/09-firewall-configuration.png" width="900" alt="Azure SQL Firewall Configuration">

---

### 🔟 Successful Azure SQL Connection

<img src="screenshots/phase_2/10-sql-connection-success.png" width="900" alt="Successful Azure SQL Connection">

---

### 1️⃣1️⃣ Predictions Table Created

<img src="screenshots/phase_2/11-predictions-table-created.png" width="900" alt="Predictions Table Created">

---

### 1️⃣2️⃣ Azure SQL Query Editor

<img src="screenshots/phase_2/12-query-editor.png" width="900" alt="Azure SQL Query Editor">

---

### 1️⃣3️⃣ Prediction Stored Successfully

<img src="screenshots/phase_2/13-prediction-record.png" width="900" alt="Prediction Stored Successfully">

---

# ✅ Phase 3 – Azure Event Hubs & Real-Time Streaming

### 1️⃣4️⃣ Azure Event Hub Namespace

<img src="screenshots/phase_3/14-eventhub namespace.png" width="900" alt="Azure Event Hub Namespace">

---

### 1️⃣5️⃣ Event Hub Deployment Completed

<img src="screenshots/phase_3/15-event hub deployment.png" width="900" alt="Event Hub Deployment">

---

### 1️⃣6️⃣ Azure Event Hub Created

<img src="screenshots/phase_3/16-event hub created.png" width="900" alt="Azure Event Hub Created">

---

### 1️⃣7️⃣ Azure Storage Networking Configuration

<img src="screenshots/phase_3/17-azure storage networking.png" width="900" alt="Azure Storage Networking">

---

### 1️⃣8️⃣ Predictions Stored in Azure SQL Database

<img src="screenshots/phase_3/18-azure sql predictions.png" width="900" alt="Azure SQL Predictions">

---

### 1️⃣9️⃣ Real-Time Event Streaming

<img src="screenshots/phase_3/19-event streaming.png" width="900" alt="Event Streaming">

---

### 2️⃣0️⃣ Event Consumer Processing Output

<img src="screenshots/phase_3/20-consumer output.png" width="900" alt="Consumer Output">

---
# ✅ Phase 4 – Azure Databricks Data Preprocessing

### 2️⃣1️⃣ Azure Blob Storage Dataset

<img src="screenshots/phase_4/21-azure_blob_storage.png" width="900" alt="Azure Blob Storage Dataset">

---

### 2️⃣2️⃣ Unity Catalog Setup

<img src="screenshots/phase_4/22-unity-catalog-setup.png" width="900" alt="Unity Catalog Setup">

---

### 2️⃣3️⃣ Azure Databricks Cluster

<img src="screenshots/phase_4/23- databrricks-cluster.png" width="900" alt="Azure Databricks Cluster">

---

### 2️⃣4️⃣ Dataset Uploaded to Unity Catalog Volume

<img src="screenshots/phase_4/24- dataset-uploaded-to-volume.png" width="900" alt="Dataset Uploaded to Unity Catalog Volume">

---

### 2️⃣5️⃣ Dataset Successfully Loaded into PySpark

<img src="screenshots/phase_4/25- reading_dataset.png" width="900" alt="Dataset Successfully Loaded">

---

### 2️⃣6️⃣ Dataset Schema Validation

<img src="screenshots/phase_4/26-dataset-schema.png" width="900" alt="Dataset Schema">

---

### 2️⃣7️⃣ Data Quality Analysis

<img src="screenshots/phase_4/27-missing_values.png" width="900" alt="Data Quality Analysis">

---

### 2️⃣8️⃣ Processed Dataset Saved as Parquet

<img src="screenshots/phase_4/28- parquet-dataset-output.png" width="900" alt="Processed Dataset Saved as Parquet">

---

# ✅ Phase 5 – Azure Machine Learning Model Training & Registration

### 2️⃣9️⃣ Azure Machine Learning Workspace

<img src="screenshots/phase_5/29-azure-machine-learning-workspace.png" width="900" alt="Azure Machine Learning Workspace">

---

### 3️⃣0️⃣ Azure ML Studio - Models

<img src="screenshots/phase_5/30-azure-ml-studio-models.png" width="900" alt="Azure ML Studio Models">

---

### 3️⃣1️⃣ Model Registered in Azure Machine Learning

<img src="screenshots/phase_5/31-model-registered.png" width="900" alt="Model Registered">

---

### 3️⃣2️⃣ Azure ML JupyterLab Environment

<img src="screenshots/phase_5/32-jupyterlab-environment.png" width="900" alt="Azure ML JupyterLab Environment">

---

### 3️⃣3️⃣ Azure ML Compute Instance Running

<img src="screenshots/phase_5/33-compute-instance-running.png" width="900" alt="Azure ML Compute Instance Running">

---

### 3️⃣4️⃣ Random Forest Model Evaluation

<img src="screenshots/phase_5/34-model-evaluation.png" width="900" alt="Random Forest Model Evaluation">

---

---

## Azure Databricks ETL

The Databricks notebook performs:

- Reads the CICIDS2018 dataset from a Unity Catalog Volume
- Validates the dataset schema
- Removes duplicate records
- Handles missing values
- Saves the processed dataset in Parquet format
- Stores the processed dataset inside Unity Catalog for downstream processing

# 🎓 Skills Demonstrated

-- Microsoft Azure
- Azure Blob Storage
- Azure Event Hubs
- Azure SQL Database
- Machine Learning
- Gradient Boosting Classifier
- Event-Driven Architecture
- Real-Time Data Streaming
- Python
- Cloud Computing
- Data Engineering
- SQL
- Git & GitHub

---

# 🗺 Azure Migration Roadmap

| Phase | Description | Status |
|--------|-------------|--------|
| Azure Blob Storage | Cloud storage for the CICIDS2018 dataset | ✅ Completed |
| Azure SQL Database | Store intrusion detection predictions | ✅ Completed |
| Azure Event Hubs | Real-time network traffic streaming | ✅ Completed |
| Azure Databricks | PySpark ETL pipeline with Unity Catalog and Parquet processing | ✅ Completed |
| Azure Machine Learning | Model training, evaluation, registration, and versioning | ✅ Completed |
| Azure ML Online Endpoint | Deploy the trained model for real-time inference | ⏳ Next |
| Power BI Dashboard | Real-time visualization of prediction results | ⏳ Planned |
| Azure Key Vault | Secure storage of secrets and connection strings | ⏳ Planned |
| Azure Monitor | Monitoring, diagnostics, and logging | ⏳ Planned |

---

# 🚀 Future Enhancements

- Process streaming data with Azure Databricks
- Deploy intrusion detection models using Azure Machine Learning
- Store prediction history in Azure SQL Database
- Build real-time dashboards with Power BI
- Secure secrets using Azure Key Vault
- Monitor application health using Azure Monitor

---

# 👨‍💻 Author

**Anto Sojan**

MSc Big Data Management & Analytics

Dublin, Ireland

---

# 🌟 Project Vision

This repository documents my journey of transforming a traditional Network Intrusion Detection System into a cloud-native cybersecurity platform using Microsoft Azure.

Each completed phase introduces a new Azure service while maintaining a scalable, secure, and production-oriented architecture.

The final solution will integrate Azure Blob Storage, Azure Event Hubs, Azure Databricks, Azure Machine Learning, Azure SQL Database, and Power BI to create a complete real-time cloud-native intrusion detection system.
