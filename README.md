## END TO END ML PROJECT 
# 📘 StudentScore ML  
### 🚀 End-to-End Machine Learning Project — Student Exam Performance Prediction

StudentScore ML is a complete end-to-end Machine Learning project that predicts a student's exam performance based on demographic and academic inputs.  
It includes **data pipelines, preprocessing, model training, evaluation, deployment, and a clean Flask-based UI** — demonstrating practical ML engineering experience.

---

# ⭐ Project Highlights
- 🔥 Fully modular **ML Pipeline** (training → prediction → deployment)  
- 📊 Regression model to predict exam score  
- 🧠 Includes **data ingestion, transformation & model trainer pipelines**  
- 🌐 Flask Web App + Modern UI  
- 🎨 Clean & simple interface (HTML + CSS)  
- 💾 Stores artifacts: `model.pkl`, `preprocessor.pkl`, `data.csv`  
- 📝 Production-like folder structure  
- 🚀 Resume & GitHub portfolio ready  

---

# 📦 Tech Stack

### **Machine Learning**
- Python  
- Scikit-learn  
- NumPy  
- Pandas  

### **Deployment & Backend**
- Flask  
- Custom ML Prediction Pipeline  
- Modular OOP-based code design  

### **Frontend**
- HTML5  
- CSS3  
- Responsive design  

---

# 🧠 ML Pipeline Overview

### **1️⃣ Data Ingestion**
- Reads dataset  
- Splits train/test  
- Saves raw & processed data into `artifacts/`

### **2️⃣ Data Transformation**
- Handles missing values  
- Encodes categorical variables  
- Standard scaling  
- Saves `preprocessor.pkl`

### **3️⃣ Model Training**
- Trains multiple regression models  
- Compares performance (R², RMSE)  
- Saves best model as `model.pkl`

### **4️⃣ Prediction Pipeline**
- Loads preprocessor + model  
- Accepts user input  
- Returns final predicted score  
- Rounds & clamps prediction to 0–100  

---

# 🎨 UI Overview

✔️ Clean white card style  
✔️ Light blue gradient background  
✔️ Dropdowns + numeric inputs  
✔️ Shows prediction clearly  
✔️ Footer: “Made with ❤️ by Aarav”  

---

# 📂 Project Structure

```
StudentScore-ML/
│── app.py
│── requirements.txt
│── README.md
│── artifacts/
│   ├── model.pkl
│   ├── preprocessor.pkl
│   └── data.csv
│── src/
│   ├── pipeline/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   │   └── predict_pipeline.py
│   ├── utils.py
│── templates/
│   ├── index.html
│   ├── home.html
│── notebook/
│   └── EDA_and_Model.ipynb
```

---

# 🚀 How to Run the Project

### **1️⃣ Clone Repository**
```bash
git clone https://github.com/Aarav1777/mlproject/


```

### **2️⃣ Create Virtual Environment**
```bash
python -m venv env
env\Scripts\activate     # Windows
source env/bin/activate  # Mac/Linux
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Start Flask App**
```bash
python app.py
```

Visit the app at:

```
http://127.0.0.1:5000 #-> welcome to home page 

http://127.0.0.1:5000/predictdata
```

---

# 📊 Sample Output
```
Prediction — Score: 96.85
```

---

# 📌 Future Improvements
- Deploy to Render / Railway / HuggingFace Spaces  
- Add SHAP model explainability  
- Add multiple model comparison  
- Add database storage (MongoDB / PostgreSQL)  
- Add authentication for users  

---

# 👨‍💻 Author
**Aarav**  
B.Tech CSE | Machine Learning Enthusiast  
Made with ❤️ during ML learning journey.

---

