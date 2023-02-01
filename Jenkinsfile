pipeline {

    agent any
/*
	tools {
        maven "maven3"
    }
*/
    environment {
        registry = "rahulshri0703/doc2"
        registryCredential = 'dockerhub'
    }

    stages{


        stage('Building image') {
            steps{
              script {
                dockerImage = docker.build( registry + ":$BUILD_NUMBER",".")
              }
            }
        }
        
        stage('Deploy Image') {
          steps{
            script {
              docker.withRegistry( '', registryCredential ) {
                dockerImage.push("$BUILD_NUMBER")
                dockerImage.push('latest')
              }
            }
          }
        }

        stage('Remove Unused docker image') {
          steps{
            sh "docker rmi $registry:$BUILD_NUMBER"
          }
        }

        
        stage('Kubernetes Deploy') {
	  agent { label 'KOPS' }
            steps {
                    sh "pwd"
                    sh "ls"
                    sh "helm upgrade --install --force vproifle-stack helm/appcharts --set appimage=${registry}:${BUILD_NUMBER} --namespace prod"
            }
        }

    }


}