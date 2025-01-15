import os
import cv2
import numpy as np

# since we named each file (0-9) and (10='+', 11='-', 12='*')
file_names = list(range(0, 13))
train = []
train_labels = []

for file_name in file_names:
    path = './training_data/' + str(file_name) + '/'
    # read the number of images inside each file
    file_count = len(next(os.walk(path))[2])
    # for each image *.png file
    for i in range(1, file_count+1):
        img = cv2.imread(path + str(i) + '.png')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # put the gray image into train
        train.append(gray)
        # put the label(file_name) into train_label
        train_labels.append(file_name)

x = np.array(train)
# since we have 20x20 sized image, reshape to 1D array for training
train = x[:, :].reshape(-1, 400).astype(np.float32)
train_labels = np.array(train_labels)[:, np.newaxis]

print(train.shape)
print(train_labels.shape)

# save it as 'trained.npz'
np.savez('trained.npz', train=train, train_labels=train_labels)