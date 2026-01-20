# Qchat: A Simple Chat Application 💬

**Qchat** is a minimalistic, real-time chat application built using **NiceGUI**, a Python framework for building web applications. This project allows users to send and receive messages instantly with a clean, modern interface and unique user identification.

---

## 🚀 Key Features
* **Real-time Messaging:** Send and receive messages instantly without page reloads using NiceGUI's refreshable components.
* **Unique User Avatars:** Automatically generates unique user avatars via **Robohash** based on session UUIDs.
* **Modern UI:** A clean, responsive design featuring a fixed footer input and "sent/received" message alignment.
* **Intuitive Controls:** Supports `Enter` key functionality for quick messaging.

---

## 🛠️ Technical Details
* **Framework:** NiceGUI (Python-based)
* **User Tracking:** `uuid4` for session-based user identification.
* **Avatar API:** Robohash (Set to `bg2` background style).
* **Styling:** Tailwind CSS classes (via NiceGUI) for layout and alignment.
* **Author:** Ritik Pratap Singh Patel

---

## 🎮 How to Use
1. **Launch:** Run the script to start the local web server.
2. **Access:** Open your browser and go to `http://localhost:8080` (default NiceGUI port).
3. **Identity:** A unique robot avatar is assigned to you automatically.
4. **Chat:** Type your message in the rounded input box at the bottom and press **Enter** or click away to send.

---

## 💻 Installation & Setup

### 1. Requirements
Ensure you have Python 3.9+ installed on your system.

### 2. Install Dependencies
You will need to install `nicegui` via pip:
```bash
pip install nicegui
```

### 3. Run the Application
```bash
python qchat.py
