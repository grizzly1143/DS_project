import socket
from time import sleep
import requests


class Client:
    def __init__(self):
        self.node = None

    def connect_to_server(self,):
        self.node = socket.socket()
        while True:
            try:
                self.node.connect(())
                break
            except ConnectionRefusedError:
                sleep(3)

    def initialize(self, name):
        response = requests.get(self.node, json={"command": "init", "dir_name": name})
        return response

    def file_create(self, filepath):
        return

    def file_read(self, filepath):
        return

    def file_write(self, filepath):
        return

    def file_delete(self, filepath):
        return

    def file_info(self, filepath):
        return

    def file_copy(self, filepath, dest_filepath):
        return

    def file_move(self, filepath, dest_filepath):
        return

    def open_directory(self, filepath):
        return

    def read_directory(self, filepath):
        return

    def make_directory(self, filepath):
        return

    def delete_directory(self, filepath):
        return

    def client_run(self):
        return


if __name__ == "__main__":
    c = Client()

    c.connect_to_server()
    c.initialize()
    c.client_run()
