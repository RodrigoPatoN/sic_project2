import paho.mqtt.client as mqtt
import time
import sys

def get_prediction(vals):

    mean = sum(vals)/len(vals)

    if mean < vals[0]:
        return 0.9 * mean
    
    else:
        return 1.1 * mean


def on_disconnect(client, userdata, rc):
    print("Disconnected with result code "+str(rc))
    print(rc)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("kapacitor")

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    num_payload = msg.payload
    predict = num_payload.decode('utf-8')
    num = float(predict)
    sys.stdout.write(str(num))

    vals.append(num)

    if len(vals) >= 5:
        prediction = get_prediction(vals[-5:])
        influx_line_msg = f"predictionMeasurement prediction={prediction}"
        client.publish("weatherprediction", influx_line_msg)
        time.sleep(10)

def on_publish(client, userdata, result):
    sys.stdout.write("Message published: "+str(result))
    print("Message published: "+str(result))

if __name__ == '__main__':

    vals = []

    client = mqtt.Client("sic-subscriber")
    client.on_message = on_message
    client.on_subscribe = on_subscribe
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_publish = on_publish

    try:
        client.connect("rabbitmq")
    except:
        print("trying...")
        time.sleep(20)

        try:
            client.connect("rabbitmq")
        except:
            print("trying...")
            time.sleep(20)

            try:
                client.connect("rabbitmq")
            except:
                print("trying...")
                time.sleep(20)

                try:
                    client.connect("rabbitmq")
                except:
                    print("failed")
    
    client.loop_forever()