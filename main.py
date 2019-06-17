""" Main file to run the iterative learning rate package """

import iterative_learning_rate


def main():
    learn_100 = iterative_learning_rate.IterativeLearningRate(0.5, 0.1, 100)
    x_values_100, y_values_100 = learn_100.learn()

    plot_100 = iterative_learning_rate.Plot(x_values_100, y_values_100, 'Learning rate over 100 iterations')
    plot_100.plot()


main()
