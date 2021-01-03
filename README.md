rtUpload (
    serverId: SERVER_ID,
    spec: '''{
          "files": [
            {
              "pattern": "*.zip",
              "target": "example-local-repo/"
            }
         ]
    }''',
 
    // Optional - Associate the uploaded files with the following custom build name and build number,
    // as build artifacts.
    // If not set, the files will be associated with the default build name and build number (i.e the
    // the Jenkins job name and number).
    failNoOp: true,
	buildName: 'holyFrog',
    buildNumber: '42'
)