## Important notes
Based on your PureConnect environment, you will need to add ```ic_server```, ```ic_username```, ```ic_password```, ```ic_application_name```, ```friendlyname``` parameters to [icws_cloud_authentication.py](icws_cloud_authentication.py) or [icws_premise_authentication.py](icws_premise_authentication.py) file.

Pretty much every snippet here starts with ``` import icws_cloud_authentication ``` which is the authentication module to connect to PureConnect Cloud environment; to connect to On-Premise environment use ``` import icws_premise_authentication ``` instead.

You do not have to use authentication module in ```import``` section, you can just copy/pase one of the module code to your script instead. 


gg
```
<row_variable> = <row_variable> + json_users['items'][i]['configurationId']['id'] + '\n'

with open('<export_file_name>.csv', 'w') as file:
    file.write(<row_variable>)
    file.close()
```
