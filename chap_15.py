import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth = 5)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis = "both", labelsize = 14)
plt.show()


x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.get_cmap('plasma'), edgecolor='none', s=10)

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.axis([0, 1100, 0, 1100000])
plt.tick_params(axis="both", which="major", labelsize=14)
plt.show()

plt.savefig('squares_plot.png', bbox_inches='tight')

x_list = list(range(5000))
y_list = [x**3 for x in x_list]
plt.scatter(x_list, y_list, c=y_list, cmap=plt.get_cmap('plasma') ,s=10)
plt.title("Cube Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)
plt.axis([0, 5100, 0, 150000000000])
plt.tick_params(axis="both", which="major", labelsize=14)

plt.plot()
plt.savefig('squares_colored.png', bbox_inches='tight')

from random import choice

class RandomWalk():
    """Class to generate random walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk."""
        # Keep taking steps untill the walk reaches the desired length
        while len(self.x_values) < self.num_points:
            # Decide which direction to go and how far to go in that direction.
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the next x and y values.
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)


while True:
    # Make a random walk, and plot the points.
    rw = RandomWalk()
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.get_cmap('plasma'), edgecolor='none', s=5)
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()
    plt.savefig('walk_colored.png', bbox_inches='tight')
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

while True:
    # Make a random walk, and plot the points.
    rw = RandomWalk(50000)
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    plt.figure(dpi=128, figsize=(10, 6))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.get_cmap('plasma'), edgecolor='none', s=1)
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()
    plt.savefig('big_walk_colored.png', bbox_inches='tight')

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

from random import randint


class dice():
    def __init__(self, num_sides=6):
        self.sides = num_sides

    def roll(self):
        return randint(1, self.sides)

dice_ins = dice()

results = []

for i in range(1000):
    result = dice_ins.roll()
    results.append(result)
#print()

import pygal
frequencies = []
for value in range(1, dice_ins.sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
#print(results)
print(frequencies)

hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times"
hist.title = "Random Variable Visualization"
hist.x_labels = ["1", "2", "3", "4", "5", "6"]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("D6", frequencies)
hist.render_to_file('die_visual.svg')

die_1 = dice()
die_2 = dice()

results = []
for roll in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_value = die_1.sides + die_2.sides

for value in range(2, max_value + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()

hist.title = 'Two dice 1000 times'
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Sum of die rolls"
hist.y_title = "Frequency of values"

hist.add('D6 + D6', frequencies)
hist.render_to_file('2die_visual.svg')

die_1 = dice()
die_2 = dice(10)

results = []
for roll_num in range(5000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
sum_value = die_1.sides + die_2.sides
for value in range(2, sum_value + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()
hist.title = 'Two dies of different sizes'
hist.x_title = 'Sum value of two dies'
hist.y_title = 'Frequency'
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
hist.add("D6 + D10", frequencies)
hist.render_to_file("Unequal_dies_sum.svg")
