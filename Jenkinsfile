pipeline {
    agent any
    environment {
        DOCKER_USER = "zulfianra" 
        GIT_REPO_URL = "https://github.com/zulfianra31/kantin-app.git"
    }
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: "${GIT_REPO_URL}"
            }
        }
        stage('Build & Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-login', passwordVariable: 'PASS', usernameVariable: 'USER')]) {
                    // Ganti sh menjadi bat karena kamu pakai Windows
                    bat "docker build -t ${USER}/kantin-backend:latest ./backend"
                    bat "docker build -t ${USER}/kantin-frontend:latest ./frontend"
                    bat "echo ${PASS} | docker login -u ${USER} --password-stdin"
                    bat "docker push ${USER}/kantin-backend:latest"
                    bat "docker push ${USER}/kantin-frontend:latest"
                }
            }
        }
        stage('Deploy ke Azure AKS') {
            steps {
                withKubeConfig([credentialsId: 'aks-config']) {
                    bat "kubectl apply -f kantin-k8s.yaml"
                    bat "kubectl rollout restart deployment backend-kantin"
                    bat "kubectl rollout restart deployment frontend-kantin"
                }
            }
        }
    }
}