if (env.BRANCH_NAME == "master" || env.BRANCH_NAME == "main"){
    properties([
        pipelineTriggers([
            pollSCM("*/5 * * * *")
        ])
    ])
}

pipeline { 
    agent any

    def ui_image
    def api_image

    stages {
        stage('Build') {
            steps{
                echo 'Building Tic-Tac-Toe images................'
                sh 'ls'
                api_image = docker.build("danielpenado/tctctoe-api", "./WEB_GAME/server/")    
                ui_image = docker.build("danielpenado/tctctoe-ui", "./WEB_GAME/frontend/tic-tac-toe")
            }
        }
        stage('Test'){
            steps{
                echo 'Testing Tic-Tac-Toe game....................'
                api_image.inside {
                    sh 'run API tests'
                }    
                ui_image.inside {
                    sh 'run UI tests'
                }
            }
        }
        stage('Deploy'){
            steps{
                echo 'Publishing Tic-Tac-Toe images to Docker Hub...................'
                api_image.push()
                ui_image.push()  
                sh "docker rmi danielpenado/tctctoe-api"  
                sh "docker rmi danielpenado/tctctoe-ui"
            }
        }
    }
}