import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from numpy.linalg import inv

class LinearLeastSquare:
    def __init__(self):
        pass
    
    # train
    def fit(self, X, Y):
        self.w = np.matmul(inv(np.matmul(X.T, X)), np.matmul(X.T, Y))
        
    def predict(self, x):
        height_pred = x * self.w
        return height_pred

    def evaluate(self, X, Y, loss='MAE', delta= 0):   
        
        Y_pred = np.matmul(X, self.w)
        
        Error = Y - Y_pred

        MAE = np.mean(np.abs(Error))
        MSE = np.mean(Error ** 2)
        if loss == 'MAE':
            return MAE
        
        elif loss == 'MSE':
            return MSE
        
        elif loss == 'Huber':
            Huber = np.mean(np.where(MAE <= delta, np.mean(MSE / 2), np.mean(( delta * MAE - ( delta ** 2 / 2) ))))
            return Huber        
        
        elif loss == 'Hinge':
            Error = 1 - (Y * Y_pred)
            Hinge = np.mean(np.where( 0 > Error, 0, Error))
            return Hinge