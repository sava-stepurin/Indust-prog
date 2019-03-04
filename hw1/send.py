import pika
import random
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

while True:
	channel.basic_publish(exchange='',
                      	routing_key='queue',
                      	body=str(random.random()))
	print("I sent number!")
	time.sleep(random.randint(1, 5))
	
connection.close()
