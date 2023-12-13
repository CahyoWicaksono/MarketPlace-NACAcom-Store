import matplotlib.pyplot as plt

# Sample data
x_values = [1, 2, 3, 4, 5]
y_values = [2, 4, 6, 8, 10]

# Plotting the line chart
plt.plot(x_values, y_values, marker='o', linestyle='-')

# Adding title and labels
plt.title('Simple Line Chart')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')

# Display the chart
plt.show()
