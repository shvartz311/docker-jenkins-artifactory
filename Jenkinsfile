pipeline
{
    agent {dockerfile true}
    stages
    {
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
    }
}