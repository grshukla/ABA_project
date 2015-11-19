import tensorflow as tf
import numpy as np

#Plugging in the x and y datasets
x = tf.placeholder("float", [None, 1024])
y = tf.placeholder("float", [None, 2 ] )

#Defining weight variables
def weight_variable(shape):
  initial = tf.truncated_normal(shape, stddev=0.1)
  return tf.Variable(initial)
  
def bias_variable(shape):
  initial = tf.constant(0.1, shape=shape)
  return tf.Variable(initial)
  
#First Layer (100 Nodes)
w_l1=weight_variable([1024,100])
b_l1=bias_variable([100])
h_1=tf.sigmoid(tf.matmul(x,w_l1) + b_l1)

#Second Layer (10 Nodes)
w_l2=weight_variable([100,10])
b_l2=bias_variable([10])
#h_2=tf.sigmoid(tf.matmul(h_1,w_l2) + b_l2)
h_2_dropout=tf.sigmoid(tf.matmul(h_1,w_l2) + b_l2)

#Applying the dropout to redout layer
#keep_prob = tf.placeholder("float")
#h_2_dropout=tf.nn.dropout(h_2, keep_prob)

#Readout Layer (Binary output)
w_l3=weight_variable([10,2])
b_l3=bias_variable([2])
y_model=tf.nn.softmax(tf.matmul(h_2_dropout,w_l3) + b_l3)

#Training the model
#cross_entropy = -tf.reduce_sum(y*tf.log(y_model))
loss = tf.reduce_mean(tf.square(y - y_model))
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(loss)
correct_prediction = tf.equal(tf.argmax(y_model,1), tf.argmax(y,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))

#Running the iterations
sess.run(tf.initialize_all_variables())
for i in range(100000):
  #sess.run(train_step, feed_dict={x: x_data, y: y_data, keep_prob: 0.25})
  sess.run(train_step, feed_dict={x: x_data, y: y_data})
  print sess.run(w_l3[0,:])
  
  
print sess.run(accuracy, feed_dict={x: x_data, y: y_data})

#For visualizing
#://stackoverflow.com/questions/33783672/how-can-i-visualize-the-weightsvariables-in-cnn-in-tensorflow
#http://stackoverflow.com/questions/33772833/error-while-merging-summaries-for-tensorboard



