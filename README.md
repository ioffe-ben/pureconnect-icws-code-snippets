## What are in the [ICWS (Interaction Center Web Services)](https://help.genesys.com/developer/cic/docs/icws/webhelp/conceptualcontent/welcome.htm) code snippets?
***How to:***
- connect to [PureConnect On-Premise](scripts/icws_premise_authentication.py) / [PureConnect Cloud via Internet](scripts/icws_cloud_authentication.py) environment
- generate list of [users]() / [workgroups]() / [roles]() / [skills]() / [wrap-up codes & category]() / [status messages]()
- generate list of [users to licenses]() / [licenses to users]() / [workgroups to users]() / [users to workgroups]() / [roles to users]() / [users to roles]()
- [subscribe to Custom Notification]()  / [send a Custom Notification]() / [receive a Custom Notification]()
- [get a specific IC user status](scripts/icws_user_status.py#L9) / [update a specific IC user status](scripts/icws_user_status.py#L15) / [retrieving a list of all IC users statuses](scripts/icws_user_status.py#L24)
- [retrive system parameter]() / [set system parameter]() / [retrive server parameter]() / [set server parameter]() / [retrive structured parameter]() / [set structured parameter]()
- [get a set of attributes from an interaction]() / [update the set of attributes on an interaction]()
- [get workgroup activations for a single user]() / [set workgroup activations for a single user]()
- [get the details for a phone number]()
- [start]() / [stop]() / [pause]() / [resume]() all screen recordings for the specified user
- [start]() / [pause]() interaction record state
- [send DTMF digits to an interaction]()
- [hold]() / [mute]() / [pause]() / [secure pause]() / [disconnect]() specified interaction
- [plays a wave file to the call]()
- [send an email](scripts/icws_send_an_email.py)

***Useful Scripts:***
- [generate .csv file with IC user data](scripts/icws_user_data_csv_export.py) (following data is provided: ic username, display name, workgroups, roles, license active, client access, media level, list of additional licenses, auto answer acd interactions, auto answer non-acd interactions, nt domain username, current ic status, department, title, email address, extension, password policies, skills with utilization & proficiency, date ic account created)

## Prerequisites
- ICWS SDK license ([I3_FEATURE_ICWS_SDK](https://help.genesys.com/pureconnect/mergedProjects/wh_tr/mergedProjects/wh_tr_icws_sdk_icg/desktop/what_is_the_icws_sdk.htm)) for your PureConnect environment
- IC user account credentials with appropriate rights & licenses
- [Python 3.5+](https://www.python.org/downloads/) version with any Python IDE (I prefer [PyCharm](https://www.jetbrains.com/pycharm/download/))

## How to setup your environment
- Download & install [Python 3.5+](https://www.python.org/downloads/)
- Within your Python terminal install "requests" module - ```pip install requests``` - more info about the module - https://pypi.org/project/requests
- Use one of the following ICWS connection methods based on your PureConnect enviromnet:
  - for [PureConnect On-Premise](scripts/icws_premise_authentication.py)
  - for [PureConnect Cloud via Internet](scripts/icws_cloud_authentication.py) 

Feel free to reach out to me with any questions, I do love a good coding challenge :v:

> **This project/work is my own and is in no way associated/attributed to any current or former employer. See [license file](LICENSE) regarding permissions, limitations, and  conditions. I do advise testing any of the provided scripts in a DEV or non-PROD environment first before running it in a PROD environment. For some large output-file base scripts it is better to run them outside of the peak hours.**
