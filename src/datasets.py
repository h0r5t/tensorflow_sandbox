import random
import math

SPACE_WIDTH = 20
SPACE_HEIGHT = SPACE_WIDTH

class DataSet():

    def __init__(self, space_width):
        self.dataPoints = {}
        self.data_list = []
        self.label_list = []
        self.space_width = space_width

    def add(self, x, y, label):
        self.dataPoints[(x, y)] = label
        self.data_list.append([x, y])
        self.label_list.append(label)

    def get(self, x, y):
        if (x, y) in self.dataPoints:
            return self.dataPoints[(x, y)]
        return None

    def getPoints(self):
        return self.dataPoints

    def getSize(self):
        return len(self.data_list)

    def __repr__(self):
        for d in self.dataPoints:
            print([d, self.dataPoints[d]])

    def getDataList(self):
        return self.data_list

    def getLabelList(self):
        return self.label_list



class ClusterPoint():
    # used for generateGaussDist()
    def __init__(self, x, y, label):
        self.x = x
        self.y = y
        self.label = label


def plotDataSet(dataset):
    w = int(dataset.space_width/2)
    xstart = -w
    ystart = -w
    xend = w
    yend = w

    for y in range(ystart, yend):
        for x in range(xstart, xend):
            label = dataset.get(x, y)
            if label == -1:
                print("o", end="  ")
            elif label == 1:
                print("x", end="  ")
            else:
                print("-", end="  ")
        print(" " + str(y))


def generateXORDataSet(num_samples, space_width, generateFloats=True):
    # Generates a dataset divided into 4 quadrants (XOR Dataset)
    # Set generateFloats to False to generate integer values only

    dataset = DataSet(space_width)
    for n in range(num_samples):
        # generate n sample points
        if not generateFloats:
            x = random.randint(-space_width/2, space_width/2)
            y = random.randint(-space_width/2, space_width/2)
        else:
            x = random.uniform(-space_width/2, space_width/2)
            y = random.uniform(-space_width/2, space_width/2)

        if x * y == 0:
            continue

        label = -1
        if x * y > 0:
            label = 1

        dataset.add(x, y, label)
    return dataset


def generateGaussDist(cluster_points, samples_per_cluster, variance, space_width, generateFloats=True):
    # Generates a clustered distribution around given cluster points using gauss distribution
    # cluster_points is a list of ClusterPoints
    dataset = DataSet(space_width)
    for p in cluster_points:
            for s in range(0, samples_per_cluster):
                rand_x = random.gauss(p.x, math.sqrt(variance))
                rand_y = random.gauss(p.y, math.sqrt(variance))
                if not generateFloats:
                    rand_x = round(rand_x)
                    rand_y = round(rand_y)

                dataset.add(rand_x, rand_y, p.label)
    return dataset


if __name__ == '__main__':
    #dataset = generateXORDataSet(70, 20, generateFloats=False)
    #dataset.print()
    #plotDataSet(dataset)

    clusters = [ClusterPoint(5, -5, -1), ClusterPoint(2, 4, 1), ClusterPoint(-5, -3, 1)]
    dataset = generateGaussDist(cluster_points=clusters, samples_per_cluster=30, variance=2, space_width=20, generateFloats=False)
    plotDataSet(dataset)
