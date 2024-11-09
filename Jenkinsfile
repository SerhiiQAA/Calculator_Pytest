pipeline {
    agent any

    tools {
        python 'Python' // Ім'я Python установки, яке ви налаштували у Jenkins
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/SerhiiQAA/Calculator_Pytest.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Pytest') {
            steps {
                sh 'pytest --junitxml=results.xml'
            }
        }
    }

    post {
        always {
            junit 'results.xml'
            cleanWs()
        }
    }
}
