This is an MVP. It works, but doesn't allow any customoization of the API for example. There's no exception handling.

I used the Add-on Builder to create the TA as follows: 
1. Download and unzip the Add-on Builder
1. Start a container with the AoB bind-mounted and create the TA. Make a note of the directory name.

    task: `run initial container with AoB`
1. Copy the TA directory out of the container and into the repo working directory. 

    task: `copy TA from AoB container`
1. Remove the container. *Careful! This will stop and remove any "splunk" container.*

    task: `remove container`
1. Start a new container with a bind mount to the TA
    
    task: `run container`

Edits to the TA are immediately available to Splunk through the bind mount.

Run task `package the app` to create the tarball which will be vetted/installed to Splunk Cloud. You can use Postman/Insomnia, or upload the app directly if you have access to a Splunk Cloud environment.
