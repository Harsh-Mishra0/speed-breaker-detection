# 🚧 Speed Breaker Detection using Deep Learning

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/TensorFlow-2.x-orange?logo=tensorflow&logoColor=white"/>
  <img src="https://img.shields.io/badge/MobileNetV2-Transfer%20Learning-green"/>
  <img src="https://img.shields.io/badge/Streamlit-Web%20App-red?logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/License-MIT-lightgrey"/>
</p>

A Computer Vision project that detects **speed breakers on roads** from images using **Deep Learning** and **Transfer Learning** with MobileNetV2. The system includes a Streamlit web app for real-time predictions.

---

## 📌 Table of Contents

- [Project Overview](#-project-overview)
- [Demo](#-demo)
- [Model Architecture](#-model-architecture)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [Model Training](#-model-training)
- [Results](#-results)
- [Future Improvements](#-future-improvements)
- [Author](#-author)

---

## 📖 Project Overview

This project classifies road images into two categories:
- ✅ **Speed Breaker Detected**
- 🚗 **Normal Road**

It leverages **MobileNetV2**, a lightweight convolutional neural network pretrained on ImageNet, fine-tuned on a custom road image dataset. The trained model is served through a **Streamlit** web application where users can upload any road image and get an instant prediction.

---

## 🎥 Demo

To run the web app locally:

```bash
streamlit run demo/app.py
```

Upload a road image → Get prediction instantly.

---

## 🧠 Model Architecture

```
Road Image
    ↓
Image Preprocessing (Resize, Normalize)
    ↓
MobileNetV2 (Pretrained on ImageNet — Feature Extractor)
    ↓
Global Average Pooling
    ↓
Dense Layer (ReLU)
    ↓
Output Layer (Sigmoid)
    ↓
Binary Classification → Speed Breaker / Normal Road
```

---

## 🛠 Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.10 | Core programming language |
| TensorFlow / Keras | Model building & training |
| MobileNetV2 | Transfer learning backbone |
| OpenCV | Image preprocessing |
| NumPy | Numerical operations |
| Matplotlib | Training visualization |
| Streamlit | Web application interface |

---

## 📂 Project Structure

```
speed-breaker-detection/
│
├── notebooks/
│   └── training.ipynb        # Model training notebook (Google Colab)
│
├── models/
│   └── speedbreaker_model.h5 # Saved trained model
│
├── src/
│   └── predict.py            # Prediction script
│
├── demo/
│   └── app.py                # Streamlit web application
│
├── requirements.txt          # Python dependencies
└── README.md
```

---

## 🚀 Installation

**1. Clone the repository**

```bash
git clone https://github.com/Harsh-Mishra0/speed-breaker-detection.git
cd speed-breaker-detection
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

---

## ▶ Usage

### Run the Streamlit Web App

```bash
streamlit run demo/app.py
```

Open your browser, upload a road image, and the model will predict whether a speed breaker is present.

### Run Prediction via Script

```bash
python src/predict.py --image path/to/your/image.jpg
```

---

## 📊 Model Training

The model was trained using **Google Colab** with GPU acceleration. Open the training notebook to retrain:

```
notebooks/training.ipynb
```

**Training Pipeline:**
1. Load and label road image dataset
2. Preprocess images (resize to 224×224, normalize pixel values)
3. Load MobileNetV2 with frozen base layers
4. Add custom classification head
5. Train for multiple epochs with Adam optimizer
6. Evaluate and save model as `.h5`

---

## 📈 Results

| Metric | Value |
|--------|-------|
| Model | MobileNetV2 (Transfer Learning) |
| Task | Binary Image Classification |
| Input Size | 224 × 224 × 3 |
| Output | Speed Breaker / Normal Road |

---

## 🔭 Future Improvements

- [ ] Real-time detection using OpenCV and live camera feed
- [ ] Video-based road analysis (frame-by-frame)
- [ ] YOLO-based object detection for improved localization
- [ ] Cloud deployment on AWS / GCP / Hugging Face Spaces
- [ ] Mobile-friendly model optimization (TFLite)

---

## 👨‍💻 Author

**Harsh Mishra**  
AI / ML Engineer | B.Tech – Artificial Intelligence & Machine Learning

- GitHub: [@Harsh-Mishra0](https://github.com/Harsh-Mishra0)

---

<p align="center">⭐ If you found this project useful, consider giving it a star!</p>
