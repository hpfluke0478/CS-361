import pika
import time
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='Notepad Directory')
notes = []

def callback(ch, method, properties, body):
    ctr = 1
    print("Note Receieved")
    notes.append(body)

    for i in notes:
        print(str(ctr) + ". " + i.decode('utf-8'))
        ctr += 1

channel.basic_consume(queue='Notepad Directory', auto_ack=True, on_message_callback=callback)
channel.start_consuming()
channel.basic_publish(exchange='', routing_key='Notepad Directory', body=notes[0])

def callback2():
    for i in notes:
        channel.basic_publish(exchange='', routing_key='Notepad Directory', body=notes[i])

if __name__== '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Stopped')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)