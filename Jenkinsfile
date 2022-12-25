pipeline {
  agent any
  stages {
    stage('store credentials') {
      steps {
        environment {
          def twilio_creds = credentials("twilio-credentials")
          USERNAME = twilio_creds.username
          PASSWORD = twilio_creds.password
        }
      }
    stage("run whatsapp bot")
      steps {
        sh 'python3 whatsapp.py ${env.USERNAME} ${env.PASSWORD}'
      }
    }
  }
}
