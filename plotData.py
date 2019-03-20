import matplotlib.pyplot as plt

def plotData(X,Y) :
    plt.plot(X, Y, 'b+')
    plt.xlabel("Population of City in 10,0000s")
    plt.ylabel("Profits in $10,000s")
    plt.show()
