pipeline {
  agent {
    dockerfile {
      filename '.'
    }

  }
  stages {
    stage('test') {
      steps {
        sh 'python -m unittest'
      }
    }

  }
}