# 📊 Student Performance Prediction

A machine learning web application that predicts a **student's performance score (0–100)** based on key academic and lifestyle factors.

## 🚀 Live Demo
[Deployed App](http://perfomanceprediction-env.eba-tukjiw3p.ap-south-1.elasticbeanstalk.com/)

---

## 📌 About the Project

Academic performance depends on multiple factors beyond just attending classes. This project analyzes key lifestyle and study habits to predict a student's expected performance score, helping identify areas of improvement.

---

## 🧠 Model

- **Algorithm:** Ridge Regression
- **Framework:** Scikit-learn
- **Evaluation Metrics:** R² Score, RMSE

---

## 📥 Input Features

| Feature | Description |
|---|---|
| Study Hours | Number of hours studied per day |
| Previous Score | Score obtained in previous exam |
| Sleep Hours | Average hours of sleep per day |
| Sample Questions Practiced | Number of practice questions attempted |
| Extracurricular Activities | Whether student participates (Yes/No) |

## 📤 Output

Predicted **performance score** between 0 and 100.

---

## 🛠️ Tech Stack

- **Language:** Python
- **Framework:** Flask
- **Libraries:** NumPy, Pandas, Scikit-learn, Matplotlib
- **Deployment:** AWS Elastic Beanstalk

---

## ⚙️ How to Run Locally

```bash
# Clone the repository
git clone https://github.com/preet-99/Perfomance_Prediction.git
cd Perfomance_Prediction

# Install dependencies
pip install -r requirements.txt

# Run the app
python application.py
```

Open `http://10.224.209.45:5000` in your browser.

---

## 📁 Project Structure

```
Perfomance_Prediction/
├── app.py
├── model/
│   └── ridge_model.pkl
├── templates/
│   └── index.html
├── requirements.txt
└── README.md
```

---

## 👤 Author

**Preet** — [GitHub](https://github.com/preet-99) | [LinkedIn](https://www.linkedin.com/in/preet-vishwakarma-b775a7317)