import boto3

def updateMenu(event, context):
    dynamoDB = boto3.resource('dynamodb')
    menusTable = dynamoDB.Table('Menu')
    menusTable.update_item(
        Key={
            "menu_id": event.get('menu_id')
        },
        UpdateExpression='set selection = :val1',
        ExpressionAttributeValues={
            ':val1': event.get('selection')}
    )

    return "OK"