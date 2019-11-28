#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
data_generate_keras.py
2019/11/19 9:36 上午 by berton
berton820@126.com
"""
import tensorflow as tf
import numpy as np


def generator():
    while True:
        # 产生单个样本
        yield {'a': np.ones([10], np.float32), 'b': np.ones([10], np.float32)}, np.ones([1], np.float32)


D = tf.data.Dataset.from_generator(
    generator,
    ({'a': tf.float32, 'b': tf.float32}, tf.float32),
    ({'a': [10], 'b': [10]}, [1])
)

D = D.batch(32)

strategy = tf.distribute.MirroredStrategy()

with strategy.scope():
    inputA = tf.keras.layers.Input(shape=(10,), name='a')
    inputB = tf.keras.layers.Input(shape=(10,), name='b')

    output = tf.keras.layers.Concatenate()([inputA, inputB])
    output = tf.keras.layers.Dense(1, input_shape=(10,), activation="relu")(output)
    model = tf.keras.models.Model(inputs=[inputA, inputB], outputs=output)
    model.compile('Adam', 'mae')

model.fit(D, steps_per_epoch=1000, epochs=10)
