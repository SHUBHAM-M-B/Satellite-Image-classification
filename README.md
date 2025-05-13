

---

# 🌍 Satellite Image Classification using Deep Learning

A web-based deep learning application to classify satellite images into 10 land use and land cover categories using a pre-trained VGG16 model. The project offers:

* 📷 Image upload & prediction via **Streamlit**
* 🧠 Training & evaluation scripts
* 🐳 Docker-ready setup
* ⚙️ Optional Flask backend

---

## 🧾 Table of Contents

* [Project Structure](#file-folder-structure)
* [Features](#features)
* [Installation](#installation)
* [Usage](#usage)

  * [Streamlit App](#streamlit-app)
  * [Model Training](#training-the-model)
  * [Model Evaluation](#evaluating-the-model)
  * [Docker Setup](#docker-setup)
* [Model Details](#model-architecture)
* [Requirements](#requirements)
* [Acknowledgements](#acknowledgements)
* [Author](#author)

---

## 📁 File & Folder Structure

```
Satellite_Image_Classifier/
├── .devcontainer/              # Dev container configs
│   └── devcontainer.json
├── .idea/                      # IDE configs (PyCharm)
│   └── ...
├── models/
│   ├── model.py                # VGG16 model definition
│   ├── trained_model.h5        # Trained model
│   └── trained_model.weights.h5
├── scripts/
│   ├── __init__.py
│   ├── evaluate.py             # Evaluate model script
│   └── train.py                # Train model script
├── utils/
│   ├── __init__.py
│   └── data_loader.py          # Data loading and preprocessing
├── __pycache__/                # Cached bytecode
├── app.py                      # Streamlit app
├── main.py                     # Flask entrypoint
├── Dockerfile                  # Docker setup
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

---

## 🚀 Features

* Upload and classify satellite images via Streamlit UI.
* Train your model from scratch with VGG16 as base.
* Evaluate your model on a test set.
* Easily portable using Docker.
* Modular architecture for maintainability.

---

## ⚙️ Installation

### 📦 Clone the Repository

```bash
git clone https://github.com/yourusername/satellite-image-classifier.git
cd satellite-image-classifier
```

### 🧪 Create Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 📚 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 💻 Usage

### ▶️ Streamlit App

Run the UI to classify satellite images:

```bash
streamlit run app.py
```

You can upload one or multiple `.jpg`, `.jpeg`, or `.png` files and get predictions in your browser.

---

### 🏋️ Training the Model

Edit dataset paths in `scripts/train.py` if needed, then run:

```bash
python scripts/train.py
```

The trained model will be saved as `models/trained_model.h5`.

---

### 📊 Evaluating the Model

Update paths in `scripts/evaluate.py` and run:

```bash
python scripts/evaluate.py
```

It will print loss and accuracy on the test set.

---

### 🐳 Docker Setup (Optional)

Build and run the Docker container:

```bash
docker build -t satellite-classifier .
docker run -p 8501:8501 satellite-classifier
```

Open [http://localhost:8501](http://localhost:8501) to access the app.

---

## 🧠 Model Architecture

* **Base Model**: VGG16 (pretrained on ImageNet, frozen)
* **Input Shape**: (64, 64, 3)
* **Top Layers**:

  * Flatten
  * Dense(512, ReLU)
  * Dropout(0.5)
  * Dense(10, Softmax)

### 📚 Classes

* AnnualCrop
* Forest
* HerbaceousVegetation
* Highway
* Industrial
* Pasture
* PermanentCrop
* Residential
* River
* SeaLake

---

## 📌 Requirements

Installed via `requirements.txt`:

```txt
tensorflow
streamlit
numpy
pillow
```

---

## 📸 Dataset

Assumed directory structure (`data/2750`) compatible with Keras `flow_from_directory`. You may use datasets like [EuroSAT](https://github.com/phelber/eurosat) for classification tasks.

---

## 🙏 Acknowledgements

* [EuroSAT Dataset](https://github.com/phelber/eurosat)
* Keras Applications (VGG16)

---

## 👨‍💻 Author

Developed by Shubham M Bolashetty,Yoganarasimha B,Suhas Shetty
📧 Contact: shubhammb1810@gmail.com
🛠 Contributions and issues welcome!

---
