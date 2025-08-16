🌾 Grain Gain
=============

Grain Gain is a major project designed to revolutionize food and nutrition management through the power of AI, ML, and real-time detection.  
The project integrates object detection, recommender systems, and a multi-model approach to help users make healthier dietary decisions.

---

## ✨ Features

- 🔍 **Real-Time Object Detection** – Identify grains and food items using YOLOv9.  
- 📊 **Diet Recommendation System** – Suggests food options (Veg ↔ Veg, NonVeg ↔ Veg, Veg ↔ Non-Veg) based on nutritional macros.  
- 📈 **Multi-Model Architecture** – Combines object detection with recommender systems for accurate results.  
- ⚡ **Flask Backend + MySQL Database** – Smooth API integration and data storage.  
- 🌐 **Modern Frontend** – Built with HTML, CSS, JavaScript for responsiveness.

---

## 🛠️ Tech Stack

**Frontend:**
- HTML  
- CSS  
- JavaScript  

**Backend & APIs:**
- Flask (Python)  
- REST API  

**Database:**
- MySQL  

**Machine Learning & AI:**
- YOLOv9 (Object Detection)  
- Custom Recommender Systems (Macro-based)  

---

## 🚀 Getting Started

**Prerequisites:**
- Python 3.9+  
- Flask  
- MySQL  
- YOLOv9 (Object Detection)  
- Custom Recommender Systems (Macro-based)  
- HTML, CSS, JavaScript for frontend development  
- Nvidia CUDA (For GPU acceleration)

**Installation:**

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yuvrajghag5/Grain-Gain.git
    cd Grain-Gain
    ```

2. **Create and activate virtual environment:**
    ```sh
    python -m venv venv
    # On Mac/Linux
    source venv/bin/activate
    # On Windows
    venv\Scripts\activate
    ```

3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the Flask app:**
    ```sh
    python app.py
    ```

---

## 📂 Project Structure

```
grain-gain/
│── frontend/         # HTML, CSS, JS files
│── backend/          # Flask API & routes
│── models/           # YOLOv9 + recommender models
│── database/         # MySQL schema & queries
│── requirements.txt  # Python dependencies
│── app.py            # Flask main entry point
│── README.txt        # Project documentation
```

---

## 📸 Screenshots (Optional)

![Food Detection](phal.png)

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Check out the [issues page](https://github.com/yuvrajghag5/Grain-Gain/issues)
