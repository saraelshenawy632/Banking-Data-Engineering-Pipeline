# 🏦 Banking Data Engineering Pipeline

An end-to-end **Banking Data Engineering Pipeline** built using **Databricks, PySpark, Delta Lake, and Apache Airflow**.

The project demonstrates how raw banking transaction data can be processed through a **Bronze → Silver → Gold** architecture, followed by comprehensive **Data Quality validation** and workflow orchestration using Apache Airflow.

---

## 📌 Project Overview

The objective of this project is to build a scalable data engineering pipeline for banking data that covers:

* Data ingestion
* Data cleaning and transformation
* Medallion Architecture
* Delta Lake storage
* Business-level data modeling
* Data quality validation
* Pipeline orchestration
* Banking KPI generation

The pipeline transforms raw banking records into reliable Gold-layer datasets ready for analytics and reporting.

---

## 🏗️ Architecture

```text
                    ┌──────────────────┐
                    │   Source Data    │
                    │      Excel       │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │  Bronze Layer    │
                    │   Raw Data       │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │  Silver Layer    │
                    │ Clean & Transform│
                    └────────┬─────────┘
                             │
                ┌────────────┼────────────┐
                ▼            ▼            ▼
        ┌────────────┐ ┌────────────┐ ┌───────────────┐
        │Gold Account│ │ Gold Daily │ │Gold Transaction│
        │   Summary  │ │    KPIs    │ │    Analysis   │
        └──────┬─────┘ └──────┬─────┘ └───────┬───────┘
               │              │                │
               └──────────────┼────────────────┘
                              ▼
                    ┌──────────────────┐
                    │  Data Quality    │
                    │    Validation    │
                    └──────────────────┘

                    Apache Airflow
                           │
                           ▼
                  Pipeline Orchestration
```

---

## 🔄 Pipeline Flow

The pipeline follows the **Medallion Architecture**:

### 🥉 Bronze Layer

The Bronze layer stores the raw ingested banking data with minimal transformation.

Main responsibilities:

* Load raw banking data
* Preserve source information
* Store the initial dataset
* Add ingestion metadata where required

Notebook:

```text
01_bronze
```

---

### 🥈 Silver Layer

The Silver layer prepares the data for analytics by applying cleaning and transformation logic.

Main responsibilities:

* Data cleaning
* Handling invalid records
* Data type transformations
* Removing unwanted records
* Preparing reliable datasets for the Gold layer

Notebook:

```text
02_silver
```

---

### 🥇 Gold Layer

The Gold layer contains business-ready datasets designed for analytics and reporting.

### Gold Account Summary

Provides account-level aggregated information.

Notebook:

```text
03_gold_account
```

### Gold Daily Banking KPIs

Generates daily banking metrics and KPIs.

Notebook:

```text
04_gold_daily
```

### Gold Transaction Analysis

Provides transaction-level analytical outputs.

Notebook:

```text
05_gold_transaction
```

---

## ✅ Data Quality

A dedicated Data Quality layer validates the final Gold datasets.

The validation includes checks such as:

* Table existence
* Row counts
* NULL values
* Key field validation
* Transaction data validation
* Gold table validation

Notebook:

```text
06_data_quality
```

---

## ⚙️ Apache Airflow Orchestration

Apache Airflow is used to orchestrate the end-to-end Databricks pipeline.

The DAG executes the notebooks in the required dependency order:

```text
Bronze
   ↓
Silver
   ↓
 ┌───────────────┬───────────────┐
 ▼               ▼               ▼
Gold Account   Gold Daily   Gold Transaction
 └───────────────┴───────────────┘
                  ↓
            Data Quality
```

The Airflow DAG uses:

```text
DatabricksSubmitRunOperator
```

to submit Databricks notebook tasks.

DAG:

```text
airflow/banking_data_pipeline.py
```

---

## 🛠️ Technology Stack

### Data Engineering

* Python
* PySpark
* Apache Spark
* Databricks
* Delta Lake
* Apache Airflow

### Data Processing

* Data Ingestion
* ETL
* Data Cleaning
* Data Transformation
* Data Aggregation
* Data Quality

### Data Architecture

* Medallion Architecture
* Bronze Layer
* Silver Layer
* Gold Layer

### Analytics

* Banking KPIs
* Account-level Analysis
* Transaction Analysis
* Daily Metrics

---

## 📊 Project Results

The pipeline successfully processes the banking dataset through multiple processing layers.

### Data Processing

```text
Raw Records
116,201
     ↓
Cleaned Records
116,162
```

### Gold Layer Outputs

```text
Gold Account Summary
10 records

Gold Daily Banking KPIs
1,294 records

Gold Transaction Analysis
2 records
```

These outputs were validated through the dedicated Data Quality notebook.

---

## 📁 Project Structure

```text
Banking-Data-Engineering-Pipeline/
│
├── README.md
│
├── databricks/
│   ├── 01_bronze.py
│   ├── 02_silver.py
│   ├── 03_gold_account.py
│   ├── 04_gold_daily.py
│   ├── 05_gold_transaction.py
│   └── 06_data_quality.py
│
├── airflow/
│   └── banking_data_pipeline.py
│
└── screenshots/
    └── banking_pipeline.png
```

---

## 🚀 Key Skills Demonstrated

This project demonstrates practical experience with:

* Building end-to-end data pipelines
* PySpark DataFrame processing
* Databricks development
* Delta Lake
* Medallion Architecture
* ETL pipeline development
* Data quality validation
* Data transformation
* Business KPI generation
* Apache Airflow orchestration
* Integrating Airflow with Databricks

---

## 🎯 Project Goal

The project was developed as a practical **Data Engineering portfolio project** to demonstrate the ability to design, build, validate, and orchestrate an end-to-end data pipeline using modern data engineering technologies.

---

## 👩‍💻 Author

**Sara Elshenawy**

B.Sc. Business Information Systems (BIS)
Tanta University

**Focus:** Data Engineering | Business Intelligence | Data Analytics

---

⭐ If you find this project useful, feel free to explore the notebooks and pipeline implementation.
