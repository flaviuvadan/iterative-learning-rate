""" Holds the class responsible for the matplotlib configuration used to generate the plots """


class Plot:
    """ Plot class """

    def __init__(self, x_values, y_values):
        """
        Initialize a Plot class.
        :param x_values: x values to plot
        :param y_values: corresponding y values
        """
        self.x_values = x_values
        self.y_values = y_values

    def plot(self):
        """ Plot the chart using the class' x and y values """
        print(self.x_values, self.y_values)
