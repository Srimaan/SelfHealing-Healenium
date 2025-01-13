# Self-Healing Test Automation (Python + Healenium)

## Overview
This project demonstrates **self-healing test automation** using **Selenium + Healenium**.

## Setup & Run Instructions

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Start Healenium Backend (Docker)
```bash
docker-compose up -d
```

### Run "Before" Test (Fails)
```bash
pytest tests/test_before_self_healing.py --html=reports/before_self_healing.html
```

### Run "After" Test (Passes with Healenium)
```bash
pytest tests/test_after_self_healing.py --html=reports/after_self_healing.html
```

### Results
Check **reports/before_self_healing.html** and **reports/after_self_healing.html**.

## 🎯 Key Features
✅ Demonstrates failing tests **before self-healing**  
✅ Enables **Healenium to dynamically fix broken locators**  
✅ Generates **pytest HTML reports**  
✅ Fully **Dockerized setup**  
