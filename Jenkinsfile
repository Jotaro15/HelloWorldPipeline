pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                echo 'Setting up the environment...'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Build') {
            steps {
                echo 'Running Hello World program...'
                sh 'python hello_world.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Running unit tests...'
                sh 'pip install pytest'
                sh 'pytest'
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
