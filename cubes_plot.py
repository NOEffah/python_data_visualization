import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('ggplot')

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues)

ax.set_title("Cubes", fontsize=40)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Cubes of Values", fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)
ax.axis([0, 5100, 0, 135000000000])

plt.show()
