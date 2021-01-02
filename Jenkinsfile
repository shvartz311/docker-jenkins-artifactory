pipeline
{
    agent {dockerfile true}
        //dockerfile { true }
        //label 'zip-job-docker'
        //additionalBuildArgs  '--privileged --build-arg version=1.2.0'
        //docker {
        //    label 'zip-job-docker'
        //    args  '-e VERSION=1.2.0 --privileged'
 // Equivalent to "docker build -f Dockerfile.build --build-arg version=1.0.2 ./build/
    // docker build -t example -f Dockerfile .
    stages
    {
        stage('Build stage - Run script')
        {
            steps
            {
                script
                {          
                    sh "python /tmp/zip_job.py"
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