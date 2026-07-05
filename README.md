# ☁️ Azure Network Intrusion Detection System

## Cloud-Native Real-Time Network Intrusion Detection using Microsoft Azure

![Azure](https://img.shields.io/badge/Microsoft-Azure-0078D4?logo=microsoftazure&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Phase-3%20Completed-success)
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

# 🏗 Current System Architecture

                            Microsoft Azure

        +-------------------------------+
        |      Azure Blob Storage       |
        | balanced_dataset.csv          |
        +---------------+---------------+
                        |
                        ▼
             Dataset Streaming Script
                        |
                        ▼
        +-------------------------------+
        |      Azure Event Hub          |
        | Real-Time Network Events      |
        +---------------+---------------+
                        |
                        ▼
        Event Hub Consumer (Python)
                        |
                        ▼
       Machine Learning Prediction
      Gradient Boosting Classifier
                        |
                        ▼
        +-------------------------------+
        |      Azure SQL Database       |
        | Prediction Logs               |
        +-------------------------------+

---

# 💻 Technologies Used

## Cloud

- Microsoft Azure
- Azure Blob Storage
- Azure SQL Database
- Azure Event Hubs

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
├── models/
│   ├── best_ids_model.pkl
│   ├── scaler.pkl
│   └── feature_columns.pkl
│
├── tests/
│   ├── test_blob.py
│   ├── test_eventhub.py
│   ├── test_predictor.py
│   ├── test_stream_dataset.py
│   └── test_sql.py
│
├── screenshots/
│   ├── phase1/
│   ├── phase2/
│   └── phase3/
│
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

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

### 1️⃣ Azure Resource Group

<img src="screenshots/01-resource-group.png" width="900" alt="Azure Resource Group">

---

### 2️⃣ Create Azure Storage Account

<img src="screenshots/02-create%20storage%20account.png" width="900" alt="Create Azure Storage Account">

---

### 3️⃣ Azure Storage Account Successfully Deployed

<img src="screenshots/03-storage%20account%20successfully%20deployed.png" width="900" alt="Storage Account Successfully Deployed">

---

### 4️⃣ Azure Blob Container

<img src="screenshots/04-blob%20containers.png" width="900" alt="Azure Blob Container">

---

### 5️⃣ Dataset Uploaded to Azure Blob Storage

<img src="screenshots/05-dataset%20uploaded.png" width="900" alt="Dataset Uploaded">

---

### 6️⃣ Project Structure

<img src="screenshots/06-python-structure.png" width="900" alt="Project Structure">

---

### 7️⃣ Dataset Successfully Loaded from Azure Blob Storage

<img src="screenshots/07python-output.png" width="900" alt="Dataset Loaded Successfully">

---
---

## Phase 2 – Azure SQL Database

<img src="screenshots/08-project-structure-phase2.png.png" width="900" alt="Updated Project Structure">

<img src="screenshots/09-firewall-configuration.png.png" width="900" alt="Azure SQL Firewall Configuration">

<img src="screenshots/10-sql-connection-success.png.png" width="900" alt="Successful Azure SQL Connection">

<img src="screenshots/11-predictions-table-created.png.png" width="900" alt="Predictions Table Created">

<img src="screenshots/12-query-editor.png.png" width="900" alt="Azure SQL Query Editor">

<img src="screenshots/13-prediction-record.png.png" width="900" alt="Prediction Stored Successfully">

---

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

| Phase | Status |
|--------|--------|
| ✅ Azure Blob Storage | Completed |
| ✅ Azure SQL Database | Completed |
| ✅ Azure Event Hubs | Completed |
| ⏳ Azure Databricks | Next |
| ⏳ Azure Machine Learning | Planned |
| ⏳ Power BI Dashboard | Planned |
| ⏳ Azure Key Vault | Planned |

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
