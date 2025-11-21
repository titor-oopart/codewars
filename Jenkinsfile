pipeline {
    agent any

    stages {

        stage('Pull Docker Images') {
            steps {
                sh 'docker pull krahuz/codewars:python-v2'
                sh 'docker pull krahuz/codewars:js-v2'
            }
        }

        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/krahuz/codewars.git'
            }
        }

        stage('Python Tests') {
            steps {
                sh '''
                docker run --rm \
                    -v $PWD:/app \
                    krahuz/codewars:python-v1 \
                    python run_all_test.py
                '''
            }
        }

        stage('JavaScript Tests') {
            steps {
                sh '''
                docker run --rm \
                    -v $PWD:/app \
                    krahuz/codewars:js-v1 \
                    npx mocha test
                '''
            }
        }
    }
}
