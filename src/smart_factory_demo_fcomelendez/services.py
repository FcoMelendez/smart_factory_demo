import sys
import getopt
import json
import library as lib

# Service Examples
# - CREATE Factory
# - CREATE Advanced Asset Attributes: 
#       i40AssetName, i40AssetState, i40AsesetEvent, i40AssetCommand
# - UPDATE an i40AsesetState
# - Simulation I (Asset event): Asset "A" publishes an i40AsesetEvent (e.g., 'start error' event)
# - Simulation II (Asset command): Asset "B" sends one command to Asset "A" (e.g., ABORT) 
# - DELETE (Clean) Factory

# CREATE Factory
#---------------
def create_factory():
    lib.create_i40_asset("urn:ngsiv2:i40Asset:Site:001", "i40Asset", "Site")
    lib.create_i40_asset("urn:ngsiv2:i40Asset:Area:001", "i40Asset", "Area")
    lib.create_i40_asset("urn:ngsiv2:i40Asset:Area:002", "i40Asset", "Area")
    lib.create_i40_asset("urn:ngsiv2:i40Asset:Workstation:001", "i40Asset", "Workstation")
    lib.create_i40_asset("urn:ngsiv2:i40Asset:Workstation:002", "i40Asset", "Workstation")
    lib.create_i40_asset("urn:ngsiv2:i40Asset:Unit:001a", "i40Asset", "Unit")
    lib.create_i40_asset("urn:ngsiv2:i40Asset:Unit:002a", "i40Asset", "Unit")
    lib.create_i40_asset("urn:ngsiv2:i40Asset:Unit:002b", "i40Asset", "Unit")
    create_advanced_asset_attributes("urn:ngsiv2:i40Asset:Workstation:002")

# CREATE Advanced Asset Attributes: i40AssetName, i40AssetState
#--------------------------------------------------------------
def create_advanced_asset_attributes(entity_id):
    # Smart Workstation: urn:ngsiv2:i40Asset:Workstation:002
    attribute_id = "i40AssetName"
    attribute_type = "string"
    attribute_value = "packagingStation"
    lib.create_i40_asset_attribute(entity_id, attribute_id, attribute_type, attribute_value)
    attribute_id = "i40AssetState"
    attribute_type = "string"
    attribute_value = "STOPPED"
    lib.create_i40_asset_attribute(entity_id, attribute_id, attribute_type, attribute_value)
    attribute_id = "i40AssetEvent"
    attribute_type = "object"
    attribute_value = {}
    attribute_value["class"] = "-"
    attribute_value["description"] = "This asset has not yet published any event"
    attribute_value["message"] = "-"
    attribute_value = attribute_value 
    lib.create_i40_asset_attribute(entity_id, attribute_id, attribute_type, attribute_value)
    attribute_id = "i40AssetCommand"
    attribute_type = "object"
    attribute_value = {"-":"-"}
    attribute_value = attribute_value 
    lib.create_i40_asset_attribute(entity_id, attribute_id, attribute_type, attribute_value) 
    attribute_id = "i40AssetCommand-STATUS"
    attribute_type = "object"
    attribute_value = {"-":"-"}
    attribute_value = attribute_value 
    lib.create_i40_asset_attribute(entity_id, attribute_id, attribute_type, attribute_value) 
    attribute_id = "i40AssetCommand-RESULT"
    attribute_type = "object"
    attribute_value = {"-":"-"}
    attribute_value = attribute_value 
    lib.create_i40_asset_attribute(entity_id, attribute_id, attribute_type, attribute_value) 

# UPDATE an i40AssetState
#-------------------------
def update_an_i40AssetState():
    entity_id = "urn:ngsiv2:i40Asset:Workstation:002"
    attr_value = "IDLE"
    lib.update_i40_asset_attribute(entity_id, "i40AssetState", attr_value)

# Simulation I (Asset event): Asset "A" publishes an i40AsesetEvent (e.g., 'start error' event)
#----------------------------------------------------------------------------------------------
def simulate_asset_event():
    entity_id = "urn:ngsiv2:i40Asset:Workstation:002"
    attr_value = {}
    attr_value["class"] = "error"
    attr_value["description"] = "Human intervention required"
    attr_value["message"] = {}
    attr_value["message"]["code"] = "0001a"
    attr_value["message"]["name"] = "start error"
    attr_value["message"]["action"] = "Check red indicators in the control unit. Check the correct placement and quantity of input materials"
    lib.update_i40_asset_attribute(entity_id, "i40AssetEvent", attr_value)

# Simulation II (Asset command): Asset "B" sends one command to Asset "A" (e.g., ABORT)
#--------------------------------------------------------------------------------------
def simulate_asset_A_command():
    entity_id = "urn:ngsiv2:i40Asset:Workstation:002"
    attr_value = {}
    attr_value["method"] = "START"
    attr_value["attrs_array"] = ["attr0", "attr1", "attr2", "attr3"]
    lib.update_i40_asset_attribute(entity_id, "i40AssetCommand", attr_value)

# Simulation III (Asset behavior): Asset "B" sends one command to Asset "A" (e.g., ABORT)
#--------------------------------------------------------------------------------------
def simulate_asset_B_behavior():
    entity_id = "urn:ngsiv2:i40Asset:Workstation:002"
    lib.update_i40_asset_attribute(entity_id, "i40AssetCommand-STATUS", "Processing")
    lib.update_i40_asset_attribute(entity_id, "i40AssetCommand-RESULT", "Accepted")
    lib.update_i40_asset_attribute(entity_id, "i40AssetState", "EXECUTE")

# DELETE (Clean) Factory
#-----------------------
def clean_factory():
    lib.delete_i40_asset("urn:ngsiv2:i40Asset:Site:001")
    lib.delete_i40_asset("urn:ngsiv2:i40Asset:Area:001")
    lib.delete_i40_asset("urn:ngsiv2:i40Asset:Area:002")
    lib.delete_i40_asset("urn:ngsiv2:i40Asset:Workstation:001")
    lib.delete_i40_asset("urn:ngsiv2:i40Asset:Workstation:002")
    lib.delete_i40_asset("urn:ngsiv2:i40Asset:Unit:001a")
    lib.delete_i40_asset("urn:ngsiv2:i40Asset:Unit:002a")
    lib.delete_i40_asset("urn:ngsiv2:i40Asset:Unit:002b")


def run_service(argv):
    arg_command = ""
    arg_help = "{0} -c <command> \n \
        \n  <command> options: \n \
        \n    'start'                     creates all the smart factory entities \
        \n    'update_asset_state'        updates the i40AssetState attribute (Workstation002) \
        \n    'simulate_asset_event'      publishes an error event via the i40AssetEvent attribute (Workstation002) \
        \n    'simulate_asset_A_command'  simulates asset_A sending a command to asset_B (Workstation002) \
        \n    'simulate_asset_B_behavior' simulates asset_B (Workstation002) receiving and processing the command \
        \n    ".format(argv[0])
    
    try:
        opts, args = getopt.getopt(argv[1:], "hc:", ["help", "command="])
    except:
        print(arg_help)
        sys.exit(2)
    
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(arg_help)  # print the help message
            sys.exit(2)
        elif opt in ("-c", "--command"):
            arg_command = arg
            if arg_command == "start":
                create_factory()
            if arg_command == "update_asset_state":
                update_an_i40AssetState()
            if arg_command == "simulate_asset_event":
                simulate_asset_event()
            if arg_command == "simulate_asset_A_command":
                simulate_asset_A_command()
            if arg_command == "simulate_asset_B_behavior":
                simulate_asset_B_behavior()
            elif arg_command == "clean":
                clean_factory()
            arg_output = arg

    print('command:', arg_command)

if __name__ == "__main__":
    run_service(sys.argv)
