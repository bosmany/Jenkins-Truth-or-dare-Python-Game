pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    credentialsId: 'github-token', // Replace with your actual credentials ID
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
                // Stop and remove the existing container if it exists
                sh '''
                if [ "$(docker ps -aq -f name=truth-or-dare-container)" ]; then
                    docker stop truth-or-dare-container
                    docker rm truth-or-dare-container
                fi
                docker run -d --name truth-or-dare-container truth-or-dare-app
                '''
            }
        }
    }
}
