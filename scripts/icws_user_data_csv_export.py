# Copyright (c) 2021, Ben Ioffe (github.com/ioffe-ben). All rights reserved. Copyrights licensed under the BSD 3-Clause License. See the accompanying LICENSE file for terms.
# Code snippet description: the following snippet shows how generate .csv IC users data document using ICWS API.
import json
import requests
import icws_cloud_authentication # or import icws_premise_authentication for PureConnect Premise (more details: https://github.com/ioffe-ben/pureconnect-icws-code-snippets/blob/main/scripts/icws_premise_authentication.py)

request = requests.get(icws_cloud_authentication.baseURL + icws_cloud_authentication.json_connection_response['sessionId'] + '/configuration/users', headers=icws_cloud_authentication.header, cookies=icws_cloud_authentication.cookie, verify=False)
json_users = json.loads(request.text)

csv_export_string = 'IC Username;' \
                        'Display Name;' \
                        'Extension;' \
                        'NT Domain User;' \
                        'Current IC Status;' \
                        'Date Account Created;' \
                        'License Active;' \
                        'Client Access;' \
                        'Media Level;' \
                        'Additional Licenses;' \
                        'Email Address;' \
                        'Department;' \
                        'Title;' \
                        'Skills (proficiency:desire to use);' \
                        'Workgroups;' \
                        'Roles;' \
                        'Password Policies;' \
                        'Auto Answer ACD Interactions;' \
                        'Auto Answer Non-ACD Interactions;\n'
i = 0

while i < len(json_users['items']):
    request_user_data_all = requests.get(icws_cloud_authentication.baseURL + icws_cloud_authentication.json_connection_response['sessionId'] + '/configuration/users/' + json_users['items'][i]['configurationId']['id'] + '?select=*',headers=icws_cloud_authentication.header, cookies=icws_cloud_authentication.cookie, verify=False)
    json_user_data = json.loads(request_user_data_all.text)

    # IC Username
    ic_username = json_users['items'][i]['configurationId']['id']

    # Display Name
    display_name = json_users['items'][i]['configurationId']['displayName']

    # Workgroups
    if "workgroups" in json_user_data:
        try:
            items = ''
            ii = 0
            while ii < len(json_user_data['workgroups']):
                items += json_user_data['workgroups'][ii]['id'] + ', '
                ii += 1
            workgroup_full_data = items[:-2]
        except:
            workgroup_full_data = '-'
    else:
        workgroup_full_data = '-'

    # Roles
    try:
        if 'roles' in json_user_data:
            try:
                items = ''
                ii = 0
                while ii < len(json_user_data['roles']['effectiveValue']):
                    items += json_user_data['roles']['effectiveValue'][ii]['id'] + ', '
                    ii += 1
                role_full_data = items[:-2]
            except:
                role_full_data = '-'
        else:
            role_full_data = '-'
    except:
        role_full_data = '-'

    # Auto Answer ACD Interactions
    try:
        autoAnswerAcdInteractions = json_user_data['autoAnswerAcdInteractions']
    except:
        autoAnswerAcdInteractions = '-'

    # Auto Answer NON-ACD Interactions
    try:
        autoAnswerNonAcdInteractions = json_user_data['autoAnswerNonAcdInteractions']
    except:
        autoAnswerNonAcdInteractions = '-'

    # NT Domain User
    try:
        ntDomainUser = json_user_data['ntDomainUser']
    except:
        ntDomainUser = '-'

    # Status Text
    try:
        statusText = json_user_data['statusText']
    except:
        statusText = '-'

    # Department Name
    try:
        departmentName = json_user_data['personalInformationProperties']['departmentName']
    except:
        departmentName = '-'

    # Title
    try:
        title = json_user_data['personalInformationProperties']['title']
    except:
        title = '-'

    # Email Address
    try:
        emailAddress = json_user_data['mailboxProperties']['emailAddress']
    except:
        emailAddress = '-'

    # Extension
    try:
        extension = json_user_data['extension']
    except:
        extension = '-'

    # Created Date
    try:
        createdDate = json_user_data['createdDate'][4:6] + '-' + json_user_data['createdDate'][6:8] + '-' + \
                      json_user_data['createdDate'][:4] + ' ' + json_user_data['createdDate'][9:11] + ':' + \
                      json_user_data['createdDate'][11:13] + ':' + json_user_data['createdDate'][13:15]
    except:
        createdDate = '-'

    # Skills
    if "skills" in json_user_data:
        try:
            items = ''
            ii = 0
            if len(json_user_data['skills']['effectiveValue']) > 1:
                while ii < len(json_user_data['skills']['effectiveValue']):
                    items += json_user_data['skills']['effectiveValue'][ii]['id']['displayName'] + ' (' + str(
                        json_user_data['skills']['effectiveValue'][ii]['proficiency']) + ':' + str(
                        json_user_data['skills']['effectiveValue'][ii]['desireToUse']) + '), '
                    ii += 1
                skills = items[:-2]
            if len(json_user_data['skills']['effectiveValue']) == 1:
                skills = json_user_data['skills']['effectiveValue']['id']['displayName'] + ' (' + str(
                    json_user_data['skills']['effectiveValue']['proficiency']) + ':' + str(
                    json_user_data['skills']['effectiveValue']['desireToUse'])
            else:
                skills = '-'
        except:
            skills = '-'
    else:
        skills = '-'

    # Licenses
    try:
        licenses = ''
        ii = 0
        try:
            while ii < len(json_user_data['licenseProperties']['additionalLicenses']):
                licenses += json_user_data['licenseProperties']['additionalLicenses'][ii]['displayName'] + ', '
                ii += 1
        except:
            licenses = '-  '

        try:
            license_full_data = str(json_user_data['licenseProperties']['licenseActive']) + ';' + str(
                json_user_data['licenseProperties']['hasClientAccess']) + ';' + str(
                json_user_data['licenseProperties']['mediaLevel']) + ';' + licenses[:-2]
        except:
            license_full_data = 'no data'
    except:
        license_full_data = '-'

    # Password Policies
    try:
        items = ''
        ii = 0
        if len(json_user_data['passwordPolicies']['effectiveValue']) > 1:
            while ii < len(json_user_data['passwordPolicies']['effectiveValue']):
                items += json_user_data['passwordPolicies']['effectiveValue'][ii]['displayName'] + ', '
                ii += 1
            passwordPolicies = items[:-2]
        if len(json_user_data['passwordPolicies']['effectiveValue']) == 1:
            passwordPolicies = json_user_data['passwordPolicies']['effectiveValue']['displayName']
    except:
        passwordPolicies = '-'

    i += 1

    csv_export_string = csv_export_string + \
                        ic_username + ';' + \
                        display_name + ';' + \
                        extension + ';' + \
                        ntDomainUser + ';' + \
                        statusText + ';' + \
                        createdDate + ';' + \
                        license_full_data + ';' + \
                        emailAddress + ';' + \
                        departmentName + ';' + \
                        title + ';' + \
                        skills + ';' + \
                        workgroup_full_data + ';' + \
                        role_full_data + ';' + \
                        passwordPolicies + ';' + \
                        str(autoAnswerAcdInteractions) + ';' + \
                        str(autoAnswerNonAcdInteractions) + ';\n'
    print(str(i) + ' out of ' + str(len(json_users['items'])) + ' processed')

with open('ic_user_data_export.csv', 'w') as file:
    file.write(csv_export_string)
    file.close()
    print('Export completed, see "ic_user_data_export.csv" file in the same folder as this script')
