if (env.BRANCH_NAME == "master" || env.BRANCH_NAME == "main"){
    properties([
        pipelineTriggers([
            pollSCM("*/5 * * * *")
        ])
    ])
}

def ui_image
def api_image

pipeline { 
    agent any

    stages {
        stage('Build') {
            steps{
                // script{
                //     echo 'Building Tic-Tac-Toe images................'
                //     api_image = docker.build("danielpenado/tctctoe-api", "WEB_GAME/server/")    
                //     ui_image = docker.build("danielpenado/tctctoe-ui", "WEB_GAME/frontend/tic-tac-toe/")
                // }
                dir('WEB_GAME/server'){
                    script{
                        sh 'ls'
                    }
                }
            }
        }
        stage('Test'){
            steps{
                script{
                    echo 'Testing Tic-Tac-Toe game....................'
                    api_image.inside {
                        sh 'echo run API tests'
                    }    
                }
            }
        }
        stage('Deploy'){
            steps{
                script{
                    echo 'Publishing Tic-Tac-Toe images to Docker Hub...................'
                    api_image.push()
                    ui_image.push()  
                    sh "docker rmi danielpenado/tctctoe-api"  
                    sh "docker rmi danielpenado/tctctoe-ui"
                }
            }
        }
    }
}