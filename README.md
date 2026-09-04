# Python Application CI/CD Pipeline with Jenkins, Docker & AWS EC2

A beginner-friendly **CI/CD project** that demonstrates how to automatically build and deploy a Python Flask application using **GitHub, Jenkins, Docker, and AWS EC2**.

## 🚀 Project Overview

This project implements an automated CI/CD pipeline where a developer pushes code to GitHub, which triggers Jenkins through a GitHub webhook.

Jenkins then:

1. Checks out the latest source code
2. Builds a Docker image
3. Stops the previous application container
4. Removes the old container
5. Starts a new container with the updated application

The application is deployed and accessible through an AWS EC2 instance.

## 🏗️ Architecture

```text
                    Developer
                        |
                        | git push
                        v
                    GitHub
                        |
                        | Webhook
                        v
              +-------------------+
              | Jenkins on EC2     |
              +-------------------+
                        |
                        v
                  Checkout Code
                        |
                        v
                 Docker Build
                        |
                        v
              practice:latest
                        |
                        v
              Stop Old Container
                        |
                        v
              Remove Old Container
                        |
                        v
               Run New Container
                        |
                        v
              +-------------------+
              | Docker Container  |
              | Python Flask App  |
              +-------------------+
                        |
                        v
                   Web Browser
```

## 🛠️ Technologies Used

* **Python**
* **Flask**
* **Git & GitHub**
* **Jenkins**
* **Docker**
* **AWS EC2**
* **Linux / Ubuntu**
* **GitHub Webhooks**

## 📁 Project Structure

```text
devops-project12/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── README.md
```

## 🐍 Application

The application is built using Python and Flask.

The Flask application runs on:

```text
0.0.0.0:5000
```

A health endpoint is also available:

```text
/health
```

Example response:

```json
{
    "status": "healthy",
    "application": "DevOps Task Manager"
}
```

## 🐳 Docker

The application is packaged as a Docker image.

Build the image manually:

```bash
docker build -t practice:latest .
```

Run the container:

```bash
docker run -d \
    --name practice \
    -p 5000:5000 \
    practice:latest
```

Check the running container:

```bash
docker ps
```

Test the application:

```bash
curl http://localhost:5000
```

## ⚙️ Jenkins CI/CD Pipeline

The Jenkins pipeline is responsible for automatically building and deploying the application.

### Pipeline Stages

```text
Checkout
   ↓
Build Docker Image
   ↓
Deploy
```

### Checkout

Jenkins retrieves the latest code from the `main` branch.

### Build

Jenkins builds the Docker image:

```bash
docker build -t practice:latest .
```

### Deploy

The existing container is stopped and removed:

```bash
docker stop practice || true
docker rm practice || true
```

Then the new container is started:

```bash
docker run -d \
    --name practice \
    -p 5000:5000 \
    practice:latest
```

## 🔄 GitHub Webhook

GitHub is configured to trigger Jenkins whenever code is pushed to the repository.

Webhook endpoint:

```text
http://<EC2-PUBLIC-IP>:8080/github-webhook/
```

The workflow is:

```text
git push
    ↓
GitHub
    ↓
Webhook
    ↓
Jenkins
    ↓
Pipeline
    ↓
Docker Build
    ↓
Deployment
```

This removes the need to manually click **Build Now** in Jenkins after every code change.

## ☁️ AWS EC2 Setup

Jenkins and Docker are installed on an Ubuntu EC2 instance.

Required services:

```text
AWS EC2
 ├── Jenkins
 ├── Docker
 └── Python application container
```

### Security Group

The EC2 Security Group needs appropriate inbound rules.

For the learning environment:

| Port | Purpose           |
| ---: | ----------------- |
|   22 | SSH               |
| 8080 | Jenkins           |
| 5000 | Flask application |

> For production environments, Jenkins should not be exposed directly to the public internet on port 8080. A secure HTTPS setup with appropriate network restrictions should be used.

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/kranthi1382/devops-project12.git
cd devops-project12
```

### 2. Build the Docker image

```bash
docker build -t practice:latest .
```

### 3. Run the application

```bash
docker run -d \
    --name practice \
    -p 5000:5000 \
    practice:latest
```

### 4. Access the application

Open:

```text
http://<EC2-PUBLIC-IP>:5000
```

## 🔧 Jenkins Configuration

Create a Jenkins **Pipeline** job.

The pipeline uses a Pipeline script stored directly in Jenkins rather than a `Jenkinsfile` in the GitHub repository.

Example pipeline:

```groovy
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/kranthi1382/devops-project12.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t practice:latest .'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    docker stop practice || true
                    docker rm practice || true

                    docker run -d \
                        --name practice \
                        -p 5000:5000 \
                        practice:latest
                '''
            }
        }

    }
}
```

## 📌 CI/CD Workflow

After the initial setup, the normal development workflow is:

```bash
# Make changes to the application

git add .

git commit -m "Update application"

git push origin main
```

GitHub then triggers Jenkins automatically.

```text
Developer
    ↓
git push
    ↓
GitHub
    ↓
Webhook
    ↓
Jenkins
    ↓
Checkout
    ↓
Docker Build
    ↓
Deploy
    ↓
Updated Application
```

## 🎯 What I Learned

Through this project, I learned how to:

* Use Git and GitHub for source-code management
* Create and manage a Jenkins Pipeline
* Configure GitHub webhooks
* Install and manage Jenkins on AWS EC2
* Install and use Docker on Ubuntu
* Create a Docker image for a Python application
* Run applications inside Docker containers
* Automate application deployment
* Configure AWS EC2 Security Groups
* Understand the basic CI/CD workflow

## 🔮 Future Improvements

Possible improvements for the next version:

* Add automated Python unit tests
* Add Docker Compose
* Push images to Docker Hub
* Add image versioning/tagging
* Store secrets securely using Jenkins Credentials
* Add application health checks
* Add HTTPS for Jenkins and the application
* Add monitoring and logging
* Introduce Infrastructure as Code using Terraform
* Deploy using AWS services such as ECS

## 👨‍💻 Author

**Kranthi**

This project was created as a hands-on DevOps learning project to understand CI/CD automation using Jenkins, Docker, GitHub, and AWS.
