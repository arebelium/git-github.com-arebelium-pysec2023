# Exercise 1
1. **Install Python 2.7** <br>

Version 2.7 downloaded and installed manually (for Windows) from this link: [Python 2.7.0.](https://www.python.org/downloads/release/python-270/)

2. **Install Python 3.x** <br>

Version 3.11 was already installed. <br>
Version 3.10 downloaded and installed manually (for Windows) from this link: [Python 3.10.0.](https://www.python.org/downloads/release/python-3100/) <br><br>
In Git Bash terminal it is possible to see all installed versions by running the following command:
```bash
$ py --list
 -V:3.11 *        Python 3.11 (64-bit)
 -V:3.10          Python 3.10 (64-bit)
 -V:2.7
```
3. **Demonstrate how to switch between different versions of Python** <br>

Use the following commands in Git Bash terminal to switch between the versions:
```bash
$ py -2.7 --version
Python 2.7

$ py -3.10 --version
Python 3.10.0

$ py -3.11 --version
Python 3.11.5
```

# Exercise 2
1. **Explore Virtualenv in Python** <br>

Create venv:
```bash
$ python -m venv [venv_name]
```
Activate venv:
```bash
$ source [venv_name]/Scripts/activate
```
2. **Demonstrate the use of PIP having different libraries in each of python virtual environments**
```bash
$ py -3.11 venv3.11/Scripts/pip.exe freeze
certifi==2023.7.22
charset-normalizer==3.2.0
idna==3.4
requests==2.31.0
urllib3==2.0.4

$ py -3.10 venv3.10/Scripts/pip.exe freeze
beautifulsoup4==4.12.2
certifi==2023.7.22
charset-normalizer==3.2.0
google==3.0.0
google-search==1.1.1
idna==3.4
lxml==4.9.3
py-bing-search==0.2.6
pygoogle==0.6
requests==2.31.0
soupsieve==2.5
urllib3==2.0.4
```