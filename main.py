""" Main file to run the iterative learning rate package """

import iterative_learning_rate


def main():
    learn = iterative_learning_rate.IterativeLearningRate(0.9, 0.1, 100)
    x, y = learn.learn()
    plot = iterative_learning_rate.Plot(x, y, 'Learning rate over 100 iterations', 'plot_100')
    plot.plot()

    learn = iterative_learning_rate.IterativeLearningRate(0.9, 0.1, 1000)
    x, y = learn.learn()
    plot = iterative_learning_rate.Plot(x, y, 'Learning rate over 100 iterations', 'plot_1000')
    plot.plot()

    learn = iterative_learning_rate.IterativeLearningRate(0.9, 0.1, 10000)
    x, y = learn.learn()
    plot = iterative_learning_rate.Plot(x, y, 'Learning rate over 100 iterations', 'plot_10000')
    plot.plot()


main()
