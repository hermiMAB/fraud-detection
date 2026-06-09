# Fraud Detection System: Adey Innovations Inc.

## Project Overview
[cite_start]This project aims to improve fraud detection capabilities for Adey Innovations Inc. by building a robust machine learning pipeline for both e-commerce and bank credit card transaction streams[cite: 8, 9]. [cite_start]The system addresses the critical business challenge of balancing financial loss from missed fraud (false negatives) against the erosion of customer trust caused by flagging legitimate transactions (false positives)[cite: 10, 11].

## Current Project Status (Interim-1)
[cite_start]As of the Interim-1 submission, the project has successfully completed the data understanding and preprocessing phase[cite: 179]:
* [cite_start]**Data Cleaning**: Implemented rigorous cleaning procedures, including removing duplicates and dropping missing values to prevent bias[cite: 107, 108, 109].
* [cite_start]**Exploratory Data Analysis (EDA)**: Conducted univariate and bivariate analysis to quantify class imbalance and identify key fraud drivers[cite: 111, 112, 113, 114].
* **Feature Engineering**:
    * [cite_start]Engineered temporal features including `hour_of_day`, `day_of_week`, and `time_since_signup`[cite: 122, 123, 124, 125].
    * [cite_start]Integrated geolocation by mapping IP addresses to country ranges using efficient `merge_asof` lookup techniques[cite: 115, 116, 117].
* [cite_start]**Modular Pipeline**: Developed a reusable `src/` module for data cleaning and preprocessing to ensure code robustness and testability[cite: 46, 92].
* [cite_start]**Imbalance Handling Strategy**: Prepared for model training by implementing stratified splitting and SMOTE to address the minority class representation[cite: 129, 130, 139].

## Project Structure
[cite_start]The repository is organized to ensure reproducibility and modularity[cite: 46, 70]:

```text
fraud-detection/
├── data/
│   ├── raw/           # Original datasets
│   └── processed/     # Cleaned and feature-engineered data
├── notebooks/         # Exploratory and analysis notebooks
├── src/               # Reusable cleaning and transformation functions
├── models/            # Saved model artifacts
├── requirements.txt   # Environment dependencies
└── README.md          # Project documentation

pip install -r requirements.txt

Resampling: We chose SMOTE (Synthetic Minority Over-sampling Technique) over undersampling to avoid losing critical information in the majority class while effectively boosting the minority fraud class representation.  Data Cleaning: Rows with missing values were dropped rather than imputed to ensure that the behavioral patterns analyzed in fraud detection remain authentic to user actions.