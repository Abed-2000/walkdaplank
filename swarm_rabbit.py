import os
import pika
from dotenv import load_dotenv

load_dotenv()
myIP = os.getenv('')

main_machine_ip = os.getenv('ABED_IP')
connection_params = pika.ConnectionParameters(host=main_machine_ip)

connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

channel.queue_declare(queue = os.getenv("RabbitQueue"))

message = "Hello from Sending Machine " +  myIP "!"
channel.basic_publish(exchange='',
                      routing_key = os.getenv('RabbitQueue'),
                      body=message)

print(f"Sent: {message}")

connection.close()
