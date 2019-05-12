# Handwriting number OCR
The project tries to create software for recognition of a handwritten number from photos. It uses computer vision and machine learning.
In this project I comapre the accuracy of the OCR model trained in different dataset
Using python, tensorflow, openCV.

## Learning Data
There are three different kinds of data
1. real scan data from my friends (10 times per number, total 63 people's handwriting)
2. [NIST dataset](https://www.nist.gov/srd/nist-special-database-19)
3. [CHROME handwritten dataset v2](http://www.iapr-tc11.org/mediawiki/index.php?title=CROHME:_Competition_on_Recognition_of_Online_Handwritten_Mathematical_Expressions)

I used [converter](https://github.com/gskielian/JPG-PNG-to-MNIST-NN-Format) to convert PNG to MNIST

## Program Structure
Proces of recognition is divided into 4 steps. The initial input is a photo of page with text.

1. Detection of page and removal of background
2. Detection and separation of numbers
3. Normalization of numbers
4. Separation and recegnition of characters (recognition of numbers)


Main libraries (all required libraries are in [environment.yml](environment.yml)):
* Numpy ()
* Tensorflow ()
* OpenCV ()
* Pillows ()
* Matlob
