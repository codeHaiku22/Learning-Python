# Python Environments
Python allows the ability to create virtual environments which are a containerized approach to projects.  These environments allow the developer to create a lean environment which only uses the packages needed by the project. 

*__Note:__ Virtual environments are transier and temporary in nature.  They should not be used to contain actual project files or code files.  They simply are a storage space for dependencies and a means to emulate a different envrionment of Python.*

## Python Versions
For the purposes of this document, Python 2.7 was also installed alongside the pre-existing Python 3.8.

```bash
$ sudo apt install python2.7

$ cd /usr/bin

$ ls -l python*
python2.7  python3  python3-config  python3.8  python3.8-config
```

## Python-is-Python3
Creates a symlink: /usr/bin/python to python3 
This makes it so you don't have to type `python3` to run python commands and can simply type `python` instead.

```bash
$ sudo apt install python-is-python3
```

## pip - pip Installs Packages

If it doesn't already exist, install `pip` (pip installs pakages).
```bash
$ sudo apt install python3-pip
```

To confirm proper installation, check the version of `pip`.

```bash
$ pip3 --version
pip 20.0.2 from /usr/lib/python3/dist-packages/pip (python 3.8)

$ which pip3
/usr/bin/pip3
```
## virtualenv
Separates different Python environments for different projects.

Now, install virtualenv
```bash
$ pip3 install virtualenv
```

## Display Global Site Packages 
Use the `pip` command To display all pre-installed global Python packages.

```bash
$ pip3 list

Package                Version
---------------------- --------------------
appdirs                1.4.4
attrs                  19.3.0
Automat                0.8.0
blinker                1.4
camelcase              0.2
...
wheel                  0.34.2
zipp                   1.0.0
zope.interface         4.7.1
```

## Create a New Python Environment
Let's use `virtualenv` to make a new Python environment.

First, let's make a directory for the Python environments and navigte to the newly created directory.

```bash
$ mkdir python_environments

$ cd !$
```

Now, let's create a directory for a project using `virtualenv`.

```bash
$ python3 -m virtualenv project1_env

created virtual environment CPython3.8.5.final.0-64 in 3691ms
  creator CPython3Posix(dest=/mnt/c/python_environments/project1_env, clear=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/home/dgrewal/.local/share/virtualenv)
    added seed packages: pip==20.2.4, setuptools==50.3.2, wheel==0.35.1
  activators BashActivator,CShellActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator
```

*__Note:__ To create a virtual environment will all of the packages available within the global site, add the parameter --system-site-packages to the end of the command issued above.*

If we go list the contents of the directory, we can see that there are some files and subdirectories that have been created there.

```bash
$ ls -l project1_env

bin  lib  pyvenv.cfg
```

## Activate Python Environment
To activate this environment use the `source` command and call the `project1_env/bin/activate` command.

*__Note:__ Once activated, the project directory name will prefix the prompt to indicate the currently active environment/project.*

```bash
$ source project1_env/bin/activate

(project1_env)$
```

To confirm, we can use the `which` command to determine the location for `python` and `pip`.

```bash
(project1_env)$ which python

/mnt/c/python_environments/project1_env/bin/python

(project1_env)$ which pip

/mnt/c/python_environments/project1_env/bin/pip
```

## Display Local Packages 
This new environment contains the minimum set of packages.

```bash
(project1_env)$ pip list

Package    Version
---------- -------
pip        20.2.4
setuptools 50.3.2
wheel      0.35.1
```

## Install Packages into Environment
Now, we can install packages into this environment.

*__Note__ Packages which do not exist on the local system will be downloaded and installed automatically.  Whereas those packages which do exist are installed directly.*

```bash
(project1_env)$ pip install numpy

Collecting numpy
  Downloading numpy-1.19.3-cp38-cp38-manylinux2010_x86_64.whl (14.9 MB)
     |████████████████████████████████| 14.9 MB 11.1 MB/s
Installing collected packages: numpy
Successfully installed numpy-1.19.3

(project1_env)$ pip install pytz

Collecting pytz
  Downloading pytz-2020.1-py2.py3-none-any.whl (510 kB)
     |████████████████████████████████| 510 kB 2.6 MB/s
Installing collected packages: pytz
Successfully installed pytz-2020.1

(project1_env)$ pip install camelcase

Processing /home/dgrewal/.cache/pip/wheels/20/1a/a6/5651fe658d5ffd7fcf610723557f7b20a52a71d7e8e1849cb6/camelcase-0.2-py3-none-any.whl
Installing collected packages: camelcase
Successfully installed camelcase-0.2
```

## Document Local Package Manifest
All of these locally imported packages are custom to this project.  They can be documented into a file for portability and transferability.

```bash
(project1_env)$ pip freeze --local > requirements.txt

(project1_env)$ cat requirements.txt

camelcase==0.2
numpy==1.19.3
pytz==2020.1
```

## Deactivate Environment
To exit from and deactivate an environment, the `deactivate` command is used.

```bash
(project1_env)$ deactivate
```

To confirm deactiviation, check the location of python.

```bash
$ which python3

/usr/bin/python3
```

## Delete Environment
Like any other directory, the directory containing the environment can be deleted.

```
$ ls -la

total 0
drwxrwxrwx 1 dgrewal dgrewal 4096 Oct 30 10:53 project1_env
-rwxrwxrwx 1 dgrewal dgrewal   42 Oct 30 11:42 requirements.txt

$ rm -rf project1_env
```

## Create a New Environment by Specifying Python Version
When creating an environment, the version of Python can be specified.  This version must exist and must be installed on the system.

```bash
$ python3 -m virtualenv py27env

created virtual environment CPython3.8.5.final.0-64 in 1112ms
  creator CPython3Posix(dest=/mnt/c/Users/dgrewal/Documents/Projects/Development/python/venv/py27_env, clear=False, global=False)
  seeder FromAppData(download=False, appdirs=latest, CacheControl=latest, certifi=latest, chardet=latest, colorama=latest, contextlib2=latest, distlib=latest, distro=latest, html5lib=latest, idna=latest, ipaddr=latest, lockfile=latest, msgpack=latest, packaging=latest, pep517=latest, pip=latest, pkg_resources=latest, progress=latest, pyparsing=latest, pytoml=latest, requests=latest, retrying=latest, setuptools=latest, six=latest, urllib3=latest, webencodings=latest, wheel=latest, via=copy, app_data_dir=/home/dgrewal/.local/share/virtualenv/seed-app-data/v1.0.1.debian)
  activators BashActivator,CShellActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator

$ python3 -m virtualenv -p /usr/bin/python2.7 py27_env

created virtual environment CPython2.7.18.final.0-64 in 3759ms
  creator CPython2Posix(dest=/mnt/c/Users/dgrewal/Documents/Projects/Development/python/venv/py27_env, clear=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/home/dgrewal/.local/share/virtualenv)
    added seed packages: pip==20.2.4, setuptools==44.1.1, wheel==0.35.1
  activators BashActivator,CShellActivator,FishActivator,PowerShellActivator,PythonActivator
```

### Activate Python Environment
To activate this environment use the `source` command and call the `py27_env/bin/activate` command.

*__Note:__ Once activated, the project directory name will prefix the prompt to indicate the currently active environment/project.*

```bash
$ source py27_env/bin/activate

(py27_env)$
```

To confirm, we can determine the version of python within this environment along with the `which` commands for `python` and `pip`

```bash
(py27_env)$ python --version

Python 2.7.18

(py27_env)$ which python

/mnt/c/python_environments/py27_env/bin/python

(py27_env)$ which pip

/mnt/c/python_environments/py27_env/bin/pip
```

## Install Packages into Environment using Manifest File
Now, we can install packages into this environment using the "requirements.txt" manifest file created earlier.

*__Note:__ Normally, there will be errors and deprecation messages when performing this task especially when an operation such as this is being performed where requirements from a higher/newer version of Python are being brought into an lower/older version of Python.*

```bash
(py27_env)$ pip install -r requirements.txt

Processing /home/dgrewal/.cache/pip/wheels/20/1a/a6/5651fe658d5ffd7fcf610723557f7b20a52a71d7e8e1849cb6/camelcase-0.2-py3-none-any.whl
Collecting numpy==1.19.3
  Using cached numpy-1.19.3-cp38-cp38-manylinux2010_x86_64.whl (14.9 MB)
Collecting pytz==2020.1
  Using cached pytz-2020.1-py2.py3-none-any.whl (510 kB)
Installing collected packages: camelcase, numpy, pytz
Successfully installed camelcase-0.2 numpy-1.19.3 pytz-2020.1
```
### Confirm Installed Packages from Manifest File
This new environment contains the minimum set of packages.

```bash
(py27_env)$ pip list

Package    Version
---------- -------
camelcase  0.2
numpy      1.19.3
pip        20.2.4
pytz       2020.1
setuptools 50.3.2
wheel      0.35.1
```

## Deactivate Environment
To exit from and deactivate an environment, the `deactivate` command is used.

```bash
(py27_env)$ deactivate
```

To confirm deactiviation, check the location f python.

```bash
$ which python3

/usr/bin/python3
```