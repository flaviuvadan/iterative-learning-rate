""" Holds the iterative learning rate class and its methods """


class IterativeLearningRate:
    """ Iterative Learning Rate class """

    def __init__(self, initial_learning_rate, final_learning_rate, iterations):
        """
        Initialize the class.
        :param initial_learning_rate: float - starting learning rate
        :param final_learning_rate: float - desired end learning rate
        :param iterations: int - number of iterations to perform
        """
        self.initial_learning_rate = initial_learning_rate
        self.final_learning_rate = final_learning_rate
        self.iterations = iterations

    def learn(self):
        """
        Perform the specified iterations and report the results
        :return: tuple([iteration i], [learning rate at i])
        """
        x_values = []
        y_values = []
        for i in range(0, self.iterations):
            alpha = i / self.iterations
            learning_rate = (1 - alpha) * self.initial_learning_rate + alpha * self.final_learning_rate
            x_values.append(i)
            y_values.append(learning_rate)
        return x_values, y_values
