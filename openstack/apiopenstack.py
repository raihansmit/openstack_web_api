import json
import requests
import pprint
import sys

# if len(sys.argv) < 3:
#     print("python apiopenstack.py [arg_image] [arg_flavor] [arg_network]")


# arg_image = sys.argv[1]
# arg_flavor = sys.argv[2]
# arg_network = sys.argv[3]

pp = pprint.PrettyPrinter(indent=4)

flavor = {
    "mini-small": "19f5879e-2416-4640-85bb-81b34ff1aa36", 
    "small": "528d0578-c730-4513-8b6e-4dda3969362a", 
    "medium": "0272e42f-603a-4cfd-82c8-adee9793762c", 
    "large": "3609f96f-571e-41f2-8f0e-899777aad985", 
    "extra-large": "0252a18c-1653-459a-9f21-10e54d3e0f5c"
}

image = {
    "UbuntuJammy_DockerCE": "6a5b8109-98f2-4b75-8ae0-6acb66f44ea9", 
    "Debian09": "e2091610-d902-41e8-9b7a-a5f6cf4f8309", 
    "Debian08": "174caf0a-4bac-4e2c-a57e-634ba0b5fb57", 
    "Centos7": "6fca519d-ef46-4f70-a932-6f5786625d12", 
    "UbuntuJammy": "784af618-496a-473b-91cf-e3977b11a32b", 
    "UbuntuBionic": "173cd753-e310-4756-b748-06381768755c", 
    "UbuntuFocal": "bd506383-f1a1-4a8a-a106-ea8e921a4ef5", 
    "Debian10": "673f47df-8af4-4df1-9c10-6f12123a41ea"
}

network = {
    "int805": "2a9e6f38-6802-4905-8f55-e8ec6fec77ee", 
    "int804": "c3a3bd74-3b1d-4064-a935-b3a35ba60cff"
}

api_url = "http://10.119.102.100"
jenis_api = {
    "auth": ":5000/v3/auth/tokens", 
    "instance": ":8774/v2.1/servers", 
    "image": ":9292/v2.1/images", 
    "flavor": ":8774/v2.1/flavors", 
    "network": ":9696/v2.0/networks"
}


def get_Token():
    headers = {
        "content-type": "application/json"
    }    
    data = {
        "auth": {
        "identity": {
            "methods": [
                "password"
            ],
            "password": {
                "user": {
                    "name": "raihan",
                    "domain": {
                        "name": "Default"
                    },
                    "password": "rhn2019"}
            }
        },
        "scope": {
            "project": {
                "domain": {
                    "id": "default"
                },
                "name": "ITF"
            }
        }
    }
    }

    send_data = requests.post(f"{api_url}{jenis_api['auth']}", data=json.dumps(data), headers=headers)
    return send_data.headers["x-subject-token"]

def get_Serverlist():
    headers = {
        "content-type": "application/json", 
        "X-Auth-Token": get_Token()
    }
    get_instance = requests.get(f"{api_url}{jenis_api['instance']}", headers=headers)
    return print(get_instance.json())

def get_Imagelist():
    headers = {
        "content-type": "application/json", 
        "X-Auth-Token": get_Token()
    }
    get_image = requests.get(f"{api_url}{jenis_api['image']}", headers=headers)
    data_image = get_image.json()
    print('List Image:')
    for image in data_image['images']:
        image_name = image['name']
        image_id = image['id']
        print(f"Image Name: {image_name}")

def get_Flavorlist():
    headers = {
        "content-type": "application/json", 
        "X-Auth-Token": get_Token()
    }
    get_flavor = requests.get(f"{api_url}{jenis_api['flavor']}", headers=headers)
    return print(get_flavor)

def get_Networklist():
    headers = {
        "content-type": "application/json", 
        "X-Auth-Token": get_Token()
    }
    get_network = requests.get(f"{api_url}{jenis_api['network']}", headers=headers)
    return print(get_network)

def createInstance():

    headers = {
        "content-type": "application/json", 
        "X-Auth-Token": get_Token()
    }
    data_instance = {
        "server": {
        "name": "test-api",
        "imageRef": f"{image[f'{arg_image}']}",
        "flavorRef": f"{flavor[f'{arg_flavor}']}",
        "OS-DCF:diskConfig": "AUTO",
        "networks": [{
            "uuid": f"{network[f'{arg_network}']}"
        }]
    }
    }
    create_instance = requests.post(f"{api_url}{jenis_api['instance']}", data=json.dumps(data_instance) , headers=headers)
    return print(f"{create_instance.json()}")


get_Token()
get_Imagelist()