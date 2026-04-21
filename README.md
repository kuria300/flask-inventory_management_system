# Inventory CLI & REST API

A **Flask** application that provides a RESTful interface to manage inventory, paired with a **CLI** for direct In-memory database interactions.

---

## Features

- REST API for inventory management
- CLI for direct database operations
- In-memory storage (no external DB required)
- Lightweight and easy to run
- Clean separation of API and CLI logic

---

## Getting Started

### 1. Installation
Ensure you have `pipenv` installed, then clone and install dependencies:
```bash
git clone <repository_url>
cd inventory-app
pipenv install / pipenv sync
pipenv shell
python <entrypoint>
