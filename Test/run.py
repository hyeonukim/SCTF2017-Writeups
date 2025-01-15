import numpy as np
import cv2
import utils
import requests
import shutil
import time

# getting trained dataset
FILE_NAME = 'trained.npz'

# loading trained dataset
with np.load(FILE_NAME) as data:
    train = data['train']
    train_labels = data['train_labels']

knn = cv2.ml.KNearest_create()
knn.train(train, cv2.ml.ROW_SAMPLE, train_labels)

def check(test, train, train_labels):
    # find nearest 'k' characters, and determine the label for it
    # the reason why k = 1 here is because we have small dataset and since each numbers are in same size, we can use k = 1
    ret, result, neighbours, dist = knn.findNearest(test, k=1)
    return result

def get_result (file_name):
    image = cv2.imread(file_name)
    # get the chars of image
    chars = utils.extract_chars(image)
    result_string = ''
    for char in chars:
        # after resizing the image, label them into 0-12
        matched = check(utils.resize20(char[1]), train, train_labels)
        # if matched number is 0-9 append it to result_string
        if matched < 10:
            result_string += str(int(matched))
            continue
        # if matched number is 10, append '+' to result_string
        if matched == 10:
            matched = '+'
        # if matched number is 11, append '-' to result_string
        elif matched == 11:
            matched = '-'
        # if matched number is 12, append '*' to result_string
        elif matched == 12:
            matched = '*'
        result_string += matched
    return result_string

host = "http://localhost:10000"
# at first we start at /start
url = '/start'

with requests.Session() as s:
    answer = ''
    # we had to solve 100 questions, but we can increase the loop amount
    for i in range(0, 100):
        start_time = time.time()
        # submit answer, our first answer at the start should be ''
        params = {'ans': answer}

        # get our next image location
        response = s.post(host + url, params)
        print('Server Return: ' + response.text)
        # update our url to check on our first for loop
        if i == 0:
            returned = response.text
            image_url = host + returned
            url = '/check'
        # after first loop we should have new url for image
        else:
            returned = response.json()
            image_url = host + returned['url']

        print('Problem ' + str(i) + ': ' + image_url)

        # download the image into target_images folder
        response = s.get(image_url, stream=True)
        target_image = './target_images/' + str(i) + '.png'
        with open(target_image, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response

        answer_string = get_result(target_image)
        print('String: ' + answer_string)
        answer_string = utils.remove_first_0(answer_string)
        answer = str(eval(answer_string))
        print('Evaluated Answer: ' + answer)
        print('--- %s seconds ---' % (time.time() - start_time))