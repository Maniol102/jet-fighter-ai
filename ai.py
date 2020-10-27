from random import uniform

class Brain:
    def __init__(self):
        self.layers = [8, 5, 5, 4]
        self.biases = [[0 for j in range(max(self.layers))] for i in range(len(self.layers)-1)]
        self.weights = [[[0 for n in range(self.layers[1])] for j in range(max(self.layers))] for i in range(len(self.layers)-1)]

        for i in range(len(self.biases)):
            for j in range(self.layers[i]):
                self.biases[i][j] = uniform(-1,1)
                self.biases[i][j ] = uniform(-1,1)

        for i in range(len(self.weights)):
            for j in range(self.layers[i]):
                for n in range(len(self.weights[i][j])):
                    self.weights[i][j][n] = uniform(-1,1)



    '''
    input_net:
    [0] = x position
    [1] = y position
    [2] = direction
    [3] = velocity
    [4] = opponent x
    [5] = opponent y
    [6] = opponent direction
    [7] = opponent velocity
    '''
    def neural_network(self, input_net):
        layer1 = [0 for i in range(self.layers[1])]
        for i in range(len(input_net)):
            for j in range(len(layer1)):
                layer1[j] += (input_net[i] + self.biases[0][i]) * self.weights[0][i][j]
        
        layer2 = [0 for i in range(self.layers[2])]
        for i in range(len(layer1)):
            for j in range(len(layer2)):
                layer2[j] += (layer1[i] + self.biases[1][i]) * self.weights[1][i][j]
        
        layer3 = [0 for i in range(self.layers[3])]
        for i in range(len(layer2)):
            for j in range(len(layer3)):
                layer3[j] += (layer2[i] + self.biases[2][i]) * self.weights[2][i][j]


'''
output
[0] = forward
[1] = turn left
[2] = turn right
[3] = shoot
'''