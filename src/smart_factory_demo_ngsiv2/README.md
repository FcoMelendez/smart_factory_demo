# Pre-requisites

1. Python3 installation
2. Orion Context Broker 

* Optional: In order to monitor the broker, a Postman client can be used along with the Postman collection available at:
'smart_factory_demo/Smart Factory Demo.postman_collection.json' 

# Setting up the demo

First step, clone this repository `git clone https://github.com/FcoMelendez/smart_factory_demo.git`

Second step, go to the `/src/smart_factory_demo_ngsiv2` folder

Third step, run your Orion Context Broker instance

Fourth step, set the ip and port of the context broker in the file 'library.py'

# Running the examples

The python scripts in this demo will allow you to create a demo environment and execute some use cases.

## Workflow

1. `python3 services.py -c start`
2. `python3 services.py -c update_asset_state`
3. `python3 services.py -c simulate_asset_event`
4. `python3 services.py -c simulate_asset_A_command`
5. `python3 services.py -c simulate_asset_B_behavior`


