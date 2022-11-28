import time
import os
import sys
from kafka import KafkaConsumer


if __name__ == '__main__':

    print("Starting script...")

    consumer = KafkaConsumer(bootstrap_servers='0.0.0.0:9093')
    consumer.subscribe('test')

    print("Waiting for message...")
    print(consumer)

    for msg in consumer:
        print(2)
        print("Msg: "+msg.value.decode('utf-8'))
        print("Waiting for message...")

    print("Ending script!")
