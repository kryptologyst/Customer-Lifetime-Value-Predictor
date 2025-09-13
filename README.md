# Customer Lifetime Value Predictor

This project builds a web application to predict Customer Lifetime Value (CLV) using a linear regression model. The application is built with Flask and allows users to get CLV predictions by inputting customer data.

## Project Structure

```
. 
├── app.py # Flask application
├── 0048.py # Script to train and save the model
├── customers.csv # Dataset used for training
├── clv_model.pkl # Saved machine learning model
├── requirements.txt # Project dependencies
├── templates
│   └── index.html # Web interface
└── .gitignore # Files to be ignored by Git
```

## Setup and Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd 0048_Customer_lifetime_value_predictor
    ```

2.  **Create a virtual environment and activate it:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## How to Run

1.  **Train the model (if not already done):**

    Run the `0048.py` script to train the model and create the `clv_model.pkl` file.

    ```bash
    python3 0048.py
    ```

2.  **Run the Flask application:**

    ```bash
    python3 app.py
    ```

3.  **Open your browser and navigate to:**

    ```
    http://127.0.0.1:5000
    ```

## Usage

Enter the following customer details into the web form:

*   **Recency:** Days since the last purchase.
*   **Frequency:** Total number of purchases made.
*   **Average Order Value:** The average amount spent per order.

Click the **Predict** button to see the estimated Customer Lifetime Value.
# Customer-Lifetime-Value-Predictor
