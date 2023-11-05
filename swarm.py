import os
import pika
from dotenv import load_dotenv
load_dotenv()

DARRYL_IP = os.getenv("DARRYL_IP")
ABED_IP = os.getenv("ABED_IP")
RabbitUser = os.getenv("RabbitUser")
RabbitPass = os.getenv("RabbitPass")
RabbitVHOST = os.getenv("RabbitVHOST")
RabbitQueue = os.getenv("RabbitQueue")

connection_params = pika.ConnectionParameters(
    host=ABED_IP,
    virtual_host=RabbitVHOST,
    credentials=pika.PlainCredentials(RabbitUser, RabbitPass)
)

connection = pika.BlockingConnection(connection_params)
channel = connection.channel()


channel.queue_declare(queue=RabbitQueue, durable=True)

message = "Hello from Sending Machine " + DARRYL_IP + "!"
channel.basic_publish(exchange='',
                   routing_key=RabbitQueue,
                   body=message)

print(f"Sent: {message}")

connection.close()