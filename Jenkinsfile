pipeline {
    // Run on any available Jenkins agent (the Jenkins server itself is fine for this practical)
    agent any

    options {
        // Stop the build if it hangs for more than 5 minutes
        timeout(time: 5, unit: 'MINUTES')
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Stage 1: Checking out source code from GitHub...'
                // Uses the repository configured in the Jenkins job.
                // No credentials are written here; if the repo is private,
                // select a credential in the job settings instead.
                checkout scm
            }
        }

        stage('Run HTML Form Tests') {
            steps {
                echo 'Stage 2: Running automated tests (test_form.py)...'
                script {
                    // Works on both Windows and Linux Jenkins agents.
                    // If test_form.py exits with a non-zero code, this step
                    // fails and Jenkins marks the build as FAILED.
                    if (isUnix()) {
                        sh 'python3 test_form.py'
                    } else {
                        bat 'python test_form.py'
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'BUILD SUCCESS: All HTML form tests passed.'
        }
        failure {
            echo 'BUILD FAILED: One or more HTML form tests failed. Check the console output above.'
        }
    }
}
