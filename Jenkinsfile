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
                script{
                    echo 'Building Tic-Tac-Toe images................'
                    api_image = docker.build("danielpenado/tctctoe-api", "WEB_Game/server/")    
                    ui_image = docker.build("danielpenado/tctctoe-ui", "WEB_Game/frontend/tic-tac-toe/")
                }
            }
        }
        stage('Test'){
            steps{
                script{
                    echo 'Testing Tic-Tac-Toe game....................'
                    api_image.inside {
                        sh 'ls'
                        sh 'pwd'
                    }    
                }
            }
        }
        stage('Deploy'){
            steps{
                script{
                    echo 'Publishing Tic-Tac-Toe images to Docker Hub...................'
                    withCredentials([string(credentialsId: 'dockerhub', variable: 'dockerpwd')]) {
                        sh "docker login -u danielpenado -p ${dockerpwd}"
                        api_image.push()
                        ui_image.push()
                    }
                }
            }
        }
    }
    post{
        always{
            sh "docker rmi danielpenado/tctctoe-api"  
            sh "docker rmi danielpenado/tctctoe-ui"
            sh "docker logout"
        }
    }
}