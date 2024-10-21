pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                echo 'Setting up the environment...'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Build') {
            steps {
                echo 'Running Hello World program...'
                bat 'python hello_world.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Running unit tests...'
                bat 'pip install pytest'
                bat 'pytest'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
