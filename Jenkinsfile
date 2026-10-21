
pipeline {
    agent any

    options {
        timeout(time: 5, unit: 'MINUTES')
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Stage 1: Checking out source code from GitHub...'
                checkout scm
            }
        }

        stage('Run HTML Form Tests') {
            steps {
                echo 'Stage 2: Running automated tests (test_form.py)...'

                script {
                    if (isUnix()) {
                        sh 'python3 test_form.py'
                    } else {
                        bat '"C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" test_form.py'
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'HTML Form Testing Pipeline execution completed.'
        }

        success {
            echo 'BUILD SUCCESS: All HTML form tests passed.'
        }

        failure {
            echo 'BUILD FAILED: Check the Console Output for details.'
        }
    }
}
