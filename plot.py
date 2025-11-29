import matplotlib.pyplot as plt

#x_coords = [1, 2, 3, 4]
#y_coords = [5, 7, 4, 8]
#plt.plot(x_coords, y_coords, 'ro') # 'ro' specifies red circle markers
#plt.title("Multiple Points")
#plt.xlabel("X-axis")
#plt.ylabel("Y-axis")
#plt.show()

## Multiple points
#x_coords = [1, 2, 3, 4]
#y_coords = [5, 7, 4, 8]
#plt.scatter(x_coords, y_coords, color='blue', marker='x', s=100) # 's' for size
#plt.title("Scatter Plot of Points")
#plt.xlabel("X-axis")
#plt.ylabel("Y-axis")
#plt.show()


# Define the coordinates of the points
x_coords = [1, 2, 3, 4, 5]
y_coords = [2, 4, 1, 5, 3]

# Create a figure and an axes object
fig, ax = plt.subplots()

# Plot the points as markers
ax.plot(x_coords, y_coords, 'o', label='Data Points', markersize=8)

# Plot the line segments connecting the points
ax.plot(x_coords, y_coords, '-', label='Line Segments', linewidth=2)

# Add labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Points Connected by Line Segments')
ax.legend()
ax.grid(True)

# Display the plot
plt.show()
