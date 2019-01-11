import tensorflow as tf
from tensorflow import keras
import numpy as np
import random

import datasets
from datasets import ClusterPoint


class TensorflowClassifierExample():

    def __init__(self):
        # Initialisiere das Modell des neuronalen Netzwerks
        # Hier wird die 'tanh'-Aktivierungsfunktion verwendet (Hyperbolic Tangent)
        self.model = keras.Sequential([

            # Input-Schicht mit 2 Neuronen
            keras.layers.Dense(2, activation=tf.nn.tanh),

            # "Deep Layers" mit jeweils 4 Neuronen
            keras.layers.Dense(4, activation=tf.nn.tanh),
            keras.layers.Dense(4, activation=tf.nn.tanh),

            # Output-Schicht mit einem Neuron
            keras.layers.Dense(1, activation=None)
        ])

        # Kompiliere das Modell & setze Hyperparameter:
        # Optimizer: Verwende das  Standard-Gradientenverfahrens
        # Learning Rate: Setze Lernrate von 0.03
        # Loss function: Kostenfunktion ist die mittlere quadratische Abweichung (MSE)
        # Metriken, die als Indikator für die Performance des Netzes angezeigt werden sollen
        #   Hier: Accuracy = Anteil der korrekt klassifizierten Objekte
        self.model.compile(optimizer=tf.train.GradientDescentOptimizer(0.03),
                  loss='mean_squared_error',
                  metrics=['accuracy'])

    def trainModel(self, dataset, epochs=200, batch_size=10):
        # Trainiere das Modell anhand des gegebenen Testdatensatzes
        # Setze Anzahl der Epochs sowie die Batch-Size
        self.model.fit(x=data_list, y=label_list, epochs=200, batch_size=10)

    def testModel(self):
        # TODO
        test_amount = 20

        for i in range(0, 20):
            index = random.randint(0, len(data_list)-1)
            input = data_list[index]
            correct_label = label_list[index]

            prediction = model.predict(np.expand_dims(input, 0))

            print("Input: " + str(input) + ", CorrectLbl: " + str(correct_label) + ", Pred: " + str(prediction))

    def testDataPoint(self, x, y):
        pass


if __name__ == '__main__':
        dataset_obj = datasets.generateXORDataSet(num_samples=100, space_width=20, generateFloats=False)
        #clusters = [ClusterPoint(5, -5, 0), ClusterPoint(2, 4, 1), ClusterPoint(-5, -3, 1)]
        #dataset_obj = datasets.generateGaussDist(cluster_points=clusters, samples_per_cluster=30, variance=2, space_width=20, generateFloats=False)
        data_list = np.asarray(dataset_obj.getDataList())
        label_list = np.asarray(dataset_obj.getLabelList())

        datasets.plotDataSet(dataset_obj)
