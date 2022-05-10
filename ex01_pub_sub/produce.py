#!/usr/bin/env python3

import pulsar

SERVICE_URL = "pulsar://localhost:6650"
TOPIC = "persistant://public/default/my-topic"

def main():
    client = pulsar.Client(SERVICE_URL)
    producer = client.create_producer(TOPIC)

    for i in range(10):
        producer.send(('hello-pulsar-%d' % i).encode('utf-8'))

    client.close()

if __name__ == "__main__":
    main()
