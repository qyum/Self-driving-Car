

from tensorflow.core.protobuf import saver_pb2
#import driving_data
#import model

#LOGDIR = './save'

sess = tf.InteractiveSession()

L2NormConst = 0.001

train_vars = tf.trainable_variables()

loss = tf.reduce_mean(tf.square(tf.subtract(y_, y))) + tf.add_n([tf.nn.l2_loss(v) for v in train_vars]) * L2NormConst
train_step = tf.train.AdamOptimizer(1e-4).minimize(loss)
sess.run(tf.global_variables_initializer())

epochs = 30
batch_size = 100

# train over the dataset about 30 times
for epoch in range(epochs):
  for i in range(int(num_images/batch_size)):
    xs, ys = train_batch(batch_size)
    train_step.run(feed_dict={x: xs, y_: ys,keep_prob: 0.8})
    if i % 10 == 0:
      xs, ys = val_batch(batch_size)
      loss_value = loss.eval(feed_dict={x:xs, y_: ys,keep_prob: 1.0})
      print("Epoch: %d, Step: %d, Loss: %g" % (epoch, epoch * batch_size + i, loss_value))
      
