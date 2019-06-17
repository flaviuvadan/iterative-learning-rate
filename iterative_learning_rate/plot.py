""" Holds the class responsible for the matplotlib configuration used to generate the plots """

import matplotlib.pyplot as plt
from matplotlib import lines

plt.style.use('seaborn-whitegrid')


class Plot:
    """ Plot class """

    def __init__(self, x_values, y_values, title, filename):
        """
        Initialize a Plot class.
        :param x_values: x values to plot
        :param y_values: corresponding y values
        :param title: title of the plot
        :param filename: name of the plot file
        """
        self.x_values = x_values
        self.y_values = y_values
        self.title = title
        self.filename = filename

    def plot(self):
        """ Plot the chart using the class' x and y values """
        fig, ax = plt.subplots()
        line = lines.Line2D(self.x_values, self.y_values)
        ax.add_line(line)
        ax.set_title(self.title)
        ax.axis([0, len(self.x_values), 0, max(self.y_values)])
        plt.savefig(self.filename)
        fig.clear()
