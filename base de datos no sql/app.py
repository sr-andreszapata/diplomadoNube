import boto3

#Crear cliente para dynamodb
dynamodb = boto3.resource('dynamodb', region_name = 'us-east-1')

tabla = dynamodb.Table('tabla-andres-zapata')

#Leer un elemento de la tabla
response = tabla.get_item(Key={'id': '2'})


#print(response['Item'])

#Leer todos los elementos de la tabla
#response = tabla.scan()

#print(response['Items'])

response = tabla.update_item(
    Key={
        'id': '3'  
    },
    UpdateExpression='SET edad = :val1',  # Expresión de actualización
    ExpressionAttributeValues={
        ':val1': 34  # Nuevo valor para atributo2
    }
)

item = {
    "id": "3",
    "nombre": "Andres Mauricio",
    "ciudad": "Entrerrios",
    "edad": 35
}

tabla.put_item(Item=item)