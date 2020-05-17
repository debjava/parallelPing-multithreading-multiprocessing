# Ping IP address parallely using Python  Multiprocessing and Multithreading

## Python Version

`py -V` or `python -V`

current python version: **3.7.4**

## How to create a virtual environment

syntax is `py -m venv` <enviornment name>

In this case, the example is given below.

* Step 1: Execute the command using `py -m venv env`

* Step 2: Activate using the command `.\env\Scripts\activate`

* Step 3: Verify using the command `where python`

## Install dependencies in Virtual environment

### Ensure proper version of PIP
In the virtual environment use the following command,

`pip list`

After executing, you may get the following details.

>(env) E:\pydev-1-2020\projectDependencyInstall>pip list
Package    Version
---------- -------
pip        19.0.3
setuptools 40.8.0
You are using pip version 19.0.3, however version 20.0.2 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.
>

### Upgrade PIP version
Execute the following command to upgrade to higher version of pip.

`py -m pip install --upgrade pip`

or

`python -m pip install --upgrade pip`

### Final step to install dependencies

After activating the virtual environment, execute the following command

`pip install -e .`

or

`pip install .`

### How to run

In Eclipse or Pycharm, run the file `Main.py`


### Performance Benchmark

**For 50 IP Addresses, parallel execution using Python Multi Processing and Multireading **

Multi-Processing Pool Size = 200, Total Time Taken:  13.2449947  seconds

Multi-Thread Pool Size = 300, Total Time Taken:  4.3145787  seconds


**For 50 IP Addresses, sequential execution using Python**

Total Time Taken:  163.009457  seconds
