pipeline {
    agent none
    stages {
        stage('Installing packages') {
            steps {
                script {
                    sh 'pip install -r app/requirements.txt'
                }
            }
        }
    }
}
