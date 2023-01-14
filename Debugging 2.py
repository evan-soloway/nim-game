import random

r1 = ["+"]*7
r2 = ["+"]*5
r3 = ["+"]*3
r4 = ["+"]*1

rows = [r1,r2,r3,r4]

for x in range (20):
     comp_selected_row = random.randint(0, len(rows)-1)
     print(len(rows[comp_selected_row]))


import tensorflow as tf

print(tf.reduce_sum(tf.random.normal([1000, 1000])))
