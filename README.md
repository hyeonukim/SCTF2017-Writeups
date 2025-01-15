
## Project Blog, documentations are written here

It explains my thought process setting up the problem

[https://hyeonukim.github.io/devblog/categories/captcha-hacking/](https://hyeonukim.github.io/devblog/categories/captcha-hacking/)

## How to use

1. Inside ASM/src/ folder, run 'run.py'
    - you should be able to see the problem in [localhost:10000](localhost:10000)   
2. Inside Test/ folder, run 'run.py'

## Problem

Detailed version of problem description

[https://hyeonukim.github.io/devblog/posts/CaptchaHacking1/](https://hyeonukim.github.io/devblog/posts/CaptchaHacking1/)

This problem is one of Samsung's Capture the Flag question from 2017.

You are supposed to automate the process of solving 100 math problems within 80 seconds in a given Captcha Image

## Collecting Data/Analyzing Data

[https://hyeonukim.github.io/devblog/posts/CaptchaHacking2/](https://hyeonukim.github.io/devblog/posts/CaptchaHacking2/)

We found that we don't need much images to train since all characters were in equal size, and we could distinguish each character using color codes

## Data Cleaning

[https://hyeonukim.github.io/devblog/posts/CaptchaHacking3/](https://hyeonukim.github.io/devblog/posts/CaptchaHacking3/)

Using the information about different color code, we could separate each characters and found ROI to save them into separate folder accordingly

## Training Data

[https://hyeonukim.github.io/devblog/posts/CaptchaHacking4/](https://hyeonukim.github.io/devblog/posts/CaptchaHacking4/)

Using our cleaned data, we could train the data using KNN model and print out the math problem into string from an image

## Automating to solve

[https://hyeonukim.github.io/devblog/posts/CaptchaHacking5/](https://hyeonukim.github.io/devblog/posts/CaptchaHacking5/)

We automated the process by getting the response of url to download the image then using our KNN model, we submit answer, repeat the process.
