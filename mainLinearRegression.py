import numpy as np
import plotData as pD

# loading data from populationProfit.txt : first column, population, second column, profits
popProfitData = np.genfromtxt("populationProfit.txt", dtype=float, delimiter=',')
populationColumn = popProfitData[:,0]
profitColumn = popProfitData[:,1]

# number of training set examples
m = profitColumn.size
# print("number of training set examples = ",profitColumn.size)

# scatter plot of training data
pD.plotData(populationColumn, profitColumn)
