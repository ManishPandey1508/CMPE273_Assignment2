import boto3

def setMenu(event, context):
    Menu = boto3.resource('dynamodb').Table('Menu')
    Menu.put_item(Item = event)
    return "ok"