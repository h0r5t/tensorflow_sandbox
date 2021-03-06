import tensorflow as tf
from tensorflow import keras
import numpy as np
import random

import datasets
from datasets import ClusterPoint
import tf_visualizer


# Simples neuronales Netz zur Klassifizierung von Punkten mit 2 Merkmalen (x und y)

class TensorflowClassifierExample():

    def __init__(self):
        # Initialisiere das Modell des neuronalen Netzwerks
        self.model = keras.Sequential([
            # Input-Schicht muss nicht explizit spezifiziert werden

            # "Deep Layers" mit verschiedener Neuronenanzahl
            keras.layers.Dense(8, activation=tf.nn.tanh),
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
        self.model.compile(optimizer=tf.train.GradientDescentOptimizer(0.01),
                           loss='mean_squared_error')

    def trainModel(self, dataset, epochs=100, batch_size=0):
        # Trainiere das Modell anhand des gegebenen Testdatensatzes
        # Setze Anzahl der Epochs sowie die Batch-Size
        data_list = np.asarray(dataset.getDataList())
        label_list = np.asarray(dataset.getLabelList())

        if batch_size == 0:
            self.model.fit(x=data_list, y=label_list, epochs=epochs)
        else:
            self.model.fit(x=data_list, y=label_list, epochs=epochs, batch_size=batch_size)

    def testModel(self, dataset):
        print("Test results:")
        data_list = np.asarray(dataset.getDataList())
        label_list = np.asarray(dataset.getLabelList())
        # prediction = self.model.predict(np.expand_dims(input, 0))
        predictions = self.model.predict(x=data_list)

        for i in range(0, len(data_list)):
            print("x/y: " + str(data_list[i]) + " -> prediction: " + str(predictions[i][0]) + " (real = " + str(label_list[i]) + ")")

    def testDataPoint(self, x, y):
        test_point = np.expand_dims([x, y], 0)
        prediction = self.model.predict(test_point)
        print("x/y: " + str([x, y]) + " -> Prediction: " + str(prediction))

    def getModel(self):
        return self.model



if __name__ == '__main__':
        # Generiere 2 Datensets für Training und Testing
        #   Simples XOR-Datenset bzw. Cluster-Datenset

        # training_data = datasets.generateXORDataSet(num_samples=40, space_width=20, generateFloats=True)
        clusters = [ClusterPoint(0, 0, -1), ClusterPoint(-7, 0, 1), ClusterPoint(7, 0, 1), ClusterPoint(0, 7, 1), ClusterPoint(0, -7, 1), ClusterPoint(-4, -5, 1), ClusterPoint(4, 5, 1), ClusterPoint(-2, 8, 1)]
        training_data = datasets.generateGaussDist(cluster_points=clusters, samples_per_cluster=10, variance=3, space_width=20, generateFloats=True)
        # testing_dataset = datasets.generateGaussDist(cluster_points=clusters, samples_per_cluster=10, variance=1, space_width=20, generateFloats=True)

        tf_visualizer.visualizeDataset(training_data)

        tf_classifier = TensorflowClassifierExample()
        tf_classifier.trainModel(dataset=training_data, epochs=250, batch_size=10)

        # tf_classifier.testModel(testing_dataset)
        tf_visualizer.visualizeClassification(tf_classifier.getModel(), training_data)
