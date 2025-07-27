# 📧 Email Spam Classifier

This is a simple web application that can predict whether an email is **Spam or Not Spam** using machine learning and natural language processing (NLP). I built this as a mini project using Flask for the web interface and trained the model using a dataset of labeled email messages.

---

## 🚀 What This Project Does

- Takes input from the user (email content)
- Preprocesses the text using NLP techniques
- Uses a trained ML model to classify it as **Spam** or **Not Spam**
- Displays the result on the webpage with a smooth UI

---

## 🛠️ Tech Stack

- **Python**
- **Flask** (Web Framework)
- **Scikit-learn** (Model and vectorizer)
- **TF-IDF** (Text vectorization)
- **HTML/CSS** (Frontend)
- **OpenCV** (for background video display)

---

## 📁 Folder Structure

Email_Spam_Classifier/
├── app.py # Main Flask application
├── model.pkl # Trained ML model
├── vectorizer.pkl # TF-IDF vectorizer
├── data.csv # Dataset used for training
├── Trained.ipynb # Jupyter notebook (training process)
├── requirements.txt # Project dependencies
├── templates/
│ └── index.html # Frontend HTML
├── static/
│ └── video.mp3 # Background video



---

## 📦 Setup Instructions

1. **Clone the repo**  
   ```bash
   git clone https://github.com/Codeninja026/Email_Spam_Classifier.git
   cd Email_Spam_Classifier
2. **(Optional) Create a virtual environment**
   python -m venv venv
   venv\Scripts\activate

3. **Install required packages**
   pip install -r requirements.txt

4. ** Run the Flask app**
   python app.py

-- 
## Features 
Features
   -97% accurate spam prediction
   -Clean and responsive UI
   -Real-time feedback
   -Background video for a better user experience
