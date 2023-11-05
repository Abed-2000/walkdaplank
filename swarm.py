import os
import pika
from dotenv import load_dotenv
import cv2
import pickle
import struct
import socket

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

def send_video_feed(server_ip):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, 8080))
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        data = pickle.dumps(frame)
        client_socket.sendall(struct.pack("<L", len(data)) + data)
    cap.release()
    client_socket.close()