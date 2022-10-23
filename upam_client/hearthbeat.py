import socket
import os
import logging
import asyncio
import psutil

HOST = "0.0.0.0"  # Standard loopback interface address (localhost)
PORT = 2023  # Port to listen on (non-privileged ports are > 1023)

async def run(loop, logger=None):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(2)
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                try:
                    if data:
                        match data.decode('ascii'):
                            case 'state':
                                conn.sendall(b'ok')
                            case 'cpu':
                                conn.sendall(str(psutil.cpu_percent(0)).encode())
                            case 'disk':
                                conn.sendall(str(psutil.disk_usage('/')[3]).encode())
                            case 'memory':
                                conn.sendall(str(psutil.virtual_memory()[2]).encode())
                            case _:
                                conn.sendall(b'UndefinedCommand')
                except Exception as e: logger.debug(e)
            # shutdown computer

                


if __name__ == "__main__":
    logger = logging.getLogger("tarsolution-client")
    logger.setLevel(os.environ.get('LOG_LEVEL', "DEBUG"))
    handler = logging.StreamHandler()
    handler.setFormatter(
        logging.Formatter(
            os.environ.get('LOG_FORMAT', "%(asctime)s [%(levelname)s] %(name)s: %(message)s")
        )
    )
    logger.addHandler(handler)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(loop=loop, logger=logger))
    loop.close()