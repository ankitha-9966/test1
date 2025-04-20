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
                        "C:\\Users\\ADMIN\\AppData\\Local\\Microsoft\\WindowsApps\\python.exe" -m venv venv'''
                    bat '''
                        .\\venv\\Scripts\\activate && python -m
                        pip install --upgrade pip'''
                    bat '''
                        .\\venv\\Scripts\\activate && python -m
                        pip install pytest
                    '''
                }
            }
            stage('Test') {
                steps{
                    bat '''
                        .\\venv\\Scripts\\activate && python
                        pytest test.py
                    '''
                }
            }

            stage('Deploy') {
                steps {
                    bat '''
                        .\\venv\\Scripts\\activate
                        "C:\\Users\\ADMIN\\AppData\\Local\\Microsoft\\WindowsApps\\python.exe" register.py
                    '''
                }
            }
        }
}