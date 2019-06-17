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
        for i in range(0, self.iterations):
            print(i)
