import numpy as np

class RecurrentNeuralNetwork:

    def __init__ (self, xs, ys, rl, eo, lr):
        self.x = np.zeros(xs)
        self.xs = xs
        self.y = np.zeros(ys)
        self.ys = ys
        self.w = np.random.random((ys,ys))
        self.G = np.zeros_like(self.w)
        self.rl = rl
        self.lr = lr
        self.ia = np.zeros((rl+1, xs))
        self.ca = np.zeros((rl+1, ys))
        self.oa = np.zeros((rl+1, ys))
        self.ha = np.zeros((rl+1, ys))
        self.af = np.zeros((rl+1, ys))
        self.ai = np.zeros((rl+1, ys))
        self.ac = np.zeros((rl+1, ys))
        self.ao = np.zeros((rl+1, ys))
        self.eo = np.vstack((np.zeros(eo.shape[0]), eo.T))
        self.LSTM = LSTM(xs, ys, rl, lr)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def dsigmoid(self, x):
        return self.sigmoid(x) * (1 - self.sigmoid(x))

    def forwardProp(self):
        for i range(1, self.rl+1):
            self.LSTM.x = np.hstack((self.ha[i-1], self.x))
            cs, hs, f, c, o = self.LSTM.forwardProp()
            self.ca[i] = cs
            self.ha[i] = hs
            self.af[i] = f
            self.ai[i] = inp
            self.ac[i] = c
            self.ao[i] = o
            self.oa[i] = self.sigmoid(np.dot(self.w, hs))
            self.x = self.eo[i-1]
        return self.oa

    def backProp(self):
        totalError = 0
        dfcs = np.zeros(self.ys)
        dfhs = np.zeros(self.ys)
        tu = np.zeros((self.ys, self.ys))
        tfu = np.zeros((self.ys, self.xs + self.ys))
        tiu = np.zeros((self.ys, self.xs + self.ys))
        tcu= np.zeros((self.ys, self.xs + self.ys))
        tou = np.zeros((self.ys, self.xs + self.ys))
        for i in range(self.rl, -1, -1):
            error = self.oa[i] - self.eo[i]
            tu += np.dot(np.atleast_2d(error * self.dsigmoid(self.oa[i])), np.atleast_2d(self.ha[i]).T)
            error = np.dot(error, self.w)
            self.LSTM.x = np.hstack((self.ha[i-1], self.ia[i]))
            self.LSTM.cs = self.ca[i]
            fu, iu, cu, ou, dfcs, dfhs =self.LSTM.backProp(error, self.)
