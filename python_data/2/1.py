from sklearn.datasets import load_digits
import numpy as np
import matplotlib.pyplot as plt


digits = load_digits()

print("Shape images:{}".format(digits.data.shape))
print("Shape target:{}".format(digits.target.shape))

plt.figure(figsize=(14, 4))

for index, (image, label) in enumerate(zip(digits.data[0:5], digits.target[0:5])):
    plt.subplot(1, 5, index + 1)
    plt.imshow(np.reshape(image, (8, 8)), cmap=plt.cm.gray)
    plt.title('Training: {}\n'.format(label, fontsize=15))