# Library Management System

A Python desktop application for managing library book records through a graphical user interface built with **CustomTkinter** and **SQLite**. The project is designed with an object-oriented structure that separates the GUI, application controller, and database operations.

> **Project status:** In development. Features and workflows may change as the application evolves.

## Overview

The Library Management System aims to make everyday book management simpler through a desktop interface. It is being developed around reusable GUI components and a dedicated database layer, with the goal of keeping the code organized, understandable, and maintainable.

## Planned capabilities

- **Book records** — add, view, and manage book information.
- **Book list** — display saved books in a reusable list/card interface.
- **Search and navigation** — find and navigate book records through the GUI.
- **Status feedback** — show clear feedback for application actions.
- **SQLite storage** — persist library data in a local database.

The list describes the project's intended scope; consult the current code to see which capabilities are implemented.

## Technology stack

- **Python** — application logic.
- **CustomTkinter** — desktop interface.
- **SQLite (`sqlite3`)** — local database storage.
- **Pathlib** — file and database path management.
- **Git and GitHub** — version control and source hosting.

## Architecture

The project is being organized into distinct layers:

```text
main.py
  └── gui/app.py
        └── Controller
              ├── GUI widgets (BookForm, BookList, BookCard)
              └── Library / Database
```

The intended separation of responsibilities is:

- **Entry point:** starts the application.
- **GUI:** displays forms, lists, toolbars, and status information.
- **Controller:** connects user actions to application operations.
- **Library/database layer:** handles book-related logic and SQLite access.

The actual repository structure may evolve during development.

## Getting started

### 1. Clone the repository

```bash
git clone https://github.com/Mohid-Emma/library-management-system.git
cd library-management-system
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv .venv
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

Install CustomTkinter:

```bash
python -m pip install customtkinter
```

SQLite support (`sqlite3`) is included with standard Python installations. If the repository provides a `requirements.txt`, you can instead install the listed dependencies with:

```bash
python -m pip install -r requirements.txt
```

### 4. Run the application

From the project root, run:

```bash
python main.py
```

If the entry point or dependency setup changes, follow the current repository code and configuration.

## Database

The project uses SQLite for local data storage. The planned database location is:

```text
~/Library Management System/library.db
```

Keep backups of important database files before testing changes that could alter or delete records.

## Development principles

This project is also a learning exercise in object-oriented GUI development. Its guiding principles include:

- Single Responsibility Principle (SRP).
- Clear separation between frontend, controller, and backend/database logic.
- Reusable widgets and consistent UI styling.
- Explicit error handling and useful status messages.
- Small, testable improvements rather than large rewrites.

## Contributing

Suggestions and improvements are welcome. Keep changes focused and test them before submitting.

1. Fork the repository.
2. Create a branch for your change.
3. Implement and test the improvement.
4. Submit a pull request explaining the change.

## Author

Created and maintained by **Mohid Younas**.

- GitHub: [@Mohid-Emma](https://github.com/Mohid-Emma)
- Repository: [library-management-system](https://github.com/Mohid-Emma/library-management-system)

---

*Building a simple, maintainable library management experience with Python, CustomTkinter, and SQLite.*
