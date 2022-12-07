import numpy as np
import pandas as pd
import os
import sys
from kafka import KafkaProducer
import time


if __name__ == "__main__":


	data = pd.read_csv('./producer/sensors_sample_data.csv')

	data_array = np.array(data)

	shape = data_array.shape

	print("Starting Kafka Producer...")

	try:
		producer = KafkaProducer(bootstrap_servers='kafka-server:9092')
	except:
		print("failed")
		time.sleep(20)		
		producer = KafkaProducer(bootstrap_servers='kafka-server:9092')

	while True:

		for i in range(shape[0]):
			
			vals = [np.random.uniform(0.7, 1.3) * val for val in data_array[i, :]]
			print(vals)
			string_send = f"weatherMesasurement temperature={vals[0]},rain={vals[1]},uvindex={vals[2]},wind={vals[3]}"
			producer.send('weatherstation', string_send.encode('utf-8'))
			print("sent")
			producer.flush()
			time.sleep(1)

		print("Ending")

		