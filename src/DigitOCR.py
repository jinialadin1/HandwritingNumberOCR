import sys
import numpy as np
import tensorflow as tf

class DataType:
    Self = 0
    IAM = 1
    CHROME = 2

class OCR:
    "simple TF for OCR"

    # constants
    batchSize = 50
    imgSize = (128, 128)

    def __init__(self, DigitList, mustRestore=False):
        
        "init model: add CNN and initialize TF"
        self.DigitList = DigitList
        self.mustRestore = mustResotre
        self.snapID = 0

        # Whether to use normalization over a batch or a population
        self.is_train = tf.placeholder(tf.bool, name='is_train')

        # input image batch
        self.inputImgs = tf.placeholder(tf.float32, shape(None, OCR.imgSize[0], OCR.imgSize[1]))

        # setup CNN
        self.setupCNN()

        # setup optimizer to train NN
        self.batchesTrained = 0
        self.learningRate = tf.placeholder(tf.float32, shape=[])
        self.update_ops = tf.get_collection(tf.GraphKeys.UPDATE_OPS)
        with tf.control_dependencies(self.update_ops):
            self.optimizer = tf.train.RMSPropOptimizer(self.learningRate).minimize(self.loss)

        #initialize TF
        (self.sess, self.saver) = self.setupTF()

    
    def setupCNN(self):
        "create CNN layers and return ouput of these layers"
        cnn4d = tf.expand_dims(input=self.inputImgs, axis=3)

        # list of parametrs for the layers
        kernelVals = [5, 5, 3, 3, 3]
        featureVals = [1, 32, 64, 128, 128, 256]
        strideVals = poolVals = [(2,2), (2,2), (1,2), (1,2), (1,2)]
        numLayers = len(strideVals)

        # create layers
        pool = cnn4d
        for i in range(numLayers):
            kernel = tf.Variable(tf.truncated_normal([kernalVals[i], kernelVals[i], featureVals[i], featureVals[i+1]], stddev=0,1))
            conv = tf.nn.conv2d(pool, kernel, padding='SAME', strides=(1,1,1,1))
            conv_norm = tf.layers.batch_normalization(conv, training=self.is_train)
            relu = tf.nn.relu(conv_norm)
            pool = tf.nn.max_pool(relu, (1, poolVals[i][0], poolVals[i][1], 1), (1, strideVals[i][0], strideVals[i][1], 1), 'VALID')

        self.cnnOut4d = pool
