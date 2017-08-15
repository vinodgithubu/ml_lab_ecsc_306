import tensorflow as tf
a = 6
b = 2
c = tf.pow(a,2) 
d = tf.pow(b,2)
e = tf.add(c,d)
f = tf.multiply(2,a)
g = tf.multiply(f,b)
h = tf.subtract(e,g)

with tf.Session() as sess:
    writer = tf.summary.FileWriter("/tmp/tboard/output1", sess.graph)
    print(sess.run(h))
    writer.close()
