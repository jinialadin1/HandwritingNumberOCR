import sys
import argparse
import cv2
import editdistance

class FilePaths:
    "paths for data and file"
    fnDigitList = '../data/DigitList.txt'
    fnTrainData[3] = ['../data/jpg/preprocess/','../data/IAM/', '../data/CHROME/']
    fnTestData = '../data/test/'

def train(model, loader):
    "train by NN"
    
def validate(model, loader):

def infer(model, fnImg):

def main():
    "main function"
    
    # command args option
    parser = argparse.ArgumentParser()
    parser.add_argument('--train', action='store_ture', help='train model by NN')
    parser.add_argument('--validate', action='store_true', help='validate model by NN')
    parser.add_argument('--data', action='store_const', const=0, help='select train data\n 0-> self data\n 1->IAM data\n 2->CHROME data')
    args = parser.parse_args()
    data_type=args.data

    # train/validate on dataset
    if args.train or args.validate:
        # load data, create TF OCR model
       

    # if there's no command input, make a simple test
    else:
        print("no command input, start a simple test")
        model = OCR(open(FilePaths.fnDigitList).read(), mustRestore=True)



if __name__=="__main__":
    main();
