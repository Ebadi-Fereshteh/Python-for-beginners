from matplotlib import projections
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split

data = load_boston()

# create dataFrame (df_boston)
df_boston = pd.DataFrame(data.data , columns= data.feature_names) 
# print(df_boston.head())

# Add column target to dataFrame
df_boston["MEDV"] = data.target

# calcute correlation between target and features
corr = df_boston.corr()
# print(corr["MEDV"])

# Select 2 features with highest correlation with target
select_features = pd.DataFrame(abs(corr["MEDV"]).sort_values(ascending= False))
# print(select_features[1:3].index.values)

# train Data
Xdata = df_boston[select_features[1:3].index.values]
Xdata = Xdata.to_numpy()
# print(Xdata)

Ydata = df_boston["MEDV"].values
Ydata = Ydata.reshape(-1, 1)
print(Ydata.shape)

X_train, X_test, Y_train, Y_test = train_test_split(Xdata, Ydata, test_size= 0.2)

# init
w = np.random.rand(2, 1)
b = np.random.rand(1, 1)

# define Hyper parameters
lr_w = 0.0001
lr_b = 0.1
epochs = 100
Errors = []
Errors_test = []
# fig, ax = plt.subplot(projections='3D')
fig = plt.figure()
ax = fig.add_subplot(121, projection="3d")
ax2 = fig.add_subplot(322)
ax3 = fig.add_subplot(326)

print(X_train.shape)
print(Y_train.shape)
print(w.shape)
# train
for epoch in range(epochs):
    for i in range(X_train.shape[0]):
        x = X_train[i, :]
        y = Y_train[i]
        y_pred = np.matmul(x, w) + b
        # y_pred = y_pred + b
        e = y - y_pred
        x = x.reshape(-1,1)
        # update
        w += lr_w * e * x
        b += lr_b * e 
    
    
    Y_pred = np.matmul(X_train,  w) + b
    Errors.append(np.mean(np.abs(Y_train - Y_pred)))
    ax.clear()
    ax.scatter(X_train[:, 0], X_train[:, 1], Y_train, c='k', marker='.', s= 3, label='Data')
    ax.set_xlabel('LSTAT')
    ax.set_ylabel('RM')
    ax.set_zlabel('Y')
    
    x_range = np.arange(X_train[:,0].min(), X_train[:,0].max())
    y_range = np.arange(X_train[:,1].min(), X_train[:,1].max())

    xs, ys = np.meshgrid(x_range, y_range)
    zs = (w[0] * xs + w[1] * ys) + b
    
    ax.plot_surface(xs, ys, zs, color='orange', alpha=0.5)
    ax2.clear()
    
    ax2.plot(Errors)   

    ax2.set_xlabel("epochs")
    ax2.set_ylabel("MAE")
    ax2.set_title('prediction Error - Train phase') 
    
    Y_pred_test = np.matmul(X_test,  w) + b
    Errors_test.append(np.mean(np.abs(Y_test - Y_pred_test)))
    ax3.clear()
    ax3.plot(Errors_test)
    ax3.set_xlabel("epochs")
    ax3.set_ylabel("MAE")
    ax3.set_title("prediction Error - Test phase")
    
    plt.pause(0.01)
plt.show()






