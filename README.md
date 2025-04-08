# 🧠 Diabetes Prediction using Machine Learning and Neural Networks

This project demonstrates how various machine learning models and neural networks can be used to predict the likelihood of diabetes based on patient data. The dataset used is the **Pima Indians Diabetes Database**, which contains diagnostic measurements for female patients.

---

## 📁 Project Structure

- `Logistic Regression.ipynb`: Implementation of logistic regression with performance evaluation.
- `Decision Trees.ipynb`: Decision tree model with visualization and confusion matrix.
- `Confusion Matrices.ipynb`: Comparison of confusion matrices for multiple models.
- `Neural Networks.ipynb`: A fully connected feedforward neural network using Keras.
- `huffman.py`: Implementation of Huffman coding for compression.
- `aritmeticke.py`: Arithmetic encoding and decoding algorithm for lossless data compression.

---

## 📊 Dataset

The dataset (`diabetes.csv`) contains the following features:

- **Pregnancies**
- **Glucose**
- **BloodPressure**
- **SkinThickness**
- **Insulin**
- **BMI** (Body Mass Index)
- **DiabetesPedigreeFunction**
- **Age**
- **Outcome** (target: 1 = diabetic, 0 = non-diabetic)

---

## ✅ Models Used

### 1. Logistic Regression
- Simple baseline for binary classification.
- Evaluated using accuracy, precision, recall, F1-score, and confusion matrix.

### 2. Decision Tree Classifier
- Tree-based model with `max_depth` tuning.
- Includes a full decision tree visualization.

### 3. k-Nearest Neighbors (k-NN)
- Classifier using Euclidean distance.
- `n_neighbors = 5`.

### 4. Support Vector Machine (SVM)
- Linear kernel used for classification.
- Confusion matrix and classification report included.

### 5. Feedforward Neural Network (Keras)
- Input layer: 12 neurons
- Hidden layer: 8 neurons
- Output layer: 1 neuron (sigmoid)
- Optimizer: Adam
- Loss: Binary Crossentropy
- Metrics: Accuracy
- Visualized training history (loss & accuracy over epochs)

---

## 📈 Evaluation Metrics

Each model is evaluated using:
- **Accuracy**
- **Confusion Matrix**
- **Precision / Recall / F1-score**
- **ROC Curves (optional in extended analysis)**

Visualizations are created using `matplotlib` and `seaborn`.
