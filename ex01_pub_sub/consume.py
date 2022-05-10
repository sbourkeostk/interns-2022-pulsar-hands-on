#!/usr/bin/env python3

import pulsar

SERVICE_URL = "pulsar://localhost:6650"
TOPIC = "persistant://public/default/my-topic"
SUB_NAME = "app1"
CONSUMER_TYPE = pulsar.ConsumerType.Shared

def main():
    client = pulsar.Client(SERVICE_URL)

    consumer = client.subscribe(TOPIC,
                                subscription_name=SUB_NAME,
                                consumer_type=CONSUMER_TYPE)

    try:
        while True:
            msg = consumer.receive()
            print("Received message: '%s'" % msg.data())
            consumer.acknowledge(msg) # what happens if we don't do this?
    except SystemError:
        pass

    consumer.unsubscribe() # or leave subscipion in place
    client.close()

if __name__ == '__main__':
    main()
