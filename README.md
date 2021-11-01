# List of [ICWS](https://help.genesys.com/developer/cic/docs/icws/webhelp/conceptualcontent/welcome.htm) (Interaction Center Web Services) Code Snippets
[desription]

## What are in the snippets?
- Generate list of [users](User%20List/script.py) / [workgroups](User%20List/script.py) / [roles](User%20List/script.py);
- Generate list of roles to users, users to roles

## Prerequisites
- ICWS SDK license (I3_FEATURE_ICWS_SDK) for your PureConnect environment;
- IC user account credentials with appropriate rights & licenses;
- Python 3.5+ version with any Python IDE (I prefer [PyCharm](https://www.jetbrains.com/pycharm/download/));

## How to setup your environment
- Download & install Python 3.5+ - https://www.python.org/downloads/
- Within your Python terminal install "requests" module - ```pip install requests``` - more info about the module - https://pypi.org/project/requests/
- Use one of the following ICWS connection methods based on your PureConnect enviromnet:
  - for [PureConnect Premise](Scripts/Connect%20to%20PureConnect%20Premise.py)
  - for [PureConnect Cloud via Internet](Scripts/Connect%20to%20PureConnect%20Cloud%20via%20Internet.py) 

> **This project/work is my own and is in no way associated/attributed to any current or former employer.**
