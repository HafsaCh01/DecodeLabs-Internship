# DecodeLabs Internship 
This repository contains the projects completed during my **DecodeLabs Internship**. Each project focuses on building fundamental programming and Artificial Intelligence (AI) concepts using Python.

---

#  Projects

## Project 1 – Rule-Based AI Chatbot 
### Overview
A simple rule-based chatbot built with Python that responds to predefined user inputs using conditional (`if-else`) statements. The chatbot can greet users, respond to common conversational phrases, and exit gracefully.

### Features
- Responds to greetings
- Handles "How are you?" questions
- Responds to thank-you messages
- Recognizes exit commands
- Provides default responses for unknown inputs
- Runs continuously until the user exits

### Technologies Used
- Python 3

### File
```
task1.py
```

### How to Run
```bash
python task1.py
```

### Sample Output
```
You: hello
Bot: Hello there! How can I help you today?
You: how are you
Bot: I'm doing great! Thanks for asking.
You: thanks
Bot: You're welcome!
You: bye
Bot: Goodbye! Have a great day.
```

### Learning Outcomes
- Python basics
- Conditional statements
- Loops
- Lists
- String handling
- Rule-based AI concepts

---

# Project 2 – Data Classification Using AI 
### Overview
A basic machine learning project that classifies flower species using the famous **Iris Dataset**. The project demonstrates how to load a dataset, split it into training and testing sets, train a classification model, and evaluate its performance.

### Features
- Loads the Iris dataset
- Splits data into training and testing sets
- Trains a Decision Tree Classifier
- Evaluates model accuracy
- Predicts the class of a new sample

### Technologies Used
- Python 3
- Scikit-learn

### File
```
task2.py
```

### Install Required Package
```bash
pip install scikit-learn
```

### How to Run
```bash
python task2.py
```

### Sample Output
```
Dataset Loaded Successfully
Number of Samples: 150
Features:
['sepal length (cm)',
 'sepal width (cm)',
 'petal length (cm)',
 'petal width (cm)']
Target Classes:
['setosa' 'versicolor' 'virginica']
Model Accuracy: 100.0 %
Sample Prediction:
Predicted Flower: setosa
```

### Learning Outcomes
- Data loading
- Data preprocessing
- Train-test splitting
- Supervised learning
- Decision Tree Classification
- Model evaluation using accuracy score

---

# Project 3 – AI Recommendation Logic
### Overview
A simple recommendation system that suggests clothing items based on user preferences. It takes user input (style, color, category, and budget) and matches it against a catalog of items using a weighted similarity-scoring algorithm, then displays the top-ranked recommendations.

### Features
- Takes user input (style, color, category, budget)
- Matches preferences against a catalog using logic/similarity scoring
- Ranks results by match score, with price as a tiebreaker
- Displays recommended items with full details
- Supports repeated searches in a single session

### Technologies Used
- Python 3

### File
```
task3.py
```

### How to Run
```bash
python task3.py
```

### Sample Output
```
Preferred style (casual/formal): casual
Preferred color (or press Enter to skip): blue
Category interested in (top/bottom/outerwear/footwear, or Enter to skip):
Max budget (or press Enter to skip): 50

=============================================
       YOUR RECOMMENDED ITEMS
=============================================

1. Ripped Jeans
   Category : bottom
   Style    : casual
   Color    : blue
   Price    : $40
   Match Score : 6

2. Denim Jacket
   Category : outerwear
   Style    : casual
   Color    : blue
   Price    : $45
   Match Score : 6
```

### Learning Outcomes
- Logic building
- Pattern matching / similarity scoring
- Recommendation system concepts
- Function-based program design

---

#  Repository Structure
```
DecodeLabs-Internship/
│
├── README.md
├── requirements.txt
├── task1.py
├── task2.py
└── task3.py
```

---

#  Requirements
Install the required Python package:
```bash
pip install scikit-learn
```

Or install using the requirements file:
```bash
pip install -r requirements.txt
```

**requirements.txt**
```
scikit-learn
```

---

# Running the Projects
### Project 1
```bash
python task1.py
```

### Project 2
```bash
python task2.py
```

### Project 3
```bash
python task3.py
```

---

#  Skills Learned
- Python Programming
- Problem Solving
- Control Flow
- Data Handling
- Machine Learning Basics
- Supervised Learning
- Decision Tree Classification
- Model Training and Evaluation
- Logic Building & Pattern Matching
- Recommendation System Concepts
- Git & GitHub

---

#  Author
**Hafsa**
GitHub: https://github.com/HafsaCh01

---

##  About
These projects were completed as part of the **DecodeLabs Internship** to strengthen my understanding of Python programming and introductory Artificial Intelligence concepts.
