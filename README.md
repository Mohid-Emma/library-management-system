# 📚 Library Management System

A desktop-based **Library Management System** built with **Python, CustomTkinter, and SQLite**.

The application provides a simple and modern graphical interface for managing books, borrowers, borrowing, and returning.

## ✨ Features

* 📚 Add new books
* ✏️ Edit book information
* 🗑️ Delete books
* 🔍 Search books
* ↕️ Sort books
* 📖 Borrow books
* ↩️ Return books
* 👤 Manage borrowers
* 💾 Store data using SQLite
* 🖥️ Modern CustomTkinter interface
* 🪟 Windows `.exe` application

## 🛠️ Technologies

| Technology    | Purpose                   |
| ------------- | ------------------------- |
| Python        | Main programming language |
| CustomTkinter | Graphical user interface  |
| SQLite        | Database                  |
| PyInstaller   | Create Windows executable |

## 📂 Project Structure

```text
Library_Project/
│
├── main.py
│
├── assets/
│   ├── icon.png
│   └── icon.ico
│
├── database/
│   ├── database.py
│   ├── library.db
│   └── __init__.py
│
├── gui/
│   ├── app.py
│   ├── controller.py
│   ├── borrower_dialog.py
│   └── __init__.py
│
├── library/
├── models/
├── utils/
├── widgets/
│
└── README.md
```

## 🚀 Run from Source Code

### 1. Clone the repository

```bash
git clone https://github.com/Mohid-Emma/library-management-system.git
```

### 2. Open the project

```bash
cd library-management-system
```

### 3. Install the required package

```bash
pip install customtkinter
```

### 4. Run the application

```bash
python main.py
```

## 🪟 Windows Application

A ready-to-use Windows executable is available in the **GitHub Releases** section.

Download:

```text
Library Management System.exe
```

You do not need to install Python to use the executable.

## 💾 Database

The application uses **SQLite** to store library data.

The database is created automatically when the application starts.

User data is stored separately from the application files so that rebuilding or updating the application does not unnecessarily replace the user's database.

## 🎨 Interface

The application uses **CustomTkinter** to provide a modern desktop interface with:

* Sidebar navigation
* Book management
* Search and sorting
* Borrow and return actions
* Status information
* Dark-themed interface

## 🧠 Architecture

The project is organized into separate components to keep responsibilities clear.

```text
User
  │
  ▼
CustomTkinter GUI
  │
  ▼
Controller
  │
  ▼
Library Logic
  │
  ▼
SQLite Database
```

This separation makes the project easier to understand, maintain, and improve.

## 📌 Project Status

**Version:** `1.0.0`

The project is currently a working desktop Library Management System. Future improvements may include additional library features, better data validation, and further UI improvements.

## 📄 License

This project is available for learning and personal use.
