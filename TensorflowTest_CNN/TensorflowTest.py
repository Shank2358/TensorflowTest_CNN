#!/usr/bin/python3.5
# -*- coding: utf-8-*-
import sys
import tensorflow as tf


def HelloTensor(s):
    # 把print输出重定向到当前目录下的log.txt文件
    stdout_backup = sys.stdout
    log_file = open("log.txt", "w")
    sys.stdout = log_file
    # 打印传入参数
    print(s)
    # 调用TensorFlow api
    hello = tf.constant('Hello, Ten1sorFlow!')
    sess = tf.Session()
    print(sess.run(hello))
    # 恢复print输出通道
    log_file.close()
    sys.stdout = stdout_backup


HelloTensor("222")