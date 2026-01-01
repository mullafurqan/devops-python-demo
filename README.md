# 🚀 DevOps Python Demo

A simple Python application built to demonstrate DevOps concepts such as application setup, containerization using Docker, service orchestration with Docker Compose, and deployment-ready project structure.  
This README is written using the **devops-node-demo** repository as reference.

---

## 📦 Project Features

- Python application
- Docker containerization
- Docker Compose orchestration
- DevOps-ready structure
- Easy to run locally or using containers

---

## 📂 Project Structure

devops-python-demo/
├── templates/
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── README.md

---

## 🐍 Application Overview

The application is a simple Python web app (for example, Flask-based) that listens on a specified port and serves HTTP requests.  
It is designed to be lightweight and suitable for containerized deployments.

---

## 🛠️ Getting Started (Without Docker)

1. Clone the repository  
git clone https://github.com/mullafurqan/devops-python-demo.git  
cd devops-python-demo  

2. Install dependencies  
pip install -r requirements.txt  

3. Run the application  
python app.py  

Application will be available at:  
http://localhost:5000

---

## 🐳 Using Docker

Build the Docker image  
docker build -t devops-python-demo .

Run the Docker container  
docker run -p 5000:5000 devops-python-demo

Access the application at:  
http://localhost:5000

---

## 🐙 Using Docker Compose

Start the application  
docker-compose up --build

Stop the application  
docker-compose down

---

## 🧠 Purpose & Learning

This repository helps in understanding:
- Python application deployment
- Docker image creation and container lifecycle
- Docker Compose usage
- Foundations for CI/CD pipelines

---

## 👨‍💻 Author

Furqan Mulla  
GitHub: https://github.com/mullafurqan

---

## 📌 Notes

This project is created for learning and demonstration purposes as part of DevOps practice and portfolio development.
