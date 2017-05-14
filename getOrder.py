import boto3

def getOrder(event, context):
    order_id = event['order_id']
    print("Order Id %s"%order_id)
    orders = boto3.resource('dynamodb').Table('orders')
    return orders.get_item(Key={'menu_id': order_id})['Item']