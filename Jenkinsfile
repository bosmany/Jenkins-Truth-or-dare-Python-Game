pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    credentialsId: 'github-token', // Replace with your credentials ID
                    url: 'https://github.com/bosmany/Jenkins-Truth-or-dare-Python-Game.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t truth-or-dare-app .'
            }
        }
        stage('Run Docker Container') {
            steps {
                sh 'docker run -d --name truth-or-dare-container truth-or-dare-app'
            }
        }
    }
}
