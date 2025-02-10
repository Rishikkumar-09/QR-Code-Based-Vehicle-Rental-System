# 🚗 QR Code-Based Vehicle Rental System

## 📌 Overview
This project is a **QR Code-Based Vehicle Rental System** that streamlines the process of renting vehicles by using QR codes. The system consists of two components:

1. **QR Code Generator** → Generates QR codes containing vehicle details.
2. **QR Code Verification & Billing** → Scans QR codes, calculates rental duration, and computes the total amount.

## 🎯 Purpose & Use Cases
This system is ideal for:
- **Car/Bike Rental Services** → Automates the rental process.
- **Self-Checkout Systems** → Enables quick and contactless transactions.
- **Smart Parking Management** → Tracks parking duration and charges accordingly.
- **Shared Mobility Services** → Rideshare, e-scooter, or bicycle rentals.

---

## 🛠️ Features
### ✅ QR Code Generator
- Takes **Vehicle ID** and **Rental Rate per Minute** as input.
- Generates a **QR code** containing vehicle details and timestamp.
- Saves the QR code as a **PNG file**.
- Provides a **user-friendly GUI** using Tkinter.

### ✅ QR Code Verification & Billing
- Scans **QR codes using a webcam** (OpenCV & ZBar).
- Extracts **Vehicle ID, Rental Rate, and Start Time**.
- Computes **total rental duration & charges**.
- Displays rental details in a **GUI window**.

---

## 📂 Project Structure
```
📁 QR-Rental-System
│── 📄 qr_generator.py        # Generates QR codes for rental vehicles
│── 📄 qr_verification.py     # Scans and verifies QR codes for billing
│── 📄 README.md              # Project documentation
│── 📁 assets                 # Stores generated QR codes
│── 📄 requirements.txt       # List of dependencies
```

---

## 🖥️ Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/QR-Rental-System.git
cd QR-Rental-System
```

### 2️⃣ Install Dependencies
Make sure you have **Python 3.9+** installed. Then, run:
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application
#### ➤ Generate QR Code
```bash
python qr_generator.py
```
#### ➤ Scan & Verify QR Code
```bash
python qr_verification.py
```

---

## 🏗️ Technologies Used
- **Python** 🐍
- **qrcode** → Generates QR codes
- **OpenCV** → Scans QR codes via webcam
- **ZBar** → Decodes QR codes
- **Tkinter** → GUI development
- **JSON & Datetime** → Data storage and timestamp handling

---

## 🚀 Future Enhancements
- Add **cloud-based storage** for rental records.
- Implement **mobile app integration** for easier scanning.
- Enable **online payment processing** via UPI/PayPal.
- Develop a **user authentication system** for tracking rentals.

---
##Demo

![Uploading Screenshot 2025-02-08 182738.png…]()
![Screenshot 2024-11-29 211715](https://github.com/user-attachments/assets/714debf6-3ead-4fc6-8502-b3b892f865f3)


## 🤝 Contributing
Feel free to contribute to this project! Open an **issue** or **pull request** on GitHub.

---

## 📜 License
This project is **open-source** and licensed under the MIT License.

---

## 🌟 Show Your Support
If you find this project useful, consider giving it a ⭐ on GitHub!

---

**Developed with ❤️ by [Rishik kumar]**

