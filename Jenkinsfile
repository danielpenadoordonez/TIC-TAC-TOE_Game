if (env.BRANCH_NAME == "master" || env.BRANCH_NAME == "main"){
    properties([
        pipelineTriggers([
            pollSCM("*/5 * * * *")
        ])
    ])
}

pipeline { 
    agent any

    stages {
        stage('Build') {
            steps{
                echo 'Building Tic-Tac-Toe game................'
                sh 'ls'    
            }
        }
        stage('Test'){
            steps{
                echo 'Testing Tic-Tac-Toe game....................'    
            }
        }
        stage('Deploy'){
            steps{
                echo 'Deploying Tic-Tac-Toe game...................'    
            }
        }
    }
}