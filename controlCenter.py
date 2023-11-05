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

connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

channel.queue_declare(queue=RabbitQueue, durable=True)

def callback(ch, method, properties, body):
    print(f"Received: {body}")

channel.basic_consume(queue=RabbitQueue, on_message_callback=callback, auto_ack=True)

print("Waiting for messages. To exit, press CTRL+C")

channel.start_consuming()
