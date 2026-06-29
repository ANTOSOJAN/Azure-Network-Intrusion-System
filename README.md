# Azure Network Intrusion Detection System

## Cloud-Native Real-Time Network Intrusion Detection using Microsoft Azure

![Azure](https://img.shields.io/badge/Microsoft-Azure-0078D4?logo=microsoftazure\&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Status](https://img.shields.io/badge/Phase-1%20Complete-success)
![License](https://img.shields.io/badge/License-MIT-green)

---

# Project Overview

This project is the cloud-native evolution of my MSc dissertation, **Real-Time Network Intrusion Detection System**.

The goal is to migrate a traditional big data intrusion detection pipeline into Microsoft Azure by integrating Azure cloud services step by step while maintaining a scalable, secure, and production-ready architecture.

**Current Phase:** Azure Blob Storage Integration

---

# Objectives

* Learn Microsoft Azure through a real-world cybersecurity project
* Build a scalable cloud-native Network Intrusion Detection System (NIDS)
* Replace local infrastructure with Azure services
* Demonstrate cloud engineering and data engineering skills
* Develop a portfolio-quality Azure project

---

# Phase 1 – Azure Blob Storage

### Completed

* Azure Resource Group
* Azure Storage Account
* Azure Blob Container
* Uploaded preprocessed CICIDS2018 dataset
* Secure environment configuration using `.env`
* Azure Blob Storage SDK integration
* Download dataset directly from Azure Blob Storage
* Load dataset into a Pandas DataFrame

---

# Azure Architecture

```text
Azure Blob Storage
        │
        ▼
balanced_dataset.csv
        │
        ▼
Python Azure Storage SDK
(blob_storage.py)
        │
        ▼
Pandas DataFrame
(300000 × 80)
```

---

# Technologies Used

## Cloud

* Microsoft Azure
* Azure Blob Storage

## Programming

* Python 3.13

## Libraries

* pandas
* azure-storage-blob
* python-dotenv

## Version Control

* Git
* GitHub

---

# Dataset

| Item     | Details            |
| -------- | ------------------ |
| Dataset  | CICIDS2018         |
| Records  | 300,000            |
| Features | 80                 |
| Storage  | Azure Blob Storage |

---

# Project Structure

```text
Azure-Network-Intrusion-System/

│
├── azure/
│   ├── __init__.py
│   └── blob_storage.py
│
├── screenshots/
│
├── docker-compose.yaml
├── requirements.txt
├── test_blob.py
├── README.md
├── LICENSE
└── .gitignore
```

---

# Running the Project

Clone the repository

```bash
git clone https://github.com/ANTOSOJAN/Azure-Network-Intrusion-System.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file containing:

```
AZURE_STORAGE_CONNECTION_STRING=your_connection_string
CONTAINER_NAME=datasets
BLOB_NAME=balanced_dataset.csv
```

Run the test script

```bash
python test_blob.py
```

---

# Skills Demonstrated

* Microsoft Azure
* Azure Blob Storage
* Cloud Storage
* Cloud Data Engineering
* Python Development
* Environment Variable Management
* Git & GitHub
* Data Processing with Pandas

---

# Project Roadmap

* ✅ Phase 1 – Azure Blob Storage
* ⏳ Phase 2 – Azure SQL Database
* ⏳ Phase 3 – Azure Event Hubs
* ⏳ Phase 4 – Azure Databricks
* ⏳ Phase 5 – Azure Machine Learning
* ⏳ Phase 6 – Power BI Dashboard

---

# Author

**Anto Sojan**

MSc Big Data Management & Analytics

---

> **This repository documents my journey of transforming a traditional big data intrusion detection system into a cloud-native solution using Microsoft Azure.**
