## What are in the [ICWS (Interaction Center Web Services)](https://help.genesys.com/developer/cic/docs/icws/webhelp/conceptualcontent/welcome.htm) code snippets?
***How to:***
- connect to [PureConnect Premise](Scripts/Connect%20to%20PureConnect%20Premise.py) and [PureConnect Cloud via Internet](Scripts/Connect%20to%20PureConnect%20Cloud%20via%20Internet.py)
- generate list of [users]() / workgroups / roles / skills / wrap-up codes & category
- generate list of users to licenses / licenses to users / workgroups to users / users to workgroups / roles to users / users to roles
- send a Custom Notification to handlers and how to recive a Custom Notification from handlers
- get and update IC user status
- get and update System parameters / Server parameters / Structured parameters
- get a set of attributes from an interaction / update the set of attributes on an interaction
- get and set workgroup activations for a single user
- get the details for a phone number
- start / stop / pause / resume all screen recordings for the specified user
- start / pause interaction record state
- send DTMF digits to an interaction
- hold / mute / pause / secure pause / disconnect specified interaction
- plays a wave file to the call

## Prerequisites
- ICWS SDK license ([I3_FEATURE_ICWS_SDK](https://help.genesys.com/pureconnect/mergedProjects/wh_tr/mergedProjects/wh_tr_icws_sdk_icg/desktop/what_is_the_icws_sdk.htm)) for your PureConnect environment;
- IC user account credentials with appropriate rights & licenses;
- [Python 3.5+](https://www.python.org/downloads/) version with any Python IDE (I prefer [PyCharm](https://www.jetbrains.com/pycharm/download/));

## How to setup your environment
- Download & install Python 3.5+ https://www.python.org/downloads
- Within your Python terminal install "requests" module - ```pip install requests``` - more info about the module - https://pypi.org/project/requests
- Use one of the following ICWS connection methods based on your PureConnect enviromnet:
  - for [PureConnect Premise](Scripts/Connect%20to%20PureConnect%20Premise.py)
  - for [PureConnect Cloud via Internet](Scripts/Connect%20to%20PureConnect%20Cloud%20via%20Internet.py) 

Feel free to reach out to me with any questions, I do love a good coding challenge :v:

> **This project/work is my own and is in no way associated/attributed to any current or former employer.**
