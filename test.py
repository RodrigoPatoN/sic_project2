import numpy as np
import pandas as pd
import os
import sys
from kafka import KafkaProducer
import time

aa = pd.read_csv('sensors_sample_data.csv', header=None)

array = np.array(aa)

if __name__ == "__main__":

	print("Starting Kafka Producer...")

	for n in range(1, 100):

		producer = KafkaProducer(bootstrap_servers='0.0.0.0:9092')

		for i in range(0, 100):
			print(f"i: {i}")
			time.sleep(1)
			producer.send('test', b'number %d' % i)
			print("sent")
			producer.flush()

		print("Ending")