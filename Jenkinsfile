pipeline {

    agent any

    environment {
        PYTHON = "C:\\Users\\ADC\\Desktop\\ICU_MLOps_Project\\venv\\Scripts\\python.exe"
        PIP = "C:\\Users\\ADC\\Desktop\\ICU_MLOps_Project\\venv\\Scripts\\pip.exe"
        DOCKER = "C:\\Users\\ADC\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe"
    }

    stages {

        stage('Checkout Source Code') {
            steps {
                checkout scm
            }
        }

        stage('Python Version') {
            steps {
                bat "\"%PYTHON%\" --version"
            }
        }

        stage('Install Dependencies') {
            steps {
                bat "\"%PIP%\" install -r requirements.txt"
            }
        }

        stage('Data Preprocessing') {
            steps {
                bat "\"%PYTHON%\" src\\preprocess.py"
            }
        }

        stage('Model Training') {
            steps {
                bat "\"%PYTHON%\" src\\train.py"
            }
        }

        stage('Check Docker') {
            steps {
                bat "\"%DOCKER%\" --version"
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "\"%DOCKER%\" build -t icu-mlops:latest ."
            }
        }

    }

    post {

        success {
            echo "===================================="
            echo " ICU MLOps Pipeline SUCCESSFUL "
            echo "===================================="
        }

        failure {
            echo "===================================="
            echo " ICU MLOps Pipeline FAILED "
            echo "===================================="
        }

        always {
            cleanWs()
        }
    }
}