**Module 1: ** 
**Data Pipeline - Books to SQLite ETL**
**Overview**
This project builds an end-to-end data pipeline that scrapes book data from BooksToScrape, cleans and transforms the data, converts prices from EURO to INR, stores it in a normalized SQLite database, and performs SQL and pandas-based analysis.

**Dataset**
Source: http://books.toscrape.com/

**Fields collected:**

Title
Price (EURO)
Star Rating
Availability
Category
Data Cleaning
Converted price to price_gbp (float)
Converted ratings (One-Five) to integers (1-5)
Converted availability to boolean in_stock
Applied median imputation for numeric parsing issues
Currency Conversion
Fixed project rate:

**1 EURO = 105.50 INR**

price_inr = price_gbp * 105.50

**Database Schema**
categories
category_id (PK)
category_name
books
book_id (PK)
title
price_gbp
price_inr
rating
in_stock
category_id (FK)

**SQL Queries Performed**
SELECT + WHERE
ORDER BY
LIMIT
DISTINCT
BETWEEN / IN

**JOIN between books and categories**
Pandas Validation
Loaded query results using pd.read_sql()
Recreated JOIN using pd.merge()
Verified both outputs matched

**Results**
Books scraped: ...
Categories scraped: ...
Database tables: 2
SQL queries executed: 5+
JOIN validation completed


**Design Decisions**
SQLite used for simplicity and portability.
Normalized schema reduces data redundancy.
Median imputation prevents pipeline failures from malformed values.

**Module 2**
**
Titanic Survival Prediction: Analytics Pipeline
Introduction**

This project implements a complete data analytics and machine learning pipeline using the Titanic dataset. The objective is to identify the key factors influencing passenger survival and develop predictive models capable of accurately classifying survival outcomes. The project follows a structured data science workflow consisting of data profiling, data cleaning, exploratory data analysis (EDA), feature engineering, predictive modeling, model evaluation, hyperparameter optimization, and model deployment.

**Project Workflow**

The project was executed in the following sequence:

**Step 1: Data Loading and Profiling**

The Titanic dataset was loaded using Seaborn and immediately saved as a local CSV file (titanic.csv) for offline reproducibility.

**The dataset was profiled using:**

Dataset dimensions (shape)
Data types (info)
Statistical summary (describe)
Missing value analysis

**Purpose:**
 To understand the structure, quality, and completeness of the data before any analysis.

**Step 2: Data Cleaning and Missing Value Treatment**

Missing values were analyzed column-wise and handled according to predefined thresholds.

**Key cleaning activities included:**

Removing rows with very small percentages of missing values
Imputing numerical variables using median values
Imputing categorical variables using mode values
Dropping highly incomplete variables where reliable imputation was not possible

**Purpose:**
 To improve data quality and ensure reliable downstream analysis.

**Step 3: Exploratory Data Analysis (EDA)**

EDA was conducted to understand survival patterns and passenger characteristics.

**Analysis included:**

Distribution of Age and Fare
Outlier detection using IQR
Survival analysis by Gender
Survival analysis by Passenger Class
Correlation analysis
Multivariate visualization

**Purpose:**
 To discover relationships between features and survival outcomes.

**Step 4: Feature Engineering**

Additional preprocessing and feature preparation were performed prior to model training.

**Activities included:**

Handling missing values
One-Hot Encoding categorical variables
Creating dummy variables
Standardizing numerical features
Preparing train and test datasets

**Purpose:**
 To convert raw data into a machine-learning-ready format.

**Predictive Models Developed**

Three classification models were developed and compared using the same prepared dataset.

**1. Logistic Regression
Introduction**

Logistic Regression is a supervised machine learning algorithm used for binary classification problems. It estimates the probability that an observation belongs to a particular class.

**Why Logistic Regression?**
Simple and interpretable
Fast training process
Produces probability scores
Serves as a strong baseline model
Application in This Project

Logistic Regression was used to predict whether a passenger survived (1) or did not survive (0) based on passenger characteristics.

**Expected Benefits**
Easy interpretation of feature impact
Good performance on structured datasets
Useful benchmark for comparing advanced models


**2. CHAID Decision Tree
Introduction**

CHAID (Chi-Square Automatic Interaction Detection) is a decision tree technique that creates splitting rules using Chi-Square statistical tests.

**Why CHAID?**
Highly interpretable
Creates understandable business rules
Captures interactions between variables
Effective with categorical data
Application in This Project

The CHAID model was developed to identify the most important survival decision paths and explain passenger outcomes through rule-based segmentation.

**Expected Benefits**
Transparent predictions
Easy visualization
Strong business interpretability



**3. Random Forest
Introduction**

Random Forest is an ensemble learning method that combines multiple decision trees and aggregates their predictions.

**Why Random Forest?**
Handles nonlinear relationships
Reduces overfitting
Provides high predictive accuracy
Robust to noisy data
Application in This Project

Random Forest was implemented to improve prediction accuracy and identify the most influential survival factors.

**Expected Benefits**
Strong generalization performance
Better handling of complex interactions
Usually achieves higher predictive accuracy than individual decision trees


**Model Evaluation Process**

All models were evaluated using the same test dataset.

The following metrics were used:

**Accuracy**

Measures overall prediction correctness.

**Precision**

Measures how many predicted survivors were actually survivors.

**Recall**

Measures how many actual survivors were correctly identified.

**F1-Score**

Balances Precision and Recall into a single metric.

**ROC-AUC**

Measures the model's ability to distinguish between survivors and non-survivors across different decision thresholds.

**Confusion Matrix**

Provides detailed insight into correct and incorrect classifications.

**Class Imbalance Handling**

Three approaches were compared:

**Baseline Model**

Original class distribution without modification.

**Class Weight Adjustment**

Applied higher importance to minority-class observations using:

class_weight='balanced'
Show more lines
SMOTE Oversampling

Generated synthetic samples for the minority class using training data only.

**Purpose:**
 To evaluate whether balancing techniques improve model performance, particularly Recall and F1 Score.

**Hyperparameter Optimization**

Random Forest parameters were tuned using GridSearchCV.

**Parameters optimized:**

Number of trees (n_estimators)
Maximum tree depth (max_depth)
Number of features considered at each split (max_features)

**Purpose:**
 To identify the best parameter combination that maximizes model performance and generalization.


**Model Comparison and Selection**

**All classification models were compared using:**

Accuracy
Precision
Recall
F1 Score
ROC-AUC

**The final model selection was based on:**

Predictive performance
Generalization ability
Stability across evaluation metrics
Practical deployment suitability
Model Deployment

The best-performing pipeline was saved using Joblib.

**The saved artifact includes:**

Missing value handling
Feature encoding
Feature scaling
Trained machine learning model

**Purpose:**
 To enable end-to-end prediction on new raw passenger data without requiring manual preprocessing.

**Conclusion**

This project demonstrates a complete analytics-to-machine-learning workflow, starting from raw Titanic passenger data and progressing through data cleaning, exploratory analysis, feature engineering, predictive modeling, model optimization, and deployment. Logistic Regression provided a strong baseline, CHAID delivered interpretable business rules, and Random Forest offered an advanced ensemble approach for improved predictive performance. The final solution identifies the key drivers of passenger survival and delivers a deployable predictive analytics pipeline.





**Module 3**
**Zepto Support Assistant**

A Retrieval-Augmented Generation (RAG) based customer support assistant built for Zepto using **FastAPI, LangGraph, ChromaDB, and Pydantic**.

The application answers customer queries related to Zepto policies such as:

Delivery Policy
Return & Refund Policy
Membership Plans
Order Tracking
Order Cancellation
Damaged/Missing Items
Gift Cards
Customer Support Hours

The system uses a LangGraph-powered workflow, retrieves relevant policy documents from a vector database, and returns structured JSON responses with confidence scores and source references.


**Project Objectives**

This project demonstrates:

Document ingestion

Vector embeddings and retrieval

ChromaDB integration

LangGraph orchestration

Intent classification

Structured JSON responses

FastAPI REST API

Docker containerization

Cloud deployment using Render

**Architecture Overview**
User Query
    │
    ▼
LangGraph Workflow
    │
    ▼
Intent Classification
    │
 ┌──┴─────────────┐
 │                │
 ▼                ▼
Policy Query   General Query
 │                │
 ▼                ▼
Retrieve Docs   Direct Answer
 │
 ▼
ChromaDB Search
 │
 ▼
Generate Response
 │
 ▼
Pydantic Validation
 │
 ▼
JSON Response


**Project Structure**
Zepto_Santhosh_Support_Assistant/
│
├── app/
│   │
│   ├── docs/
│   │    ├── doc_01.txt
│   │    ├── doc_02.txt
│   │    ├── doc_03.txt
│   │    ├── doc_04.txt
│   │    ├── doc_05.txt
│   │    ├── doc_06.txt
│   │    ├── doc_07.txt
│   │    └── doc_08.txt
│   │
│   ├── db.py
│   ├── ingest.py
│   ├── rag.py
│   ├── graph.py
│   ├── prompts.py
│   ├── models.py
│   ├── main.py
│   ├── Dockerfile
│   ├── render.yaml
│   ├── requirements.txt
│   └── test.py
│
└── README.md

**Requirements Explanation**

fastapi
uvicorn
chromadb
langgraph
pydantic

**FastAPI**
Used to create REST APIs and expose the /ask endpoint.
**Purpose**
API development
Request handling
Response serialization

**Uvicorn**
ASGI web server used to run FastAPI applications.
Purpose
uvicorn main:app --reload
Starts FastAPI server
Handles incoming requests


**ChromaDB**
Vector database used for storing and searching embedded policy documents.
**Purpose**
Stores document embeddings
Semantic similarity search
Retrieves top matching policy chunks

**LangGraph**
Used for workflow orchestration.
**Purpose**
Controls the application flow:

classify_intent
        │
        ▼
retrieve_and_answer
        OR
direct_answer

**Pydantic**
Data validation framework.
**Purpose**
Validates request and response schemas.
Example:
{
  "answer": "Refunds are processed...",
  "sources": ["doc_02"],
  "confidence": 1.0
}


**Module Explanation**
1. ingest.py
Responsible for loading policy documents.
Tasks
Read all 8 documents
Create chunks
Prepare data for storage
**2. db.py**
Handles ChromaDB operations.
**Tasks**
Create collection
Store embeddings
Retrieve matching documents

**3. rag.py**
Contains Retrieval-Augmented Generation logic.
**Tasks**
Receive query
Search vector database
Return relevant chunks

**4. prompts.py**
Stores structured prompt templates.
Uses:
Role
Context
Task
Format
Length
**5. graph.py**
Contains LangGraph workflow.
Nodes
classify_intent
Determines whether query is:
policy_question

**retrieve_and_answer**
For policy-related questions.
**Steps:**
Retrieve documents
Build answer
Return sources

**direct_answer**
For non-policy questions.
Returns:
I can only answer questions about Zepto policies right now.

**6. models.py**
Contains Pydantic models.
**QueryRequest**
{
    "query": str
}
**AnswerResponse**
{
   "answer": str,
   "sources": list,
   "confidence": float
}

**7. main.py**
FastAPI entrypoint.
Provides:

**LangGraph Workflow**
START
  │
  ▼
classify_intent
  │
  ├────────────► direct_answer
  │
  ▼
retrieve_and_answer
  │
  ▼
END

**
Example API Calls
Example 1: Policy Question**
**Request**
{
    "query": "What is the refund policy?"
}
**Response**
{
  "answer": "Based on the retrieved context: Grocery and perishable items may be reported for a return within 24 hours...",
  "sources": [
    "doc_02"
  ],
  "confidence": 1.0
}

**Example 2: General Question**
**Request**
{
    "query": "Who won the cricket world cup?"
}
**Response**
{
  "answer": "I can only answer questions about Zepto policies right now.",
  "sources": [],
  "confidence": 1.0
}

**Deployment**
The application was deployed successfully using Render.

**Deployment URL**
https://zepto-santhosh-support-assistant.onrender.com
https://zepto-santhosh-support-assistant.onrender.com/docs

**Features Verified**

FastAPI application startup
API documentation
LangGraph execution
ChromaDB retrieval
JSON responses

**Conclusion**
This project implements a complete GenAI-powered Zepto Support Assistant using a Retrieval-Augmented Generation (RAG) architecture. The solution combines FastAPI, LangGraph, ChromaDB, Pydantic, and Docker to provide grounded, structured, and scalable responses to customer support questions. The application satisfies all Module 3 requirements and has been successfully deployed on Render for public access and testing.
