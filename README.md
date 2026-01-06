## Model Aging Detector

This project is a machine learning monitoring system that focuses on detecting **model aging**.
Instead of relying only on accuracy, the system checks whether a trained model is becoming
**unstable or uncertain** in its predictions over time.

The project is designed to work with **any tabular dataset**. Only the target column name
needs to be specified.

---

## Motivation

In many machine learning projects, models are evaluated only using accuracy.
However, in real-world scenarios, a model can still show good accuracy while its
internal decision logic slowly degrades.

This project attempts to identify such hidden degradation by monitoring:
- Prediction confidence
- Stability of model behavior
- Changes in decision consistency

---

## Project Overview

The system follows these steps:

1. Load a dataset (CSV format)
2. Split the data into a baseline part and a current part
3. Train a machine learning model on baseline data
4. Save the trained model and feature structure
5. Compare prediction behavior on current data
6. Detect whether the model is stable or showing signs of aging
7. Display results using a Streamlit dashboard

---

## Folder Structure

ModelAgingDetector/
├── data/raw/dataset.csv
├── models/
│   ├── base_model.pkl
│   └── feature_columns.pkl
├── dashboard/app.py
├── experiments/synthetic_data/
├── reports/aging_report.txt
└── src/
    ├── data/
    ├── model/
    ├── monitoring/
    ├── utils/
    └── main.py

---

## Key Idea Used

Instead of checking only prediction accuracy, the project calculates:

Instability = variance of prediction confidence

If the confidence values fluctuate a lot, the model is considered unstable,
even if accuracy looks acceptable.

---

## How to Run the Project

From the project root directory:

python src/main.py
python -m streamlit run dashboard/app.py

---

## Model Health Status

Low instability  -> MODEL HEALTHY  
High instability -> WARNING: UNSTABLE PREDICTIONS  

The instability threshold can be adjusted based on requirements.

---

## Datasets Used for Testing (Examples)

This project supports **any tabular dataset**.
Below are some datasets that were tested or are suitable for testing.

### 1. Titanic Survival Dataset
Link:
https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv

Target column:
Survived

Code change:
TARGET_COLUMN = "Survived"

---

### 2. Heart Disease Dataset
Link:
https://raw.githubusercontent.com/anshupandey/Machine-Learning/master/MLDatasets/heart.csv

Target column:
target

Code change:
TARGET_COLUMN = "target"

---

### 3. Credit Card Default Dataset
Link:
https://archive.ics.uci.edu/ml/machine-learning-databases/00350/default%20of%20credit%20card%20clients.xls

Target column:
default.payment.next.month

Code change:
TARGET_COLUMN = "default.payment.next.month"

---

### 4. Bank Marketing Dataset
Link:
https://raw.githubusercontent.com/arib168/data-science-projects/master/datasets/bank_marketing.csv

Target column:
y

Code change:
TARGET_COLUMN = "y"

---

### 5. Adult Income Dataset
Link:
https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data

Target column:
income

Code change:
TARGET_COLUMN = "income"

---
## 🧠 Why These Datasets Are Suitable

These datasets:

* Contain **categorical + numerical features**
* Exhibit **distribution variation**
* Are ideal for demonstrating **model aging beyond accuracy**
* Are widely accepted in academia and industry

---

## ✅ Summary Table (Quick View)

| Dataset             | Target Column                | Code Change Needed |
| ------------------- | ---------------------------- | ------------------ |
| Titanic             | `Survived`                   | Yes (1 line)       |
| Heart Disease       | `target`                     | Yes (1 line)       |
| Credit Card Default | `default.payment.next.month` | Yes (1 line)       |
| Bank Marketing      | `y`                          | Yes (1 line)       |
| Adult Income        | `income`                     | Yes (1 line)       |

---

## Dataset Independence

Only one change is required for a new dataset:

TARGET_COLUMN = "<target_column_name>"

All other steps such as missing value handling, categorical encoding,
feature alignment, and confidence-based instability calculation are
handled automatically.

---

## Academic Relevance

This project demonstrates:
- Understanding of real-world ML issues
- Difference between accuracy and reliability
- Practical handling of feature mismatch
- Model monitoring concepts used in industry

---

## Conclusion

The Model Aging Detector shows how machine learning models can degrade silently
even when accuracy remains stable. By focusing on prediction confidence and
stability, the system provides an additional layer of reliability checking
for ML systems.
