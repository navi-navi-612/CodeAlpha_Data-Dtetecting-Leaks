# CodeAlpha_Data-Dtetecting-Leaks

 A secure cloud-based system that detects and prevents SQL injection attacks, encrypts user data, and avoids redundancy using Firebase.

---

## 🛠️ Features

This project is a secure web application designed to:

🛡️ Detect and block SQL injection attacks
   – It scans user input for malicious SQL patterns to prevent data leaks.
🔒 Encrypt sensitive user data using AES-256
   – Ensures confidential data is stored securely in the database.
🔁 Prevent data redundancy
   – Checks for duplicate entries and stores only unique, verified data.
🔑 Use capability codes for controlled SQL access
   – Only authorized SQL operations are allowed using special codes.
👨‍💼 Provide a secure admin dashboard
   – Admins can log in to monitor and manage submissions safely.
☁️ Store data in Firebase Realtime Database
   – Ensures fast, cloud-based, and real-time data storage.
- 🌐 Built using Flask, Python, HTML, CSS

---

## 📂 Project Structure
project-folder/ ├── app.py   # Flask app routes ├── utils.py   # Firebase operations ├── capability_code.py  # Capability access control logic ├── injection_checker.py  # SQL injection detection ├── encryption.py   # AES-256 encryption ├── templates/ │ └── index.html   # Frontend UI (user side) ├── static/ │  └── style.css   # CSS styling ├── firebase_config.json   # 🔒 Firebase credentials (DO NOT UPLOAD) ├── .env   # 🔒 Secret keys (DO NOT UPLOAD) ├── .env.example  # ✅ Sample .env structure ├── .gitignore   # Hides sensitive files from Git ├── README.md   # This file └── requirements.txt   # Python dependencies

---

## 🚫 Do NOT Upload These Files to Anywhere

| File                   | Reason                            |
|------------------------|-----------------------------------|
| .env                 | Contains secret keys/passwords    |
| firebase_config.json | Firebase admin credentials        |

*✔️ Add them to .gitignore to keep them private.*

---


## 💻 Setup Instructions

1. *Clone this repository*

    git clone https://github.com/navi-navi-612/detecting-data-leaks-sql-injection.git
    cd detecting-data-leaks-sql-injection

3. Install dependencies

    pip install -r requirements.txt

3. Add your .env file (Use .env.example as a reference)
     AES_SECRET_KEY=your-32-byte-secret-key ( and also user should define this key in a .env file)
4. Run the Flask application

    python app.py


---

🧪 Example .env.example

AES_SECRET_KEY=your-aes-secret-key
ADMIN_USERNAME=admin
ADMIN_PASSWORD=admin123
VALID_CAPABILITY_CODE=securecode2024


---

📡 Firebase Setup (Quick Guide)

1. Go to Firebase Console

2. Create a new project and enable Realtime Database

3. In Project Settings > Service Accounts, generate a new private key

4. Download and save it as firebase_config.json in your project

5. Add your Database URL inside the config



---

🧑‍💻 Author

Internship Project for CodeAlpha
Submitted by: Vendra Naveena
GitHub: navi-navi-612


---

🔐 Disclaimer

This is a demo project. Ensure best practices like environment variable protection, secure API keys, and HTTPS deployment for production use.

---
