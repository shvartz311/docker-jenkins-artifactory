pipeline
{
    agent {
        dockerfile true
        //label 'zip-job-docker'
    }
    stages
    {
        stage ('Artifactory Configuration')
        {
            steps
            {
                rtServer (id: SERVER_ID,  url: "http://172.18.0.4:8082/artifactory", credentialsId: "admin.password")
            }
        }
        stage('Build stage - Run script')
        {
            steps
            {
                script
                {          
                    sh "python3 /tmp/zip_job.py"
                }
            }
        }
        stage('Publish stage - Archive artifacts')
        {
            steps
            {
                archiveArtifacts artifacts: '*.zip', followSymlinks: false
            }
        }
        stage ('Publish build info')
        {
            steps
            {
                rtPublishBuildInfo (serverId: SERVER_ID)
            }
    }
}
}