import os
import pika
from dotenv import load_dotenv
load_dotenv()

CONTROL_CENTER_IP = os.getenv("CONTROL_CENTER_IP")
RabbitUser = os.getenv("RabbitUser")
RabbitPass = os.getenv("RabbitPass")
RabbitVHOST = os.getenv("RabbitVHOST")
RabbitQueue = os.getenv("RabbitQueue")

connection_params = pika.ConnectionParameters(
    host=CONTROL_CENTER_IP,
    virtual_host=RabbitVHOST,
    credentials=pika.PlainCredentials(RabbitUser, RabbitPass)
)

def publishControlCenter(message):
    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()
    channel.queue_declare(queue=RabbitQueue, durable=True)
    channel.basic_publish(exchange='',
                    routing_key=RabbitQueue,
                    body=message)
    connection.close()
    