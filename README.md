## What are in the [ICWS (Interaction Center Web Services)](https://help.genesys.com/developer/cic/docs/icws/webhelp/conceptualcontent/welcome.htm) code snippets?
***How to:***
- connect to [PureConnect On-Premise](scripts/icws_premise_authentication.py) / [PureConnect Cloud via Internet](scripts/icws_cloud_authentication.py) environment (switchover supported)
- generate a .csv document with [IC users](scripts/icws_csv_data_export.py#L7) / [workgroups](scripts/icws_csv_data_export.py#L25) / [roles](scripts/icws_csv_data_export.py#L43) / [skills](scripts/icws_csv_data_export.py#L61) / [wrap-up codes](scripts/icws_csv_data_export.py#L79) / [wrap-up categories](scripts/icws_csv_data_export.py#L97)
- generate a .csv document with [users to licenses](scripts/icws_csv_user_to_licenses.py) / [workgroups to users]() / [users to workgroups]() / [roles to users]() / [users to roles]()
- generate a .csv document with [workgroups details]()
- [subscribe to Custom Notification](scripts/icws_subscribe_send_receive_a_custom_notification.py#L7)  / [send a Custom Notification](scripts/icws_subscribe_send_receive_a_custom_notification.py#L22) / [receive a Custom Notification](scripts/icws_subscribe_send_receive_a_custom_notification.py#L36)
- [get a specific IC user status](scripts/icws_user_status.py#L9) / [update a specific IC user status](scripts/icws_user_status.py#L15) / [retrieving a list of all IC users statuses](scripts/icws_user_status.py#L24)
- [retrive system parameter]() / [set system parameter]() / [retrive server parameter]() / [set server parameter]() / [retrive structured parameter]() / [set structured parameter]()
- [get a set of attributes from an interaction](scripts/icws_get_update_attributes.py#L10) / [update the set of attributes on an interaction](scripts/icws_get_update_attributes.py#L18)
- [get a workgroup activations for a single user](scripts/icws_workgroup_activations.py#L7) / [set workgroup activations for a single user](scripts/icws_workgroup_activations.py#L13)
- [get the details for a phone number](scripts/icws_phone_number_details.py)
- [start]() / [stop]() / [pause]() / [resume]() all screen recordings for the specified user
- [start]() / [pause]() interaction record state
- [hold](scripts/icws_interaction_manipulation.py#L10) / [mute](scripts/icws_interaction_manipulation.py#L19) / [pause](scripts/icws_interaction_manipulation.py#L28) / [record](scripts/icws_interaction_manipulation.py#L37) / [send to voicemail](scripts/icws_interaction_manipulation.py#L49) / [send DTMF digits to an interaction](scripts/icws_interaction_manipulation.py#L57) / [pickup](scripts/icws_interaction_manipulation.py#L66) / [disconnect](scripts/icws_interaction_manipulation.py#L74) specified interaction
- [plays a wave file to the call]()
- [send an email](scripts/icws_send_an_email.py)

***Useful Scripts:***
- [generate .csv file with IC user data](scripts/icws_user_data_csv_export.py) (following data is provided: ic username, display name, workgroups, roles, license active, client access, media level, list of additional licenses, auto answer acd interactions, auto answer non-acd interactions, nt domain username, current ic status, department, title, email address, extension, password policies, skills with utilization & proficiency, date ic account created)
- [pass and retrive data between Python application and PureConnect server](scripts/icws_subscribe_send_receive_a_custom_notification.py)

## Prerequisites
- ICWS SDK license ([I3_FEATURE_ICWS_SDK](https://help.genesys.com/pureconnect/mergedProjects/wh_tr/mergedProjects/wh_tr_icws_sdk_icg/desktop/what_is_the_icws_sdk.htm)) for your PureConnect environment
- [Python 3.5+](https://www.python.org/downloads/) version with any Python IDE (I prefer [PyCharm](https://www.jetbrains.com/pycharm/download/))
- Based on your PureConnect environment, you will need to add ```ic_server```, ```ic_username```, ```ic_password```, ```friendlyname``` (for Cloud), ```ic_application_name``` parameters to [icws_cloud_authentication.py](scripts/icws_cloud_authentication.py) or [icws_premise_authentication.py](scripts/icws_premise_authentication.py) file

## How to setup your environment
- Download & install [Python 3.5+](https://www.python.org/downloads/)
- Within your Python terminal install "requests" module - ```pip install requests``` - more info about the module - https://pypi.org/project/requests
- Use one of the following ICWS connection methods based on your PureConnect enviromnet:
  - for [PureConnect On-Premise](scripts/icws_premise_authentication.py)
  - for [PureConnect Cloud via Internet](scripts/icws_cloud_authentication.py) 

Feel free to reach out to me with any questions, I do love a good coding challenge :v:

> **This project/work is my own and is in no way associated/attributed to any current or former employer. See [license file](LICENSE) regarding permissions, limitations, and  conditions. I do advise testing any of the provided scripts in a DEV or non-PROD environment first before running it in a PROD environment. For some large output-file base scripts it is better to run them outside of the peak hours.**
