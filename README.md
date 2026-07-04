# ☁️ Azure Network Intrusion Detection System

## Cloud-Native Real-Time Network Intrusion Detection using Microsoft Azure

![Azure](https://img.shields.io/badge/Microsoft-Azure-0078D4?logo=microsoftazure\&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.13-3776AB?logo=python\&logoColor=white)
![Status](https://img.shields.io/badge/Phase-1%20Completed-success)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📖 Project Overview

This project is the **cloud-native implementation** of my MSc dissertation:

> **Real-Time Network Intrusion Detection System using Big Data Technologies and Machine Learning**

The objective is to migrate a traditional big data intrusion detection pipeline into **Microsoft Azure**, replacing local infrastructure with scalable cloud services.

Instead of building a sample Azure application, this repository demonstrates the migration of a real-world cybersecurity project to Azure, one service at a time.

---

# 🎯 Project Objectives

* Build a cloud-native Network Intrusion Detection System (NIDS)
* Learn Microsoft Azure through practical implementation
* Replace local storage with Azure Blob Storage
* Implement cloud-native data engineering practices
* Develop a production-ready Azure portfolio project

---

# 🚀 Phase 1 – Azure Blob Storage (Completed)

### ✔ Completed Tasks

* Created Azure Resource Group
* Created Azure Storage Account
* Configured Azure Blob Storage
* Created Blob Container
* Uploaded preprocessed CICIDS2018 dataset
* Configured secure environment variables (.env)
* Integrated Azure Storage Blob SDK
* Loaded dataset directly from Azure Blob Storage using Python

---

# 🏗️ Phase 1 Architecture

```text
                     Azure Cloud

        +------------------------------------+
        |        Azure Blob Storage          |
        |                                    |
        |   balanced_dataset.csv             |
        +----------------+-------------------+
                         |
                         |
                         ▼
        +------------------------------------+
        | Python Azure Blob Storage SDK      |
        |        blob_storage.py             |
        +----------------+-------------------+
                         |
                         ▼
        +------------------------------------+
        |      Pandas DataFrame              |
        |      Shape (300000 × 80)           |
        +------------------------------------+
```

---

# 💻 Technologies Used

## Cloud Platform

* Microsoft Azure
* Azure Blob Storage

## Programming Language

* Python 3.13

## Python Libraries

* pandas
* azure-storage-blob
* python-dotenv

## Version Control

* Git
* GitHub

---

# 📂 Project Structure

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

# 📊 Dataset Information

| Attribute | Value              |
| --------- | ------------------ |
| Dataset   | CICIDS2018         |
| Records   | 300,000            |
| Features  | 80                 |
| Storage   | Azure Blob Storage |

---

# ▶️ Running the Project

## Clone Repository

```bash
git clone https://github.com/ANTOSOJAN/Azure-Network-Intrusion-System.git
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Environment Variables

Create a `.env` file:

```env
AZURE_STORAGE_CONNECTION_STRING=YOUR_CONNECTION_STRING
CONTAINER_NAME=datasets
BLOB_NAME=balanced_dataset.csv
```

## Run the Application

```bash
python test_blob.py
```

---

# 📸 Project Screenshots

## 1️⃣ Azure Resource Group

<img src="screenshots/01-resource-group.png" width="900">

---

## 2️⃣ Azure Storage Account

<img src="screenshots/02-create storage account.png" width="900">

---

## 3️⃣ Storage Account Successfully Deployed

<img src="screenshots/03-storage account successfully deployed.png" width="900">

---

## 4️⃣ Azure Blob Container

<img src="screenshots/04-blob containers.png" width="900">

---

## 5️⃣ Dataset Uploaded to Azure Blob Storage

<img src="screenshots/05-dataset uploaded.png" width="900">

---

## 6️⃣ Project Structure

<img src="screenshots/06-python-structure.png" width="900">

---

## 7️⃣ Dataset Successfully Loaded from Azure

<img src="screenshots/07python-output.png" width="900">

---

# 🎓 Skills Demonstrated

* Microsoft Azure
* Azure Blob Storage
* Cloud Computing
* Cloud Storage
* Python Development
* Data Engineering
* Environment Variable Management
* Git & GitHub
* Pandas
* Azure SDK Integration

---

# 🗺️ Azure Migration Roadmap

| Phase                              | Status      |
| ---------------------------------- | ----------- |
| ✅ Phase 1 – Azure Blob Storage     | Completed   |
| ⏳ Phase 2 – Azure SQL Database     | In Progress |
| ⏳ Phase 3 – Azure Event Hubs       | Planned     |
| ⏳ Phase 4 – Azure Databricks       | Planned     |
| ⏳ Phase 5 – Azure Machine Learning | Planned     |
| ⏳ Phase 6 – Power BI Dashboard     | Planned     |

---

# 🌟 Future Enhancements

* Store prediction results in Azure SQL Database
* Replace local Kafka with Azure Event Hubs
* Process streaming data using Azure Databricks
* Deploy trained ML models with Azure Machine Learning
* Build an interactive dashboard using Power BI
* Integrate Azure Key Vault for secret management
* Add Azure Monitor for logging and monitoring

---

# 👨‍💻 Author

**Anto Sojan**

📍 Dublin, Ireland

---

## ⭐ Project Vision

This repository documents my journey of transforming a traditional big data Network Intrusion Detection System into a modern cloud-native cybersecurity solution using Microsoft Azure.

Each completed phase introduces a new Azure service while maintaining a scalable and production-oriented architecture.
