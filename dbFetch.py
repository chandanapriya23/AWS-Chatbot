import json
from CUSTOM import db

#=========================================================================

def lambda_handler(event, context):
    table_name='accommodation'
    LocationName = event["currentIntent"]["slots"]["UniversityLocation"].title()
    print(LocationName)
    Gender = event["currentIntent"]["slots"]["AccommodationFor"].title()
    print(Gender)
    Rooms = event["currentIntent"]["slots"]["RoomTypes"].title()
    print(Rooms)
    
    condition="Location='"+LocationName+"' and RoomType='"+Rooms+"' and RoomFor='"+Gender+"' and Status='Available'"
    print(condition)
    response=db.fetch(table_name,condition)
    
    Status=False
    if response['status'] == 'success':
        for i in response['rows']:
            Status=True
            
        if  Status :
            print('Room Available')
            result= {"dialogAction":{"fulfillmentState":"Fulfilled","type":"Close","message":{"contentType":"PlainText","content": " "+Rooms+" Bedroom is available in "+LocationName+ ". " }}}
            return result
        else:
            print('Room Not Available')
            result= {"dialogAction":{"fulfillmentState":"Fulfilled","type":"Close","message":{"contentType":"PlainText","content": " "+Rooms+" Bedroom is not available in "+LocationName+ ". I am sorry, will let you know soon if we have any availabilities in near future." }}}
            return result
    else:
        result= {"dialogAction":{"fulfillmentState":"Fulfilled","type":"Close","message":{"contentType":"PlainText","content": ""+LocationName+ ":: NOT AVAILABLE" }}}
        return result
        


