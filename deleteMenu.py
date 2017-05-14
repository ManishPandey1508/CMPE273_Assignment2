import boto3
from botocore.exceptions import ClientError


def deleteMenu(event, context):
    Menu = boto3.resource('dynamodb').Table('Menu')

    try:
        response = Menu.delete_item(
            Key={
                "menu_id": event.get('menu-id')
            }
        )
    except ClientError as e:
        if e.response['Error']['Code'] == "ConditionalCheckFailedException":
            print(e.response['Error']['Message'])
        else:
            raise
    else:
        print("DeleteItem succeeded:")

    return "OK"


