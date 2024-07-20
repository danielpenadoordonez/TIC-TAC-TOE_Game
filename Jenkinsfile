if (env.BRANCH_NAME == "master" || env.BRANCH_NAME == "main"){
    properties([
        pipelineTriggers([
            pollSCM("*/2 * * * *")
        ])
    ])
}

def ui_image
def api_image

pipeline { 
    agent any

    environment {
        TCTCTOE_MACHINE_API = 'tctctoe-api-svc'
        JENKINS_DOCKER_SERVER = 'jenkins-docker'
    }
    
    parameters {
        booleanParam(name: 'DOCKER_COMPOSE_TEST', defaultValue: true, description: 'Run application tests in a Docker Compose environment')
    }

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
            parallel {
                stage('Testing in Docker Compose'){
                    when{
                        expression{
                            params.'DOCKER_COMPOSE_TEST' == true
                        }
                    }
                    steps{
                        script{
                            echo 'Testing Tic-Tac-Toe game....................' 
                            dir('WEB_Game'){
                                sh 'docker compose up -d'
                                //Run Backend Unit Tests
                                sh 'docker exec tctctoe-api bash -c "python3 -m unittest tests/test*.py"'
                                //Test connection to the nginx server that runs the UI and then the connection from the UI to the API
                                sh 'curl -v http://${JENKINS_DOCKER_SERVER}'
                                sh 'docker exec tctctoe-ui curl -v http://${TCTCTOE_MACHINE_API}:8080/api/get-game-id'
                                sh 'docker compose down'
                            }  
                        }
                    }
                }
                stage('Testing on the host'){
                    steps{
                        script{
                            catchError(stageResult: 'UNSTABLE', buildResult: currentBuild.result){
                                dir('WEB_Game/server'){
                                    sh 'python3 api.py'
                                    //Run Backend Unit Tests
                                    sh 'python3 -m unittest tests/test*.py'
                                    sh 'curl -v http://localhost:8080/api/get-game-id'
                                    //Test connection to the nginx server that runs the UI and then the connection from the UI to the API
                                    //sh 'curl -v http://${JENKINS_DOCKER_SERVER}'
                                    //sh 'docker exec tctctoe-ui curl -v http://${TCTCTOE_MACHINE_API}:8080/api/get-game-id'
                                }
                            }
                        }
                    }
                }
            }
        }
        stage('Publish images'){
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
            script{
                echo 'Cleaning up the build environment..........................'
                dir('WEB_Game'){
                    sh 'docker compose down'
                }
            }
            sh "docker rmi danielpenado/tctctoe-api"  
            sh "docker rmi danielpenado/tctctoe-ui"
            sh "docker logout"
        }
    }
}