pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/SHREYASKURANE/ICU_MLOps_Project.git'
            }
        }

        stage('Python Version') {
            steps {
                bat '"C:\\Users\\ADC\\Desktop\\ICU_MLOps_Project\\venv\\Scripts\\python.exe" --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\ADC\\Desktop\\ICU_MLOps_Project\\venv\\Scripts\\pip.exe" install -r requirements.txt'
            }
        }

        stage('Preprocessing') {
            steps {
                bat '"C:\\Users\\ADC\\Desktop\\ICU_MLOps_Project\\venv\\Scripts\\python.exe" src\\preprocess.py'
            }
        }

        stage('Train Model') {
            steps {
                bat '"C:\\Users\\ADC\\Desktop\\ICU_MLOps_Project\\venv\\Scripts\\python.exe" src\\train.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t icu-mlops:latest .'
            }
        }
    }

    post {

        success {
            echo 'ICU MLOps Pipeline Completed Successfully!'
        }

        failure {
            echo 'Pipeline Failed!'
        }
    }
}