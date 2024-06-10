#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json
import urllib.request
import boto3
from datetime import datetime

# Initialize DynamoDB resource and specify the table
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('aws-project-table')  #give the correct table name

# Set your Slack incoming webhook URL
slack_webhook_url = "https://hooks.slack.com/services/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"  #webhook URL

def lambda_handler(event, context):
    # URL to fetch data from
    url = "http://api.open-notify.org/iss-now.json"
    
    try:
        # Fetch data from the URL
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
        
        # Extract necessary fields from the response
        iss_position = data.get("iss_position", {})
        latitude = iss_position.get("latitude")
        longitude = iss_position.get("longitude")
        timestamp = data.get("timestamp")
        message = data.get("message")
        
        # Generate a unique ID for the item
        item_id = str(datetime.utcnow().timestamp())
        
        # Create the item to be stored in DynamoDB
        item = {
            'aws-project-table': item_id,  # Primary key attribute
            'latitude': latitude,
            'longitude': longitude,
            'timestamp': timestamp,
            'message': message
        }
        
        # Store the item in DynamoDB
        table.put_item(Item=item)
        
        return {
            'statusCode': 200,
            'body': json.dumps('Data stored successfully!')
        }
        
    except Exception as e:
        error_message = f"Error occurred: {e}"
        print(error_message)
        send_slack_message(error_message)
        return {
            'statusCode': 500,
            'body': json.dumps('An error occurred')
        }

def send_slack_message(message):
    slack_message = {
        'text': message
    }
    
    data = json.dumps(slack_message).encode('utf-8')
    
    req = urllib.request.Request(
        slack_webhook_url,
        data=data,
        headers={'Content-Type': 'application/json'}
    )
    
    try:
        with urllib.request.urlopen(req) as response:
            response.read()
    except Exception as e:
        print(f"Error sending message to Slack: {e}")

