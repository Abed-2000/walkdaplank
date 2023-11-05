import os
import pika
from dotenv import load_dotenv

load_dotenv()


connection_params = pika.ConnectionParameters(
    host = os.getenv("ABED_IP"),
    virtual_host = os.getenv("RabbitVHOST"),
    credentials=pika.PlainCredentials(os.getenv('RabbitUser'), os.getenv('RabbitPass'))
)

connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

channel.queue_declare(queue = os.getenv('RabbitQueue'))

def callback(ch, method, properties, body):
    print(f"Received: {body}")

channel.basic_consume(queue = os.getenv('RabbitQueue'), on_message_callback=callback, auto_ack=True)

print("Waiting for messages. To exit, press CTRL+C")

channel.start_consuming()
