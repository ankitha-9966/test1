pipeline {
    agent any
        stages{
            stage('Checkout code') {
                steps {
                    git credentialsId: 'PATAproject', url: "https://github.com/ankitha-9966/test1.git", branch: "main"
                }
            }

            stage('Install dependencies') {
                steps{
                    bat '''
                        python -m venv venv
                        call venv\\Scripts\\activate
                        pip install --upgrade pip
                        pip install pytest
                    '''
                }
            }
            stage('Test') {
                steps{
                    bat '''
                        call venv\\Scripts\\activate
                        pytest test.py
                    '''
                }
            }

            stage('Deploy') {
                steps {
                    bat '''
                        call venv//Scripts//activate
                        python register.py
                    '''
                }
            }
        }
}