#!/bin/bash

# For running this script is assumed that you are a user with privileges 
# in the source and the destination project. Additionally you will run the script in the https://shell.cloud.google.com/ 

# Export users from one source project
gcloud config set project 'your-source-project-id'
firebase auth:export your-users-file-export.json --format=json --project your-source-project-id

# Import users, in this case we will be assuming the default config which is SCRYPT
gcloud config set project 'your-destination-project-id'

firebase auth:import your-users-file-export.json --project your-destination-project-id    \
    --hash-algo=SCRYPT         \
    --hash-key=your-hash-key-encoded                     \
    --salt-separator=your-salt-separator-encoded    \
    --rounds=8                    \
    --mem-cost=14

# That is all :)