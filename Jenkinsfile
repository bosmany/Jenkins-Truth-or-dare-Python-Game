pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                // Checkout the code from the repository
                git 'https://github.com/your-repo/truth-or-dare.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t truth-or-dare-app .'
                }
            }
        }
        stage('Run Docker Container') {
            steps {
                script {
                    sh 'docker run -d --name truth-or-dare-container truth-or-dare-app'
                }
            }
        }
    }
}
