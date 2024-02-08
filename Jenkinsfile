pipeline {
    agent {
        docker {
            image 'python:3.11.7'
        }
    }

    triggers {
        pollSCM '*/5 * * * *'
    }

    // environment {
    //     POSTGRES_DB = credentials('jenkins-postgres-db')
    //     POSTGRES_USER = credentials('jenkins-postgres-user') 
    //     POSTGRES_PASSWORD = credentials('jenkins-postgres-password')
    //     POSTGRES_HOST = credentials('jenkins-postgres-host')
    //     POSTGRES_PORT = credentials('jenkins-postgres-port')
    // }

    stages {
        stage('Building') {
            steps {
                echo 'Building...'
                sh '''
                    python3 -m venv env
                    . ./env/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Testing') {
            steps {
                echo 'Testing...'
                sh '''
                    . ./env/bin/activate
                    pytest
                '''
            }
        }

        stage('Deploying') {
            steps {
                echo 'Deploying...'
                // sh '''
                //     docker build -t emsdjango.azurecr.io/emsdjango:latest .
                //     docker push emsdjango.azurecr.io/emsdjango:latest
                // '''
            }
        }
    }
}