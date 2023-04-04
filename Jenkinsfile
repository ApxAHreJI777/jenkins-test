pipeline {
  agent any
  stages {
    stage('Checkout Code') {
      steps {
        git(url: 'https://github.com/ApxAHreJI777/jenkins-test', branch: 'master')
      }
    }

    stage('Build') {
      steps {
        sh 'docker-compose up --build -d'
      }
    }

    stage('Test') {
      steps {
        sh 'docker exec jenkinstest python -m unittest'
      }
    }

    stage('Cleanup') {
      steps {
        sh 'docker-compose down'
      }
    }

  }
}