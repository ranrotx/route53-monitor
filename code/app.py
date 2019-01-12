import json
import boto3

sns = boto3.client('sns')

monitoredRecords = {
    'hostname.example.com' : 'arn:aws:sns:region:account:NotifyMe'
}

def lambda_handler(event, context):
    
    changes = event['detail']['requestParameters']['changeBatch']['changes']

    for x in changes:

        if x['action'] == 'UPSERT':
            
            hostToUpdate = x['resourceRecordSet']['name']
            print "UPSERT action detected on " + hostToUpdate

            if hostToUpdate in monitoredRecords:
                arn = monitoredRecords[hostToUpdate]
                message = json.dumps(x['resourceRecordSet'])

                print "Calling " + arn + " with " + message
                response = sns.publish(
                    TopicArn=arn,
                    Message=message
                )
            
            else:
                print "Ingnoring since not in list of monitoredRecords"
        
        else:
            
            print "Not an UPSERT, no action required"

    return {
        "statusCode": 200,
        "body": response
    }
