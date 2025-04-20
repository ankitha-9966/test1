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
                        "C:\\Users\\ADMIN\\AppData\\Local\\Microsoft\\WindowsApps\\python.exe" -m venv venv
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
                        "C:\\Users\\ADMIN\\AppData\\Local\\Microsoft\\WindowsApps\\python.exe" register.py
                    '''
                }
            }
        }
}