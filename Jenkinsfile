if (env.BRANCH_NAME == "master" || env.BRANCH_NAME == "main"){
    properties([
        pipelineTriggers([
            pollSCM("*/3 * * * *")
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
                    dir('WEB_Game'){
                        sh 'docker compose up -d'
                        sh 'docker exec tctctoe-api bash -c "python3 -m unittest tests/test*.py"'
                        sh 'docker compose down'
                    }  
                }
            }
        }
        stage('Deploy'){
            steps{
                script{
                    echo 'Publishing Tic-Tac-Toe images to Docker Hub...................'
                    withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'DOCKER_REGISTRY_PWD', usernameVariable: 'DOCKER_REGISTRY_USER')]) {
                        sh "docker login -u ${DOCKER_REGISTRY_USER} -p ${DOCKER_REGISTRY_PWD}"
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