# Batch Prediction Pipeline

This project implements a simple batch prediction pipeline for an ML system.

## Project Goal

The system reads input data from a database, runs a trained machine learning model, saves prediction results back into the database, and executes automatically on a schedule.

## Technologies Used

- Python
- SQLite
- Pandas
- Scikit-learn
- Joblib
- Schedule

## Database Tables

### input_data

Stores input features for prediction:

- id
- sepal_length
- sepal_width
- petal_length
- petal_width

### predictions

Stores model prediction results:

- id
- input_id
- prediction
- prediction_timestamp

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt