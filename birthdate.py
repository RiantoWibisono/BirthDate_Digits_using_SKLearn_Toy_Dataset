import numpy as np 
import pandas as pd 
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt 

dataDigit = load_digits()
user = input('Input your birthdate (ddmmyy format): ')
position = 1

fig = plt.figure(figsize=(10,2))
for i in user:
    plt.subplot(1, 6, position)
    plt.imshow(dataDigit['images'][int(i)])
    plt.title('Number = {}'.format(dataDigit['target'][int(i)]))
    position += 1

plt.show()