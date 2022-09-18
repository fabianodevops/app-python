pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3-alpine'
                }
            }
        }    
        stage('Installing packages') {
            steps {
                script {
                    sh 'pip install -r app/requirements.txt'
                }
            }
        }
    }
}
