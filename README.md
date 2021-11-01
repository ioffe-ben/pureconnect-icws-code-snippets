# List of [ICWS](https://help.genesys.com/developer/cic/docs/icws/webhelp/conceptualcontent/welcome.htm) (Interaction Center Web Services) Code Snippets
[desription]

## What are in the snippets?
- Generate list of [users](User%20List/script.py) / [workgroups](User%20List/script.py) / [roles](User%20List/script.py);
- Generate list of roles to users, users to roles

## Prerequisites
- ICWS SDK license (I3_FEATURE_ICWS_SDK) for your PureConnect environment;
- IC user account credentials with appropriate rights & licenses;
- Python 3.5+ version with any Python IDE (I prefer PyCharm);

## How to setup your environment
- Download & install Python 3.5+ - https://www.python.org/downloads/
- Within your Python terminal install "requests" module - ```pip install requests``` - more info about the module - https://pypi.org/project/requests/
- Use following ICWS connection method based on your PureConnect enviromnet:
  - [PureConnect Premise] (Scripts/Connect to PureConnect Premise.py)
  - [PureConnect Cloud via Internet] (Scripts/Connect to PureConnect Cloud via Internet.py)

> **This project/work is my own and is in no way associated/attributed to any current or former employer.**
