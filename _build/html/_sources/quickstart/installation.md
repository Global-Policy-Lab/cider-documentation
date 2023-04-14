## Installation

### Using Poetry
To install, and manage dependencies and virtual environments this project uses Poetry. Follow the [instructions](https://python-poetry.org/docs/) to install Poetry.

From the root directory `poetry update` followed by `poetry install` - this will establish a virtual environment with all the needed dependencies.

Once your virtual environment is made you can use `poetry run [command]` to run a single CLI command inside the virtual environment.

You can use `poetry shell` to enter into the virtual environment.

### Using Pip
Another option is to install dependencies using Pip:

1. Run `pip install .` in the top-level directory to automatically install Cider's dependencies.
2. Add Cider's top-level directory to your PYTHONPATH:

```export PYTHONPATH=$PYTHONPATH:/path/to/cider```

You'll likely want to add this line to your .bashrc, .zshrc, or similar.

### On AWS
The following process should reliably get Cider up and running on a new AWS EC2 Ubuntu instance: 
1. Create AWS EC2 Ubuntu instance. This process should work on any Ubuntu machine, but it has been verified on the current default EC2 Ubuntu AMI (ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-20230325), 64-bit x86, t2.large with 8gb memory
1. ssh into the Ubuntu machine. Substitute the path to your key and the AWS Public IPv4 DNS address into this line and execute in your terminal: `ssh -i "path/key.pem" ubuntu@ec2-xx-xxx-xxx-xxx.us-east-2.compute.amazonaws.com`
1. Execute the following, confirming selections along the way

```
# Clone cider
git clone https://github.com/Global-Policy-Lab/cider.git
cd cider

# Install a version of python compatible with cider
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.9

# Add .local/bin, where scripts will be installed, to PATH
echo 'export PATH="/home/ubuntu/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# Install pip
sudo apt install python3-pip

# Install distutils to manage module installation
sudo apt-get install python3.9-distutils

# Install cider's dependencies
python3.9 -m pip install .

# Install Java
sudo apt install default-jdk

# Point pyspark to python 3.9
echo 'export PYSPARK_PYTHON=python3.9; export PYSPARK_DRIVER_PYTHON=python3.9' >> ~/.bashrc
source ~/.bashrc
```

### On Apple M1
The above may not work on Apple M1 processors due to certain dependencies being unavailable or behaving badly. One option to sidestep this issue is to use [conda](https://docs.conda.io/en/latest/) to create a virtual environment which uses x86 architecture (rather than the ARM64 architecture which Apple's M1 chips use).

[This guide](https://towardsdatascience.com/how-to-manage-conda-environments-on-an-apple-silicon-m1-mac-1e29cb3bad12) contains details on setting up Conda and creating such an environment. Summarized, the steps are as follows:

1. Install conda, likely [Miniconda](https://docs.conda.io/projects/continuumio-conda/en/latest/user-guide/install/)
2. Run the following commands:
```
CONDA_SUBDIR=osx-64 conda create -n my_env_name python=3.8
conda activate my_env_name
conda config --env --set subdir osx-64
```
3. Run `conda install swig`

And then follow either of the installation procedures above from within the environment you just created.