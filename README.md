# AWSSpotAdvisorData

# Overview

This repository contains a script to extract Spot Advisor data from AWS. 
when this scripts run it checks if new data is available through AWS API and if so it saves it in json format with a time stamp in the file's name.

This repository also contains some utils functions for parsing the json files to pandas data frame.

# Prerequests

Python 3.10

You can use Anaconda to install all the required packages or simply run ```pip install -r requirements.txt```

# How to Use

Simply run ```python .\extract_data.py```

