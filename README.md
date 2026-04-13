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
from doc_classifier import Classifier

# Initialize the model
model = Classifier()

# Sample text
text = """
Deep learning is widely used in natural language processing,
especially for text classification and semantic understanding.
"""

# Predict category
prediction = model.predict(text)

print("Predicted category:", prediction)
```
