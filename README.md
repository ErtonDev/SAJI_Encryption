# SAJI_Encryption
[![Python 3.6](https://img.shields.io/badge/python-3.9-yellow.svg)](https://www.python.org/)
[![Build](https://img.shields.io/badge/Supported_OS-Linux-orange.svg)]()
[![Build](https://img.shields.io/badge/Supported_OS-Windows-orange.svg)]()

Simple text encryption software in spanish. (*I am looking forward to adding more languages in the future*)

<p align="center">
  <img src="https://raw.githubusercontent.com/ErtonDev/SAJI_Encryption/main/resources/logo.png" alt="drawing" width="400"/>
</p>

> SAJI logo

## Resources
SAJI uses the following modules:
 - PyQt5 https://pypi.org/project/PyQt5/
 - pathlib https://pypi.org/project/pathlib/
 - string *(Installed by default)*
 - io *(Installed by default)*

Make sure to have them installed on your computer.

## Execution
`gui.py` is the file responsible for the display of the user interface. It also imports important functions from `main.py`.
```python
# gui.py
from main import encryption, decryption
```

```python
# main.py
def encryption(text):
  ...
  # where text is the user input
  
def decryption(text):
  ...
  # same
```

<p align="center">
  <img src="https://raw.githubusercontent.com/ErtonDev/SAJI_Encryption/main/resources/Encriptación SAJI_001.png" alt="drawing"/>
</p>

> SAJI executed on Linux OS in spanish.

To execute the script type the following command in your terminal:
```
gui.py
```
or
```
python gui.py
```
In case you have an especific version of python, type:
```
python3 gui.py          or          python2 gui.py          --- (Depending on your version)
```
