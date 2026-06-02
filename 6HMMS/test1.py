import numpy as np
import operator

import numpy as np

def calculate_mean_std(data, boundaries):
    means = [np.mean(data[boundaries[i]:boundaries[i+1]]) for i in range(len(boundaries)-1)]
    stds = [np.std(data[boundaries[i]:boundaries[i+1]]) for i in range(len(boundaries)-1)]
    return means, stds


def adjust_boundaries(data, boundaries, means, stds):
    new_boundaries = [boundaries[0]]
    for i in range(len(means)):
        lower_bound = means[i] - stds[i] / 2
        upper_bound = means[i] + stds[i] / 2
        lower_bound_index = np.argmax(data >= lower_bound)
        upper_bound_index = np.argmax(data > upper_bound)
        if lower_bound_index == 0:
            lower_bound_index = 1
        if upper_bound_index == 0:
            upper_bound_index = len(data)
        new_boundaries.extend([lower_bound_index, upper_bound_index])
    return new_boundaries

def calculate_transition_probabilities(data, boundaries):
    transition_counts = np.zeros((len(boundaries)-1, len(boundaries)-1))
    for i in range(len(boundaries)-1):
        for j in range(len(boundaries)-1):
            transition_counts[i, j] = np.sum((data >= boundaries[i]) & (data < boundaries[i+1]) & (data >= boundaries[j]) & (data < boundaries[j+1]))
    transition_probabilities = transition_counts / np.sum(transition_counts, axis=1, keepdims=True)
    return transition_probabilities

def part_1a(data, num_states, max_iterations=100, tolerance=1e-6):
    # Initialize boundaries
    boundaries = [0, len(data)]
    
    # Initialize prior probabilities
    prior = np.ones(num_states) / num_states
    
    for _ in range(max_iterations):
        # Step 1: Calculate mean and standard deviation for each state
        means, stds = calculate_mean_std(data, boundaries)
        
        # Step 2: Adjust boundaries
        new_boundaries = adjust_boundaries(data, boundaries, means, stds)
        
        # Check for convergence
        if np.allclose(new_boundaries, boundaries, atol=tolerance):
            break
        
        boundaries = new_boundaries
        
    # Step 3: Calculate transition probabilities
    transition_probabilities = calculate_transition_probabilities(data, boundaries)
    
    return prior, means, stds, transition_probabilities

inital_states1 = [[31, 28, 28, 37, 68, 49, 64, 66], [22, 17], [53, 73, 81, 78, 48, 49, 47]]
inital_states2 = [[25, 62, 75, 80, 75], [36, 74, 33, 27], [34]]
inital_states3 = [[-4, 69, 59, 45, 62], [22, 17, 28, 12, 14, 24, 32, 39], [61, 35, 32]]

A = [[31, 28, 28, 37, 68, 49, 25, 62, 75, 80, -4, 69, 59, 45, 62, 22], 
     [64, 66, 22, 17, 53, 73, 75, 36, 74, 33, 17, 28, 12, 14, 24, 32], 
     [81, 78, 48, 49, 47, 27, 34, 39, 61, 35, 32]]

A1 = [[31, 28, 28, 37, 68, 49, 64, 66, 25, 62, 75, 80, 75, -4, 69, 59, 45, 62],
      [22, 17, 36, 74, 33, 27, 22, 17, 28, 12, 14, 24, 32, 39], 
      [53, 73, 81, 78, 48, 49, 47, 34, 61, 35, 32]]

# Initialize boundaries based on initial states
boundaries = [0]
for state in A1:
    boundaries.append(boundaries[-1] + len(state))

# Flatten initial states into a single list
data = [item for sublist in A1 for item in sublist]
print("Initial Boundaries:", boundaries)
print("Initial Data:", data)

# Calculate mean and standard deviation for each state
means, stds = calculate_mean_std(data, boundaries)
print("Means:", means)
print("Standard Deviations:", stds)


