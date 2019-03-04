import pika
import time

params = pika.ConnectionParameters('rabbit', 5672)
while True:
	try:
		connection = pika.BlockingConnection(params)
		break
	except Exception:
		time.sleep(3)
channel = connection.channel()


channel.queue_declare(queue='queue')

def callback(ch, method, properties, body):
    print("Received %r" % body)

channel.basic_consume(callback,
                      queue='queue',
                      no_ack=True)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
