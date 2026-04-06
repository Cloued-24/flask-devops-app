<img width="918" height="682" alt="1" src="https://github.com/user-attachments/assets/fd5ea7a1-bd0b-481b-bdc8-4722314174d2" /># Building and Containerizing a Flask Web Application with Docker: A Step-by-Step DevOps Project

Introduction

As I dive into the world of DevOps, one of the most fundamental skills to master is containerization. In this tutorial, I'll walk you through my DevOps project: containerizing a Flask web application with PostgreSQL using Docker and Docker Compose.

By the end of this guide, you'll have a fully containerized web application running on your local machine, and you'll understand the core concepts that power modern cloud-native applications.

Project Overview

What We're Building:

    A simple Flask web application that displays system information

    PostgreSQL database for data persistence

    Both services running in separate Docker containers

    Orchestrated with Docker Compose

Technologies Used:

    Python 3.9 & Flask 2.3.2

    PostgreSQL 13

    Docker & Docker Compose

    Git & GitHub

Step 1: Project Setup

Let's start by creating our project structure:

    mkdir flask-devops-app

    cd flask-devops-app

    mkdir app

Create the following files:

    touch app/__init__.py 
    app/routes.py 
    app/requirements.txt
    touch docker-compose.yml 
    Dockerfile 
    .dockerignore 
    .gitignore 
    README.md


![image alt](<img width="918" height="682" alt="1" src="https://github.com/user-attachments/assets/3b9af2f3-e9c3-445b-8da6-c544e2c26ef5" />
)

Step 2: Building the Flask Application

First, let's create a simple Flask app that displays container information:

app/requirements.txt

    Flask==2.3.2

app/init.py:

    from flask import Flask

    app = Flask(__name__)

    from app import routes

![image alt](<img width="704" height="422" alt="6" src="https://github.com/user-attachments/assets/695ff744-8d52-4829-9b05-cb87869ee1b5" />)

app/routes.py:

![image alt](<img width="1558" height="932" alt="7" src="https://github.com/user-attachments/assets/92086c1f-32d4-4341-b4bf-e7e133707d5e" />)

Step 3: Writing the Dockerfile

Now, let's create a production-ready Dockerfile:

![image alt](<img width="1545" height="844" alt="8" src="https://github.com/user-attachments/assets/22513975-3e12-4e51-b757-9819a4ba8866" />)

Step 4: Docker Compose for Multi-Container Setup

Let's add PostgreSQL using Docker Compose:

docker-compose.yml:

<img width="1554" height="1051" alt="9" src="https://github.com/user-attachments/assets/490ea1aa-eaaf-45f4-be1d-70f4dca9c144" />

Step 5: Building and Running the Application

Now for the exciting part - let's run our containers:

<img width="1849" height="840" alt="4" src="https://github.com/user-attachments/assets/b90bbd02-9290-402a-b5b8-eca0681a8616" />

Open your browser and navigate to http://localhost:5000. You should see the "Hello DevOps!" page displaying the container's hostname.





![image alt](https://github.com/Cloued-24/flask-devops-app/blob/8ea4351ccf0774c5212575341e76153999b8021c/flask-app-screenshot.png)

## Quick Start

1. Build and run:
```bash
docker-compose up -d

## Application Demo

