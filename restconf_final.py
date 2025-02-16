import json
import requests
requests.packages.urllib3.disable_warnings()

# Router IP Address is 10.0.15.181-184
api_url = "https://10.0.15.181/restconf" # Add

# the RESTCONF HTTP headers, including the Accept and Content-Type
# Two YANG data formats (JSON and XML) work with RESTCONF 
headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
} # Add
basicauth = ("admin", "cisco")

def create():
    yangConfig = {
        "ietf-interfaces:interface": {
            "name": "Loopback65070076",
            "description": "created loopback by RESTCONF",
            "type": "iana-if-type:softwareLoopback",
            "enabled": True,
            "ietf-ip:ipv4": {
                "address": [
                    {
                        "ip": "172.30.76.1",
                        "netmask": "255.255.255.0"
                    }
                ]
            },
            "ietf-ip:ipv6": {}
        }
    } # Add

    resp = requests.put(
        api_url + "/data/ietf-interfaces:interfaces/interface=Loopback65070076", # Add
        data=json.dumps(yangConfig), # Add
        auth=basicauth, 
        headers=headers, # Add 
        verify=False
        )

    if(resp.status_code == 204):
        return "Cannot create: Interface loopback 65070076" # Add
    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface Loopback65070076 created."
    else:
        print('Error. Status Code: {}'.format(resp.status_code))


def delete():
    resp = requests.delete(
        api_url + "/data/ietf-interfaces:interfaces/interface=Loopback65070076", # Add
        auth=basicauth, 
        headers=headers, # Add
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface Loopback65070076 deleted."
    else:
        print('Error. Status Code: {}'.format(resp.status_code))
        return "Cannot delete: Interface loopback 65070076" # Add


def enable():
    yangConfig = {
        "ietf-interfaces:interface": {
            "name": "Loopback65070076",
            "type": "iana-if-type:softwareLoopback",
            "enabled": True,
        } # Add
    }

    resp = requests.patch(
        api_url + "/data/ietf-interfaces:interfaces/interface=Loopback65070076", # Add
        data=json.dumps(yangConfig), # Add
        auth=basicauth, 
        headers=headers, # Add
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface loopback 65070076x is enabled successfully" # Add
    else:
        print('Error. Status Code: {}'.format(resp.status_code))
        return "Cannot enable: Interface loopback 65070076" # Add
        


def disable():
    yangConfig = {
        "ietf-interfaces:interface": {
            "name": "Loopback65070076",
            "type": "iana-if-type:softwareLoopback",
            "enabled": False,
        } # Add
    }

    resp = requests.patch(
        api_url + "/data/ietf-interfaces:interfaces/interface=Loopback65070076", # Add
        data=json.dumps(yangConfig), # Add
        auth=basicauth, 
        headers=headers, # Add
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface loopback 65070104 is disabled" # Add
    else:
        print('Error. Status Code: {}'.format(resp.status_code))
        return "Cannot shutdown: Interface loopback 65070104" # Add


def status():

    resp = requests.get(
        url=api_url+"/data/ietf-interfaces:interfaces-state/interface=Loopback65070076", # Add
        auth=basicauth, 
        headers=headers, # Add
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        response_json = resp.json()
        # test = json.dumps(response_json, indent=4)
        # return test
        
        admin_status = response_json["ietf-interfaces:interface"]["admin-status"]
        oper_status = response_json["ietf-interfaces:interface"]["oper-status"]
        if admin_status == 'up' and oper_status == 'up':
            return "Interface loopback 65070076 is enabled"
        elif admin_status == 'down' and oper_status == 'down':
            return "Interface loopback 65070076 is disabled"
    elif(resp.status_code == 404):
        print("STATUS NOT FOUND: {}".format(resp.status_code))
        return "No Interface loopback 65070076"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))


