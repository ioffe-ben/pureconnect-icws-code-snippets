## Important notes



icws_cloud_authentication.py
icws_premise_authentication.py

gg
```
<row_variable> = <row_variable> + json_users['items'][i]['configurationId']['id'] + '\n'

with open('<export_file_name>.csv', 'w') as file:
    file.write(<row_variable>)
    file.close()
```
