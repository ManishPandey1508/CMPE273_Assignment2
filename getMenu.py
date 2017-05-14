import boto3
from boto3.dynamodb.conditions import Key, Attr


def getMenu(event, context):
    menu_id = event['menu-id']
    print("Menu Id %s"%menu_id)
    Menu = boto3.resource('dynamodb').Table('Menu')
    return Menu.get_item(Key={'menu_id': menu_id})['Item']