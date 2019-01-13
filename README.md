# route53-monitor

When performing dynamic DNS updates against a Route53 hosted zone, sometimes it may be useful to monitor certain records for updates. One example is you might have a dynamic DNS updater client that updates its record in Route53 whenever its dynamic IP changes. Then when this record changes, you wish to create a notification so that others are aware. This notification could then be used to update Security Groups that have references to this IP.

Inside the `app.py` file, you'll find monitoredRecords that contains the mapping of hostnames to SNS topics. The Lambda function will be triggered by any changes to Route53 that are detected using CloudWatch Events. When the function runs, it is looking for UPSERTs and will then compare the records in the change to monitoredRecords. If there is a match, it will send an SNS notification to the ARN associated with the record.
