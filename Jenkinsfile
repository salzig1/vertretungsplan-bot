pipeline {
  agent any
  stages {
    stage('start_whatsapp_bot') {
      enviroment {
        TWILIO_CREDS = credentials("twilio-credentials")
      }
      steps {
        sh 'python3 whatsapp.py ${TWILIO_CRED_USR} ${TWILIO_CRED_PSW}'
      }
    }
  }
}
