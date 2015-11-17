from rdkit import Chem
from rdkit.Chem import AllChem
import numpy as np

#Finding the Noraml fingerptirint
m1 = Chem.MolFromSmiles('Cc1ccccc1')
fp1 = AllChem.GetMorganFingerprint(m1,2)  #radius=2
keys=fp1.GetNonzeroElements().keys()
values=fp1.GetNonzeroElements().values()

#Finding fingerptints as bit vectors
fp1 = AllChem.GetMorganFingerprintAsBitVect(m1,2,nBits=1024)
n_on_bits=fp1.GetNumOnBits()          #number of on bits
on_bits=fp1.GetOnBits()               #Index of on bits

#Making a Simple Neural Net
#Making the dataset
x_data=np.zeros((len(smiles),1024))
for i in range(6):
  m1 = Chem.MolFromSmiles(smiles[i])
  fp1 = AllChem.GetMorganFingerprintAsBitVect(m1,2,nBits=1024)
  n_on_bits=fp1.GetNumOnBits() 
  on_bits=fp1.GetOnBits()
  for j in range(n_on_bits):
    x_data[i,on_bits[j]]=1
    

y_data=np.zeros((6,2))

#Making a Neural Net
x = tf.placeholder("float", shape=[None, 1024])   #Number of features =1024
y_ = tf.placeholder("float", shape=[None, 2])     # Output can be either 0 or 1

W = tf.Variable(tf.zeros([1024,2]))
b = tf.Variable(tf.zeros([2]))

sess.run(tf.initialize_all_variables())
y = tf.nn.softmax(tf.matmul(x,W) + b)

cross_entropy = -tf.reduce_sum(y_*tf.log(y))

train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

for i in range(1000):
  train_step.run(feed_dict={x: x_data, y_: y_data})




