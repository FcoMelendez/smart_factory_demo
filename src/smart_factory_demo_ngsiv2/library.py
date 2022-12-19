import requests
import json

# Interface Examples:
# - CREATE an i40Asset
# - CREATE an i40Asset Attribute
# - UPDATE an i40Asset Attribute
# - DELETE an i40Asset

# CREATE an i40Asset
#-------------------
def create_i40_asset(entity_id, entity_type, i40assetType, i40AssetName = None, 
                     hasParentI40Asset = None, i40AssetState = None, oee = None, 
                     oeeAvailability = None, oeePerformance = None, oeeQuality = None, 
                     oeeObject = None):
    payload_dict = {}
    # Entity Id
    payload_dict["id"] = str(entity_id)
    # Entity Type
    payload_dict["type"] = str(entity_type)
    # i40AssetType
    payload_dict["i40AssetType"] = {}
    payload_dict["i40AssetType"]["type"]= "string"
    payload_dict["i40AssetType"]["value"]= str(i40assetType)
    # i40AssetName
    if i40AssetName is not None:
        payload_dict["i40AssetName"] = {}
        payload_dict["i40AssetName"]["type"]= "string"
        payload_dict["i40AssetName"]["value"]= str(i40AssetName)
    # hasParentI40Asset
    if hasParentI40Asset is not None:
        payload_dict["hasParentI40Asset"] = {}
        payload_dict["hasParentI40Asset"]["type"]= "string"
        payload_dict["hasParentI40Asset"]["value"]= str(hasParentI40Asset)
    # i40AssetState
    if i40AssetState is not None:
        payload_dict["i40AssetState"] = {}
        payload_dict["i40AssetState"]["type"]= "string"
        payload_dict["i40AssetState"]["value"]= str(i40AssetState)        
    # oee params
    if oee is not None:
        payload_dict["oee"] = {}
        payload_dict["oee"]["type"]= "number"
        payload_dict["oee"]["value"]= float(oee)
    if oeeAvailability is not None:
        payload_dict["oeeAvailability"] = {}
        payload_dict["oeeAvailability"]["type"]= "number"
        payload_dict["oeeAvailability"]["value"]= float(oeeAvailability)
    if oeePerformance is not None:
        payload_dict["oeePerformance"] = {}
        payload_dict["oeePerformance"]["type"]= "number"
        payload_dict["oeePerformance"]["value"]= float(oeePerformance)
    if oeeQuality is not None:
        payload_dict["oeeQuality"] = {}
        payload_dict["oeeQuality"]["type"]= "number"
        payload_dict["oeeQuality"]["value"]= float(oeeQuality)
    if oeeObject is not None:
        if type(oeeObject) is dict:
            payload_dict["oeeObject"] = {}
            payload_dict["oeeObject"]["type"]= "object"
            payload_dict["oeeObject"]["value"]= json.dumps(oeeObject)
    

    url = "http://localhost:1026/v2/entities/"

    payload= json.dumps(payload_dict)
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)

# CREATE a new i40Asset Attribute
#--------------------------------
def create_i40_asset_attribute (entity_id, attr_id, attr_type, attr_value):
    url = "http://localhost:1026/v2/entities/"+str(entity_id)+"/attrs"
    attribute = {}
    attribute[str(attr_id)] = {}
    attribute[str(attr_id)]["type"] = attr_type
    attribute[str(attr_id)]["value"] = attr_value
    payload = json.dumps(attribute)
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)

# UPDATE an i40Asset Attribute
#--------------------------------
def update_i40_asset_attribute (entity_id, attr_id, attr_value):
    url = "http://localhost:1026/v2/entities/"+str(entity_id)+"/attrs/"+str(attr_id)+"/value"
    content_type = "text/plain"
    attribute = json.dumps(attr_value)
    if type(attr_value) is dict:
        content_type = "application/json"
    payload = attribute
    headers = {'Content-Type': content_type}
    response = requests.request("PUT", url, headers=headers, data=payload)
    print(response.text)

# DELETE an i40Asset
#-------------------
def delete_i40_asset(entity_id):
    url = "http://localhost:1026/v2/entities/"+str(entity_id)
    payload={}
    headers = {}
    response = requests.request("DELETE", url, headers=headers, data=payload)
    print(response.text)