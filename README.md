# Building and Containerizing a Flask Web Application with Docker: A Step-by-Step DevOps Project

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



![image alt](https://github.com/Cloued-24/flask-devops-app/blob/8ea4351ccf0774c5212575341e76153999b8021c/flask-app-screenshot.png)

## Quick Start

1. Build and run:
```bash
docker-compose up -d

## Application Demo

