@Library('cicd-pipeline-library') _

import clss.ImageSpec

if (env.BRANCH_NAME == "master" || env.BRANCH_NAME == "main"){
    properties([
        pipelineTriggers([
            pollSCM("*/2 * * * *")
        ])
    ])
}

def tctctoeImages = []

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
                    println('Building Tic-Tac-Toe images................')

                    List<ImageSpec> imageSpecs = new ArrayList<ImageSpec>()
                    imageSpecs.add(new ImageSpec("danielpenado/tctctoe-api", "WEB_Game/server/"))
                    imageSpecs.add(new ImageSpec("danielpenado/tctctoe-ui", "WEB_Game/frontend/tic-tac-toe/"))

                    tctctoeImages = dockerUtils.buildImages(imageSpecs)
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
                            println('Testing Tic-Tac-Toe game....................') 
                            dir('WEB_Game'){
                                List<String> testCommands = new ArrayList<String>()

                                testCommands.add('docker compose up -d')
                                testCommands.add('docker exec tctctoe-api bash -c "python3 -m unittest tests/test*.py"')
                                testCommands.add('curl -v http://${JENKINS_DOCKER_SERVER}')
                                testCommands.add('docker exec tctctoe-ui curl -v http://${TCTCTOE_MACHINE_API}:8080/api/get-game-id')
                                testCommands.add('docker compose down')

                                testCommands.each{ testCmd -> sh testCmd }
                            }  
                        }
                    }
                }
                stage('Testing on the host'){
                    steps{
                        script{
                            catchError(stageResult: 'UNSTABLE', buildResult: currentBuild.result){
                                dir('WEB_Game/server'){
                                    List<String> testCommands = new ArrayList<String>()

                                    testCommands.add('python3 api.py')
                                    testCommands.add('python3 -m unittest tests/test*.py')
                                    testCommands.add('curl -v http://localhost:8080/api/get-game-id')

                                    testCommands.each{ testCmd -> sh testCmd }        
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
                    println('Publishing Tic-Tac-Toe images to Docker Hub...................')
                    withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'DOCKER_REGISTRY_PWD', usernameVariable: 'DOCKER_REGISTRY_USER')]) {
                        dockerUtils.login(DOCKER_REGISTRY_USER, DOCKER_REGISTRY_PWD)
                        dockerUtils.pushImages(tctctoeImages)
                    }
                }
            }
        }
    }
    post{
        always{
            script{
                println('Cleaning up the build environment..........................')
                dir('WEB_Game'){
                    sh 'docker compose down'
                }
                dockerUtils.removeImages(["danielpenado/tctctoe-api", "danielpenado/tctctoe-ui"])
                dockerUtils.logout()
            }
        }
    }
}