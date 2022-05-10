#!/usr/bin/env python3

import pulsar

class ExclamationFunction(pulsar.Function):
    def __init__(self):
        pass

    def process(self, input, context):
        return input + '!!!!'
