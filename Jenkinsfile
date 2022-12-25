pipeline {
    agent any

    environment {
        def twilio_creds = credentials("twilio-credentials")
        USERNAME = "${twilio_creds.username}"
        PASSWORD = "${twilio_creds.password}"
    }

    stages {
        stage('Run Python script') {
            steps {
                sh "python /path/to/script.py ${env.USERNAME} ${env.PASSWORD}"
            }
        }
    }
}
