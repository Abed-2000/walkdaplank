import cv2
import socket
import threading
import pickle
import struct

def handle_client(client_socket):
    try:
        print("Client connected.")
        data = b""
        payload_size = struct.calcsize("<L")

        while True:
            while len(data) < payload_size:
                data += client_socket.recv(4096)
            packed_msg_size = data[:payload_size]
            data = data[payload_size:]
            msg_size = struct.unpack("<L", packed_msg_size)[0]

            while len(data) < msg_size:
                data += client_socket.recv(4096)

            frame_data = data[:msg_size]
            data = data[msg_size:]
            frame = pickle.loads(frame_data)

            cv2.imshow('Received Frame', frame)
            cv2.waitKey(1)
    except Exception as e:
        print(f"Error handling client: {str(e)}")
    finally:
        client_socket.close()
        print("Client disconnected.")

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 8080))
    server_socket.listen(5)
    print("Server listening on port 8080")

    while True:
        client_socket, addr = server_socket.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()
