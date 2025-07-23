# 🎯 COBB Internship Data Dashboard & Customer Segmentation

🚀 **Streamlit Web App** presenting key insights and deliverables from an 8-week Data Analyst Internship at **COBB Italy (India)**.

---

## 🔍 Project Overview

This interactive dashboard visualizes core sales metrics and performs customer segmentation using machine learning (K-Means Clustering). Built with **Python** and **Streamlit**, the tool provides:

- 📈 Dynamic sales analysis (bar charts, pie charts, heatmaps)
- 👥 Customer segmentation based on spending behavior
- 🛠️ Automated data preprocessing pipeline for real-time insights

---

## 🌐 Live Application

👉 **[Launch the Dashboard](https://cobb-intern-dashboard-krgftnbrk97cz6whvlqxen.streamlit.app/)**  
Hosted on Streamlit Cloud — no setup needed. Just open and explore.

---

## 🧠 Tech Stack

- **Language:** Python  
- **Libraries:** Pandas, NumPy, Plotly, Scikit-learn  
- **Framework:** Streamlit  
- **Deployment:** Streamlit Cloud  
- **Clustering Algorithm:** K-Means

---

## ✨ Key Features

- ✅ Sidebar filters for year-wise and customer segment selection
- 📊 Real-time charts (interactive & responsive)
- 👥 Customer clustering based on:
  - Age  
  - Annual Income  
  - Spending Score  
- ⚙️ Backend pipeline for preprocessing CSV inputs

---

## 🗂️ Repository Structure
📁 cobb-intern-dashboard/
├── streamlit_dashboard.py       # 🚀 Main Streamlit app file
├── sample_customer_data.csv     # 🧪 Sample data auto-loaded in the app
├── requirements.txt             # 📦 All Python dependencies
├── README.md                    # 📘 Project overview and usage guide

## 📌 How to Run Locally

```bash
pip install -r requirements.txt
streamlit run streamlit_dashboard.py

