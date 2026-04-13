# doc-classifier

> A machine learning package for classification of scientific documents into academic fields. It helps researchers, students, and organizations efficiently organize and analyze large volumes of scientific text.

[![PyPI version](https://img.shields.io/pypi/v/doc-classifier.svg)](https://pypi.org/project/doc-classifier/)

---

## ✨ Features

- Supports **Arabic, French, English**
- Trained on **117 976 documents**
- Evaluated on **50 558 documents**
- Achieves **~87% accuracy**

---

## 🏷️ Supported Labels

- Sciences & Technology  
- Physics & Chemistry  
- Mathematics & Computer Science  
- Natural & Life Sciences  
- Earth & Universe Sciences  
- Economics, Marketing & Management  
- Law & Political Sciences  
- Literature & Foreign Languages  
- Social & Human Sciences  
- Sports & Physical Activities  
- Health Sciences  
- Architecture & Urban Planning  

---

## 📦 Installation

Install the package from PyPI:

```bash
pip install doc-classifier
```

Usage Example:

```python
from doc_classifier import classify

# Sample text
text = "This article analyzes the basic classification of machine learning, including supervised learning, unsupervised learning, and reinforcement learning. It combines analysis on common algorithms in machine learning, such as decision tree algorithm, random forest algorithm, artificial neural network algorithm, SVM algorithm, Boosting and Bagging algorithm, BP algorithm. Through the development of theoretical systems, further improvement of autonomous learning capabilities, the integration of multiple digital technologies, and the promotion of personalized custom services, the purpose is to improve people's awareness of machine learning and accelerate the speed of popularization of machine learning."

# Predict category
label = classify(summary)

print("Predicted category:", label)
```
