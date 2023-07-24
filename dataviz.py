import matplotlib.pyplot as plt
import numpy as np

# Generate some random data for 5 different datasets
data_labels = ['Dataset 1', 'Dataset 2', 'Dataset 3', 'Dataset 4', 'Dataset 5']
data_values = [np.random.randint(1, 10) for _ in range(5)]

# Create a bar plot
plt.bar(data_labels, data_values)

# Add labels and title
plt.xlabel('Datasets')
plt.ylabel('Values')
plt.title('Bar Plot with 5 Different Datasets')

# Show the plot
plt.show()
