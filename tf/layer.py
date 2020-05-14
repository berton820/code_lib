#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
layer.py
2019/11/19 9:31 上午 by berton
berton820@126.com
"""
import tensorflow as tf
# 加载词向量
with tf.device('/cpu:0'), tf.variable_scope('word_embedding'):
    self.word_embeddings = tf.get_variable(
        'word_embeddings',
        shape=(self.vocab.size(), self.vocab.embed_dim),
        initializer=tf.constant_initializer(self.vocab.embeddings),
        trainable=True
    )