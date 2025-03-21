## Instructions for the Course
In this course we are going to use **Google cloud Services** below I'm sharing step-to-step of how to setup the enviroment for the course.

Remember: Terminal in windows means GitBash.

### Check the video and what we are going to accomplish
[![](https://markdown-videos-api.jorgenkh.no/youtube/ae-CV2KfoN0)](https://youtu.be/ae-CV2KfoN0&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=14)

* Generating SSH keys
* Creating a virtual machine on GCP
* Connecting to the VM with SSH
* Installing Anaconda
* Installing Docker
* Creating SSH `config` file
* Accessing the remote machine with VS Code and SSH remote
* Installing docker-compose
* Installing pgcli
* Port-forwarding with VS code: connecting to pgAdmin and Jupyter from the local computer
* Installing Terraform
* Using `sftp` for putting the credentials to the remote machine
* Shutting down and removing the instance
Want in video? Check 

### Step-by-Step with Tips
- Set up SSH keys to access VM's [Documentation](https://cloud.google.com/compute/docs/connect/create-ssh-keys)
    * Open terminal and navigate using ```cd .ssh/ ```
    * Create your keys using: ``` ssh-keygen -t rsa -f gcp -C USERNAME ``` where gcp means the filename.
    * Upload to the GCP into -> Compute Engine -> Settings/Metadata (LEFT PANNEL) -> Tab SSH KEYS -> Add SSH Keys
    * You can print the .pub key using ``` cat gcp.pub``` copy and paste on the input on the page to add the Key.

After you done this, every VM you create gonna inherit the SSH keys.

- Running the First Instance
    * Go to Compute Engine -> VM instances -> Create Instance
    ```
    Name: **Name of your Instance***
    Region: **Choose the region closest to your location**
    Zone: **Choose Any or One of the options**
    Machine Type: **E2-standard-4 (4 vCPU, 16GB memory)

    OS & Storage:
    Change the OS to Ubuntu -> Ubuntu 20.04 LTS
    ```
    * **HIT CREATE**

- Connecting via SSH
    * Once the Machine is running, check if you got a External IP and copy it.
    * Go to a Terminal and Type: ```ssh -i ~/.ssh/gcp USERNAME@IP ```
    * If you got Denied or some error: Check the name of the file in the .ssh folder and SSH key you added onto metadata.

- Configuring the VM Instance That its running
    * Start by downloading Anaconda: (02-2015) ``` wget https://repo.anaconda.com/archive/Anaconda3-2024.10-1-Linux-x86_64.sh ```
    * After this Run: ``` bash Anaconda3-2024.10-1-Linux-x86_64.sh ``` and follow the instructions
    * No need to change the Path Location.
    * At the end type YES for intialize Anaconda
    * After finishing press ```Ctrl+D or Command+D``` to exit and close the terminal

- We can config a better way to connect into the VM/Server.
    * Open a terminal window and run ``` cd .ssh/ ```
    * Create a blank file named config with: ``` touch config ```
    * You can open that on the editor into vscode using: ``` code config ```
    * Copy and Edit the following:
    ```
    Host de-zoomcamp
        HostName $YOUR_VM_EXTERNAL_IP$
        User $USER_FOR_SSH_KEY$
        IdentityFile $AbsolutePathForFile$ (Eg: ~/.ssh/gcp - c:/Users/MyUser/.ssh/gcp)
    ```
After this you can quickly connect using: ``` ssh de-zoomcamp ```

- Checking the progress
    * Open a terminal window and run the last command ``` ssh de-zoomcamp ```
    * If you got ``` (base) $youruser$@de-zoomcamp:~$ ``` You've successfully installed the Anaconda
    * You can check if the python got right as well with ``` which python ``` or python --version

- Installing Docker
    * Connected to the machine run the following ``` sudo apt-get update ``` to Update package list.
    * Once finished you can run: ``` sudo apt-get install docker.io ```
    * You can try to run ``` docker run hello-world ``` and probably will fail.
    * You gonna need check how to run docker commands without sudo [GitHubLink](https://github.com/sindresorhus/guides/blob/main/docker-without-sudo.md)

- Installing Docker-Compose
    * Go to Github Official Docker/compose releases page and get the latest [GitHub](https://github.com/docker/compose/releases)
    * Search for the one option with **docker-compose-linux-x86_64** and copy the link
    * Go to your VM machine via Terminal and let's create the bin folder with ``` cd ~ ``` and then ``` mkdir bin ```
    * Enter the folder ``` cd bin ``` and download the file with ``` wget $LINK_COPIED$ -O docker-compose```
    * Lets make sure its a Executable file running ``` chmod +x docker-compose ```
    * You can check with ``` ./docker-compose version ```

- Adding Docker-Compose on the PATH variable:
    * We need to edit the bashrc file using ``` nano .bashrc ```
    * In the end of the file add: ``` export PATH="${HOME}/bin:${PATH}"
    * Press ``` CTRL+O ``` to save and hit Enter to confirm ``` CTRL+X ``` for exit
    * Logout and login again into the machbine and check if you just type ``` docker-compose version ``` if you got response

- Preparing VSCODE to VM
    * Go to your VSCODE and Extensions search for **Remote - SSH** it's a package from Microsoft
    * On the bottom bar you should have on the far left A simbol that looks like >< Look for:
    * **Connect to Host...               REMOTE-SSH**
    * If you did everything until this point you gonna see the **de-zoomcamp** option.
    * Select and you will open the vscode into the Remote Machine.

- PGCLI
    * You can try to install using ``` pip install pgcli``` but probably you gonna get error messages
    * Alexey shared a few hints: ``` conda install -c conda-forge pgcli ``` use conda to install
    * After this install a lib called mycli ``` pip install -U mycli ``` if you did this correctly it will work fine

**Here on foward I'm taking my own steps to Run using my own configuration and Projects.**
- Clone your Repository into the machine
    * Go to your Github and grab the link by HTTPS to clone into the remote machine using ``` git clone ```
    * I'm doing this because I want to start my docker-compose already created in the previous steps
    * After cloned I've just run a ``` docker-compose up ``` to start things up

- Port Foward to local Machine
    * In the VSCode Open the **Terminal** and make sure that everything is running with docker ps
    * Go to the **Ports** tab and foward the port 5432
    * You can open a new Local terminal and try to connect using ```pgcli -h localhost -U root -d ny_taxi ```
- Insert the data into the Postgres
    * I've Inserted the yellow_taxi_data and zones data
    * Tips - Build the docker image first, in the docker compose remove double quotes(") for user/password/database name

- Installing Terraform
    * Go to terraform page [Terraform](https://terraform.io/downloads)
    * Copy the link for Amd64
    * Make sure you have unzip installed with ``` sudo apt-get install unzip ```
    * Run ```unzip terraform_1.10.5_linux_amd64.zip ```and you can run ```rm terraform_1.10.5_linux_amd64.zip``` to remove the zipped file

- Credentials
    * We can copy to our server the credentials.json we've used in the past using sftp
    * Navigate in the terminal to the key folder where you have the credentials.json
    * Run ``` sftp de-zoomcamp ``` create a new folder named .gc with ``` mkdir .gc ``` and navigate to it
    * Use ``` put credentials.json ``` in order to send from your local machine to the VM machine the credentials file

- Configuration
    * Let's Set-up the config of gcloud auth
    * Export the file location to a variable like ``` export GOOGLE_APLICATION_CREDENTIALS=~/.gc/credentials.json ```
    * Use this to autenticate with the key file ``` gcloud auth activate-service-account --key-file $GOOGLE_APLICATION_CREDENTIALS ```
    * If the credentials are Ok and you did everything right run ``` terraform init ```