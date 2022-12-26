pipeline {
    agent any

    environment {
        TWILIO_CREDS = credentials("twilio-credentials")
    }

    stages {
        stage('Run Python script') {
            steps {
                sh 'python3 whatsapp.py ${TWILIO_CREDS_USR} ${TWILIO_CREDS_PSW}'
            }
        }
    }
}
