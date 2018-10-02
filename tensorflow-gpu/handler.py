from __future__ import print_function
import tensorflow as tf

def Handler(req):
    sess = tf.Session()
    a = tf.constant(req.input)
    return sess.run(a)
