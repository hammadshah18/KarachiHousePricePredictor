[![askpython.com/python-mod...](https://images.openai.com/thumbnails/url/pUc3B3icu1mSUVJSUGylr5-al1xUWVCSmqJbkpRnoJdeXJJYkpmsl5yfq5-Zm5ieWmxfaAuUsXL0S7F0Tw7JLqmM8IwszqgoiwjN9SzMToqPSPUJzijLcM7ID8wJNsk3qMgJKAl1T8n0tSxKT0zxLkt29HYNN_ELDVQrBgBi-itI)](https://www.askpython.com/python-modules/machine-learning-model-streamlit-house-price-prediction-gui?utm_source=chatgpt.com)



---

# Karachi House Price Predictor

![Karachi House Price Predictor](https://github.com/hammadshah18/KarachiHousePricePredictor/raw/main/bg.jpg)

## 📌 Overview

The **Karachi House Price Predictor** is an interactive web application built using Python, Streamlit, and scikit-learn. It leverages machine learning to predict real estate prices in Karachi based on various input features such as location, number of bedrooms, bathrooms, and more.

🔗 Access the live app: [Karachi House Price Predictor](https://karachihousepricepredictor-5suw5z6fhsc5ibwtdxgj4q.streamlit.app/)

---

## 🛠️ Technologies Used

* **Frontend**: Streamlit
* **Backend**: Python 3.10.11
* **Machine Learning**: scikit-learn (v1.5.1)
* **Data Handling**: pandas, numpy
* **Model Serialization**: joblib

---

## 📁 Project Structure

```
KarachiHousePricePredictor/
│
├── app.py                 # Main Streamlit application
├── model/                 # Directory containing the trained model
│   └── house_price_model.pkl
├── KarachiHouseCleanData.csv  # Cleaned dataset
├── requirements.txt       # Python dependencies
└── .gitignore             # Git ignore file
```

---

## 📦 Installation

Clone this repository and set up a virtual environment:

```bash
git clone https://github.com/hammadshah18/KarachiHousePricePredictor.git
cd KarachiHousePricePredictor
python -m venv venv310
.\venv310\Scripts\Activate.ps1
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 Run the Application Locally

To start the Streamlit app:

```bash
streamlit run app.py
```

Then, open your browser and navigate to [http://localhost:8501](http://localhost:8501) to interact with the application.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📢 Acknowledgments

* **Streamlit**: For providing an intuitive platform to build and deploy web applications.
* **scikit-learn**: For offering robust machine learning tools.
* **pandas & numpy**: For efficient data manipulation and analysis.

---


