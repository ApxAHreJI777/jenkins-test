pipeline {
  agent any
  stages {
    stage('Checkout code') {
      steps {
        git(url: 'https://github.com/ApxAHreJI777/jenkins-test', branch: 'master')
      }
    }

    stage('Test') {
      steps {
        sh 'docker-compose up --build -d'
        sh 'docker exec jenkinstest python -m unittest'
        sh 'docker-compose down'
      }
    }

  }
}