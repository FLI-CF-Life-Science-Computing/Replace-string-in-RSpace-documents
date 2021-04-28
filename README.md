# Replace string in RSpace documents

A Python script that uses the RSpace API and the Python RSpace API client to search all documents for a user for a string and replace it

## Prerequisite

* Python3
* RSpace API client: https://github.com/rspace-os/rspace-client-python

## How to use

There are four variables in the script that need to be set.

* API_KEY: The API key of the RSpace user the script searches for the string (https://researchspace.helpdocs.io/article/v0dxtfvj7u-rspace-api-introduction)
* ELN_URL: The URL of your RSpace ELN deployment
* ORIGINALTEXT: The text that is searched for
* NEWTEXT: The text that replace the ORIGINALTEXT

After the variables have been set you can run the script: *python3 main.py*

The script creates a log file named main.log inside the main.py folder. The log file can be used to track which documents have been changed.
