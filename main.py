# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

from wxfserializer.serializer import WXFExprSerializer
from wxfserializer.wxfdataconsumer import InMemoryWXFDataConsumer
from wxfserializer.wxfexprprovider import WXFExprProvider
from wxfserializer.wxfnumpyencoder import NumPyWXFEncoder

import numpy
import time

def basicListOfString(lenght=10000):
    pyExpr = ['abcdefgh' for i in range(lenght)]
    start = time.perf_counter()
    expr_provider = WXFExprProvider()
    data_consumer = InMemoryWXFDataConsumer()
    serializer = WXFExprSerializer(expr_provider, data_consumer)
    serializer.serialize(pyExpr)
    stop = time.perf_counter()
    print('serialization of list of string took: ', stop - start)
    # print(data_consumer.data())
    with open('/tmp/pytest.wxf', 'wb') as output:
        output.write(data_consumer.data())

def basicListOfInteger(lenght=10000):
    pyExpr = list(range(lenght))
    start = time.perf_counter()
    expr_provider = WXFExprProvider()
    data_consumer = InMemoryWXFDataConsumer()
    serializer = WXFExprSerializer(expr_provider, data_consumer)
    serializer.serialize(pyExpr)
    stop = time.perf_counter()
    print('serialization of list of int took: ', stop - start)

def basicNumPyArray(length=1e7):
    start = time.perf_counter()
    arr = numpy.empty(int(length), 'int16')
    arr.fill(int(5))
    expr_provider = WXFExprProvider(NumPyWXFEncoder())
    data_consumer = InMemoryWXFDataConsumer()
    serializer = WXFExprSerializer(expr_provider, data_consumer)
    serializer.serialize(arr)
    stop = time.perf_counter()
    with open('/tmp/numpytest.wxf', 'wb') as output:
        output.write(data_consumer.data())
    print('serialization of numpy array took: ', stop - start)

def mixNumPyAndBasicTypes():
    start = time.perf_counter()
    arr = numpy.empty(int(1e1), 'int16')
    arr.fill(-1)
    pyexpr = ["foo", 1, -512, arr]
    expr_provider = WXFExprProvider(NumPyWXFEncoder())
    data_consumer = InMemoryWXFDataConsumer()
    serializer = WXFExprSerializer(expr_provider, data_consumer)
    serializer.serialize(pyexpr)
    stop = time.perf_counter()
    with open('/tmp/numpytest2.wxf', 'wb') as output:
        output.write(data_consumer.data())
    print('serialization of mixed numpy array took: ', stop - start)

def main():
    # basicListOfString()
    # basicNumPyArray()
    # mixNumPyAndBasicTypes()
    basicListOfInteger()

    # start = time.perf_counter()
    # arr = numpy.empty(int(1e1), 'uint16')
    # arr.fill(-1)
    # # pyexpr = [1, ["foo"], [[]], [[], 1, [arr, 1]], '']
    # pyexpr = {
    #     'str': "abc élève wolf: \uF11E",
    #     'int': {'int8': [-1, 1]},
    #     'numpy' : arr
    # }
    # expr_provider = WXFExprProvider(NumPyWXFEncoder())
    # data_consumer = InMemoryWXFDataConsumer()
    # serializer = WXFExprSerializer(expr_provider, data_consumer)
    # serializer.serialize(pyexpr)
    # stop = time.perf_counter()
    # with open('/tmp/test.wxf', 'wb') as output:
    #     output.write(data_consumer.data())
    # print('serialization of mixed numpy array took: ', stop - start)

    expr_provider = WXFExprProvider()
    data_consumer = InMemoryWXFDataConsumer()
    serializer = WXFExprSerializer(expr_provider, data_consumer)
    serializer.serialize(
        {
            'list': [1, 2, 3],
            'int': 1e5
        }
    )
    wxf_bytes = data_consumer.data()
    with open("/tmp/file.wxf", 'wb') as w_file:
        w_file.write(wxf_bytes)

main()