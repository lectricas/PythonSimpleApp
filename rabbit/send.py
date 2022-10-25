import pika, sys, os
from time import sleep

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


def main():
    while True:
        print("Daylight, its time to make some traffic")
        for x in range(5):
            message = f'User {x}'
            channel.basic_publish(exchange='test', routing_key='test_routing', body=bytes(message, encoding='utf8'))
        print("Night is coming...")
        sleep(3)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
