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

### AWS
The following process should reliably get Cider up and running in Jupyter notebooks on a new AWS EC2 Ubuntu instance:
1. Create AWS EC2 Ubuntu instance. This process should work on any Ubuntu machine, but it has been verified on the current default EC2 Ubuntu AMI (ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-20230325), 64-bit x86, t2.large with 8gb memory
1. ssh into the Ubuntu machine. Substitute the path to your key and the AWS Public IPv4 DNS address into this line and execute in your terminal: `ssh -i "path/key.pem" ubuntu@ec2-xx-xxx-xxx-xxx.us-east-2.compute.amazonaws.com`
1. Execute the following, confirming all prompts along the way:

```
# download and install miniconda
wget https://repo.anaconda.com/miniconda/Miniconda3-py39_23.1.0-1-Linux-x86_64.sh
bash Miniconda3-py39_23.1.0-1-Linux-x86_64.sh
source .bashrc

# Create a conda environment w/ cider-compatible version of python
conda create --name py39 python=3.9
conda deactivate
conda activate py39
conda install nb_conda_kernels

# Install cider
git clone https://github.com/Global-Policy-Lab/cider.git
cd cider

# Install cider's dependencies
pip install .

## Including Java
sudo apt-get update
sudo apt install default-jdk
```

To work in a Jupyter notebook:
- If not in it, activate the conda environment created in script above: `conda activate py39`
- In your ssh session execute: `jupyter notebook --no-browser --port=8888`
- Leave the ssh session running, open a new terminal window, and execute the following, substituting the path to your key and EC2 address, as above: `ssh -i "path/key.pem" -L 8000:localhost:8888 ubuntu@ec2-xx-xxx-xxx-xxx.us-east-2.compute.amazonaws.com`
- Open a browser window and go to `localhost:8000`
	+ If prompted for a token, go back to the first terminal window and copy the token from the end of one of the long URLs that look something like: http://<!-- -->localhost:8888/?token=9a22e1a45e0c1c3a3e89c8fc18448d25ff956d8908140cd6
- In the browser, create a notebook via the "New" menu button and select "Python [conda env:py39]"

### On Apple Silicon (M1, M2, etc.)
The above may not work on Apple processors due to certain dependencies being unavailable or behaving badly. One option to sidestep this issue is to use [conda](https://docs.conda.io/en/latest/) to create a virtual environment which uses x86 architecture (rather than the ARM64 architecture which Apple's M1 chips use).

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