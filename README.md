# 🎨 simple-image2ascii - Convert Images & Videos to ASCII Art

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![NumPy](https://img.shields.io/badge/NumPy-Supported-orange)
![OpenCV](https://img.shields.io/badge/OpenCV-Supported-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

`simple-image2ascii` is a Python library that transforms images and videos into ASCII art using NumPy and OpenCV. 

---

## 🚀 Installation

Install the library using `pip`:

```bash
pip install simple-image2ascii
```

---

## 🔧 Usage

### 📷 Convert Image to ASCII

```python
import cv2
import simple_image2ascii

# Load an image
image = cv2.imread("example.jpg")

# Create an ASCIIEngine instance
engine = simple_image2ascii.ASCIIEngine()

# Convert to ASCII
ascii_art = engine.get_ascii(image)

# Print the result
print(ascii_art)
```

### 🎥 Convert Video to ASCII (Using OpenCV)

```python
import cv2
import simple_image2ascii

cap = cv2.VideoCapture("video.mp4")
engine = simple_image2ascii.ASCIIEngine()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    ascii_frame = engine.get_ascii(frame)
    print(ascii_frame)

cap.release()
```

---

## 🛠 Features

✅ **Grayscale conversion**
✅ **Adaptive ASCII mapping**
✅ **8×8 pixel block processing**
✅ **Supports image resizing**
✅ **Works with both images and videos**

---

## 📦 Dependencies

- `numpy`
- `opencv-python`

To install dependencies manually:

```bash
pip install numpy opencv-python
```

---

## 📜 License

This project is licensed under the **MIT License**.

---

## ✉ Contact
🐙 **GitHub**: [AlekseyScorpi](https://github.com/AlekseyScorpi)

