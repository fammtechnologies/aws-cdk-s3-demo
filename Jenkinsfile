pipeline {

    agent any

    options {
        timestamps()
        ansiColor('xterm')
        disableConcurrentBuilds()
    }

    parameters {

        string(
            name: 'BRANCH_NAME',
            defaultValue: 'feature/s3-deployment',
            description: 'GitHub Branch Name'
        )

        choice(
            name: 'ENVIRONMENT',
            choices: ['dev', 'qa', 'prod'],
            description: 'Deployment Environment'
        )

        string(
            name: 'AWS_REGION',
            defaultValue: 'us-east-1',
            description: 'AWS Region'
        )

    }

    environment {

        AWS_DEFAULT_REGION = "${params.AWS_REGION}"

    }

    stages {

        stage('Checkout Source') {

            steps {

                checkout([
                    $class: 'GitSCM',
                    branches: [[name: "*/${params.BRANCH_NAME}"]],
                    userRemoteConfigs: [[
                        url: 'https://github.com/fammtechnologies/aws-cdk-s3-demo.git',
                        credentialsId: 'github-pat'
                    ]]
                ])

            }

        }

        stage('Environment Information') {

            steps {

                sh '''
                    echo "========================================"
                    echo "Workspace Information"
                    echo "========================================"

                    pwd
                    ls -la

                    echo ""

                    echo "Python Version"
                    python3 --version

                    echo ""

                    echo "PIP Version"
                    pip3 --version

                    echo ""

                    echo "Node Version"
                    node --version

                    echo ""

                    echo "NPM Version"
                    npm --version

                    echo ""

                    echo "AWS CLI Version"
                    aws --version

                    echo ""

                    echo "CDK Version"
                    cdk --version
                '''

            }

        }

        stage('Create Python Virtual Environment') {

            steps {

                sh '''
                    python3 -m venv .venv
                '''

            }

        }

        stage('Install Python Dependencies') {

            steps {

                sh '''
                    . .venv/bin/activate

                    python -m pip install --upgrade pip

                    pip install -r requirements.txt
                '''

            }

        }

        stage('Verify AWS Authentication') {

            steps {

                sh '''
                    aws sts get-caller-identity
                '''

            }

        }

        stage('CDK Bootstrap') {

            steps {

                sh '''
                    . .venv/bin/activate

                    cdk bootstrap
                '''

            }

        }

        stage('CDK Synth') {

            steps {

                sh '''
                    . .venv/bin/activate

                    cdk synth
                '''

            }

        }

        stage('CDK Diff') {

            steps {

                sh '''
                    . .venv/bin/activate

                    cdk diff
                '''

            }

        }

        stage('Deploy Infrastructure') {

            steps {

                sh '''
                    . .venv/bin/activate

                    cdk deploy --require-approval never
                '''

            }

        }

    }

    post {

        always {

            echo "========================================"
            echo "Pipeline Finished"
            echo "========================================"

        }

        success {

            echo "AWS CDK Deployment Successful"

        }

        failure {

            echo "Pipeline Failed"

        }

    }

}
