import random
import math

class DataSet():

    def __init__(self):
        self.dataPoints = {}

    def add(self, x, y, label):
        self.dataPoints[(x, y)] = label

    def get(self, x, y):
        if (x, y) in self.dataPoints:
            return self.dataPoints[(x, y)]
        return None

    def print(self):
        for d in self.dataPoints:
            print([d, self.dataPoints[d]])


class ClusterPoint():
    # used for generateGaussDist()
    def __init__(self, x, y, label):
        self.x = x
        self.y = y
        self.label = label


def plotDataSet(dataset, xstart, ystart, xend, yend):
    for y in range(ystart, yend):
        for x in range(xstart, xend):
            label = dataset.get(x, y)
            if label == 0:
                print("o", end="  ")
            elif label == 1:
                print("x", end="  ")
            else:
                print("-", end="  ")
        print(" " + str(y))


def generateXORDataSet(numSamples, generateFloats=True):
    # Generates a dataset divided into 4 quadrants (XOR Dataset)
    # Set generateFloats to False to generate integer values only

    dataset = DataSet()
    for n in range(numSamples):
        # generate n sample points
        if not useFloats:
            x = random.randint(-5, 5)
            y = random.randint(-5, 5)
        else:
            x = random.uniform(-5, 5)
            y = random.uniform(-5, 5)

        if x * y == 0:
            continue

        label = 0
        if x * y > 0:
            label = 1

        dataset.add(x, y, label)
    return dataset


def generateGaussDist(cluster_points, samples_per_cluster, variance, generateFloats=True):
    # Generates a clustered distribution around given cluster points using gauss distribution
    # cluster_points is a list of ClusterPoints

    dataset = DataSet()
    for p in cluster_points:
            for s in range(0, samples_per_cluster):
                rand_x = random.gauss(p.x, math.sqrt(variance))
                rand_y = random.gauss(p.y, math.sqrt(variance))
                if not generateFloats:
                    rand_x = round(rand_x)
                    rand_y = round(rand_y)

                print((rand_x, rand_y))

                dataset.add(rand_x, rand_y, p.label)
    return dataset


if __name__ == '__main__':
    # dataset = generateXORDataSet(40, generateFloats=False)
    # dataset.print()
    # plotDataSet(dataset, -5, -5, 5, 5)

    clusters = [ClusterPoint(5, -5, 0), ClusterPoint(2, 4, 1), ClusterPoint(-2, -3, 1)]
    dataset = generateGaussDist(clusters, 30, 2, generateFloats=False)
    plotDataSet(dataset, -10, -10, 10, 10)
