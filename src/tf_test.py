import tensorflow as tf
from tensorflow import keras
import numpy as np
import random

import dataset


class TF_Test():

    def __init__(self):
        pass

    def createModel(self):
        pass

    def trainModel(self):
        pass

    def testRandomBatch(self):
        pass

    def testPoint(self):
        pass


def tf_test():
    dataset_obj = dataset.generateXORDataSet(num_samples=80, space_width=20, generateFloats=False)
    data_list = np.asarray(dataset_obj.getDataList())
    label_list = np.asarray(dataset_obj.getLabelList())

    dataset.plotDataSet(dataset_obj)


    model = keras.Sequential([
        keras.layers.Dense(2, activation=tf.nn.tanh),
        keras.layers.Dense(4, activation=tf.nn.tanh),
        keras.layers.Dense(2, activation=tf.nn.tanh),
        keras.layers.Dense(1, activation=None)
    ])

    tf.print(model)

    model.compile(optimizer=tf.train.GradientDescentOptimizer(0.03),
              loss='mean_squared_error',
              metrics=['accuracy'])

    model.fit(x=data_list, y=label_list, epochs=300)

    # Testing

    test_amount = 20

    for i in range(0, 20):
        index = random.randint(0, len(data_list)-1)
        input = data_list[index]
        correct_label = label_list[index]

        prediction = model.predict(np.expand_dims(input, 0))

        print("Input: " + str(input) + ", CorrectLbl: " + str(correct_label) + ", Pred: " + str(prediction))


if __name__ == '__main__':
    tf_test()
