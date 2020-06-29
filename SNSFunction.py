import json
import boto3

def lambda_handler(event, context):
    client=boto3.client("sns",
                    aws_access_key_id = "<AWS Access Key>",
                    aws_secret_access_key = "<AWS Secret Key>",
                    region_name ="us-east-1")
    confirmation = event["currentIntent"]["slots"]["Confirmation"].title()
    Name = event["currentIntent"]["slots"]["Name"].title()
    PhoneNumber = event["currentIntent"]["slots"]["PhoneNumber"].title()
    print(confirmation)
    if(confirmation =='Yes'):
        response = {"dialogAction":{"fulfillmentState":"Fulfilled","type":"Close","message":{"contentType":"PlainText","content":" We are processing your request. We will send a confirmation message to your Number about reservation status. " }}}
        client.publish(PhoneNumber=""+PhoneNumber+"",Message="Reservation is Confirmed under the Name "+Name+"")
        return response
    if(confirmation =='No'):
        response = {"dialogAction":{"fulfillmentState":"Fulfilled","type":"Close","message":{"contentType":"PlainText","content":" We are not processing your request. We will send a confirmation message to your Number. " }}}
        client.publish(PhoneNumber=""+PhoneNumber+"",Message="We Are Not Processing Your Reservation. Will see you soon. Have a nice day!!")
        return response

    