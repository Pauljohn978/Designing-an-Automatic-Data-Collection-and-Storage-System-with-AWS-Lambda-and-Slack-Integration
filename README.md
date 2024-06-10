Designing an Automatic Data Collection and Storage System with AWS Lambda and Slack Integration for Server Availability Monitoring and Slack Notification
Tech: AWS Lambda, Amazon RDS, CloudWatch, Slack AP

The programme tasked with creating an AWS Lambda function that will periodically fetch data from an API and store it in an Amazon RDS instance. This function is triggered by an Amazon CloudWatch Event
that occurs every 15 seconds.To fetch the data from the API, the function uses the requests library (or a similar library) to make a GET request to the API. The function
then uses a library such as psycopg2 to connect to the Amazon RDS instance and store the data in the database. In addition to fetching and storing the data, the function also uses Amazon CloudWatch to
monitor the server and send an alert to a Slack community if the server goes down. 

Usage:
Copy the code into AWS Lambda, the replace the Slack URL with your own aftering creating it. Also rename the DynamoDB Table to your own NoSQL table.
