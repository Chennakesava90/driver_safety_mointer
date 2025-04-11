# 🚗 Driver Safety Monitoring System

A real-time AI-powered driver monitoring system that detects driver drowsiness (eye closure) and phone usage while driving. Designed to enhance road safety by alerting the driver during unsafe behavior.

---

## 📸 Features

- 🔍 Detects:
  - **Closed eyes** (drowsiness)
  - **Phone usage while driving**
- 📢 Plays alert sound when violations are detected
- 🧠 Uses pre-trained YOLOv8 model
- 🎥 Supports:
  - **Live webcam detection**
  - **Image upload**
  - **Video upload**
- 📝 Stores violation logs for review

---

## 📷 Sample Output

### ✅ Safe Driving
![Safe Driving](sample_outputs/safe_driving.png)

### 😴 Drowsiness Detected
![Drowsiness Detected](sample_outputs/drowsiness_detected.png)

### 📱 Phone Usage Detected
![Phone Usage](sample_outputs/phone_usage_detected.png)

### ❌ Both Violations
![Both Violations](sample_outputs/both_violations.png)

![Phone Usage Detected](sample_outputs/phone_usage_alert.png)

> *(Note: Place your sample images in a folder named `sample_outputs/` in the project directory.)*

---

## 🛠️ Technologies Used

- 🐍 Python
- 📦 OpenCV
- 🔊 Pygame (for audio alert)
- 🧠 YOLOv8 (Ultralytics)
- 📁 PyTorch

---

## 📦 Installation

```bash
git clone https://github.com/Chennakesava90/driver_safety_mointer.git
cd driver_safety_mointer
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🚀 Usage

### ▶️ Real-Time Webcam Detection
```bash
python driver_mointer.py --source webcam
```

### 🖼️ Image Detection
```bash
python driver_mointer.py --source image --path path_to_image.jpg
```

### 🎞️ Video Detection
```bash
python driver_mointer.py --source video --path path_to_video.mp4
```

---

## 📁 Project Structure

```
driver_safety_mointer/
│
├── driver_mointer.py              # Main detection script
├── yolov8n.pt                     # YOLOv8 model weights
├── requirements.txt              # Required Python packages
├── alert.mp3                     # Alert sound
├── phone_log.txt                 # Log file for phone usage
├── logs/
│   └── violations_log.txt        # Drowsiness & phone usage log
├── sample_outputs/               # Folder for sample output images
└── README.md
```

---

## 📌 Future Improvements

- Add face recognition for driver identity
- Implement seatbelt detection
- Real-time dashboard for fleet monitoring

---

## 🙋‍♂️ Author

**Chennakesava**  
🔗 GitHub: [@Chennakesava90](https://github.com/Chennakesava90)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

