""" Holds the class responsible for the matplotlib configuration used to generate the plots """


class Plot:
    """ Plot class """

    def __init__(self, x_values, y_values, title):
        """
        Initialize a Plot class.
        :param x_values: x values to plot
        :param y_values: corresponding y values
        :param title: title of the plot
        """
        self.x_values = x_values
        self.y_values = y_values
        self.title = title

    def plot(self):
        """ Plot the chart using the class' x and y values """
        print(self.x_values, self.y_values)
