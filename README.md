#  AI Cybersecurity System (Phishing & Deepfake Detection)

##  Overview
This project presents an AI-powered cybersecurity system designed to detect phishing attacks and address emerging threats caused by Generative AI.

With the rapid advancement of AI, cybercriminals are now able to generate highly convincing phishing messages and deepfake content. This system provides a practical and scalable solution using machine learning and computer vision techniques to detect such threats.

---

##  Problem Statement
The democratization of Generative AI tools has significantly lowered the barrier for cybercriminals to launch sophisticated phishing campaigns and deepfake attacks. Traditional security systems are no longer sufficient.

This project aims to build an intelligent system that can:
- Detect phishing messages using NLP and ML
- Provide a modular framework for deepfake detection

---

##  Key Features

### 🔹 1. Phishing Detection (Core Module)
- NLP-based text classification
- TF-IDF feature extraction with n-grams
- Multiple ML models:
  - Logistic Regression
  - Naive Bayes
- Automatic model selection
- Hybrid detection system:
  - Machine Learning + Rule-based keywords
- Real-time prediction system

---

### 🔹 2. Deepfake Detection (Extension Module)
- Lightweight computer vision-based detection
- Uses:
  - Blur detection (Laplacian variance)
  - Noise estimation
  - Edge detection
- Modular design for future deep learning integration

---

##  Technologies Used

- **Programming Language:** Python  
- **Libraries:**
  - Pandas (data handling)
  - NumPy (numerical operations)
  - Scikit-learn (machine learning)
  - OpenCV (image processing)
- **Techniques:**
  - Natural Language Processing (NLP)
  - TF-IDF Vectorization
  - Logistic Regression
  - Naive Bayes
  - Hybrid ML + Rule-based detection

---

##  Project Structure
cyber_ai_project/
│
├── data/
│ └── emails.csv
│
├── src/
│ ├── preprocess.py # Data cleaning
│ ├── feature.py # TF-IDF
│ ├── model.py # ML models
│ ├── train.py # Training pipeline
│ ├── evaluate.py # Evaluation
│ ├── predict.py # Prediction system
│ ├── deepfake.py # Deepfake detection
│ └── test_system.py # Large test suite
│
├── models/
│ ├── model.pkl
│ └── vectorizer.pkl
│
├── main.py # Main execution file
├── test_deepfake.py # Optional image testing
├── requirements.txt
└── README.md

---

##  Machine Learning Pipeline

1. Data Loading  
2. Data Cleaning & Preprocessing  
3. Feature Extraction (TF-IDF)  
4. Train-Test Split  
5. Model Training (Multiple Models)  
6. Model Selection (Best Accuracy)  
7. Evaluation (Metrics + Confusion Matrix)  
8. Prediction (Real-time input)

---

##  Results

| Metric | Value |
|------|------|
| Dataset Accuracy | ~96% |
| Real-world Test Accuracy | ~88% |
| Spam Recall Improved | Yes (Hybrid approach) |

---

##  Testing & Validation

- Implemented **80+ real-world test cases**
- Evaluates:
  - Phishing detection accuracy
  - Model generalization
  - Real-world robustness

Run tests:
```bash
python -m src.test_system
How to Run
1. Install Dependencies
pip install -r requirements.txt
2. Run Main System
python main.py
3. Run Test Suite
python -m src.test_system
4. Deepfake Test (Optional)
python test_deepfake.py

Key Innovations
Hybrid detection system (ML + rule-based)
Real-world validation with large test suite
Modular and scalable architecture
Practical cybersecurity-focused solution

Future Scope
Deepfake detection using CNN and deep learning
Real-time deployment (API/Web app)
Integration with email systems
Multi-modal AI security system (text + image + video)
