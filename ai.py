from random import uniform

class Brain:
    def __init__(self):
        self.layers = [8, 5, 5, 4]
        self.biases = [[0 for j in range(max(self.layers))] for i in range(len(self.layers)-1)]
        self.weights = [[[0 for n in range(max(self.layers[1:]))] for j in range(max(self.layers))] for i in range(len(self.layers)-1)]

        for i in range(len(self.biases)):
            for j in range(self.layers[i]):
                self.biases[i][j] = uniform(-1,1)
                self.biases[i][j] = uniform(-1,1)

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
        layer = [[0 for j in range(max(self.layers))] for i in range(len(self.layers))]
        layer[0] = input_net
                                                                     
        for f in range(len(self.layers) - 1):
            for i in range(len(self.layers[f])):
                for j in range(self.layers[f + 1]):
                    layer[f][j] += (layer[f][i] + self.biases[f][i]) * self.weights[f][i][j]
        return layer[:self.layers[-1]]
                      
    
                                                                     
    '''
    output
    [0] = forward
    [1] = turn left
    [2] = turn right
    [3] = shoot
    '''
