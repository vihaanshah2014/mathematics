import numpy as np
import matplotlib.pyplot as plt

#talagrand inequality function
def talagrand_inequality(dimension, parameters):
    #extract parameters
    c = parameters['c'];
    K = parameters['K'];

    conentration_bound = K * np.sqrt((c + np.log(2)) / dimension)

    return conentration_bound;

#finding optimal measure using the inequality
def optimal_estimate_talagrand(data, dimension, paramters):
    empirical_measure = np.mean(data, axis=0);
    expected_measure = np.mean(data, axis=0);

    concentration_bound = talagrand_inequality(dimension, paramters)

    optimal_estimate = empirical_measure + concentration_bound
    
    return optimal_estimate

#data points that can be changed to test and understand
samples = 1000
dimension = [10, 50, 100, 200]
parameters = {'c': 1.0, 'K': 1.0}

avg_estimates = []
for dim in dimension:
    data = np.random.rand(samples, dim)
    estimate = optimal_estimate_talagrand(data, dim, parameters)
    avg_estimate = np.mean(estimate)
    avg_estimates.append(avg_estimate)
    print(f"For {dim} dimensions, the average optimal estimate is: {avg_estimate:.3f}")

plt.figure(figsize=(8,6))
plt.plot(dimension, avg_estimates, marker='o')
plt.xlabel('Number of Dimensions')
plt.ylabel('Average Optimal Estimate')
plt.title('Average Optimal Estimate vs. Number of Dimensions')
plt.grid(True)
plt.show()

#There is not too much change shown when parameters are changed slightly
#Feel free to uncomment the code to visualize it

# Change the parameters and observe the impact
# parameters_list = [
#     {'c': 0.5, 'K': 1.0},
#     {'c': 1.0, 'K': 1.0},
#     {'c': 2.0, 'K': 1.0},
#     {'c': 1.0, 'K': 0.5},
#     {'c': 1.0, 'K': 2.0}
# ]

# dimension = 50
# avg_estimates_params = []
# for params in parameters_list:
#     data = np.random.rand(samples, dimension)
#     estimate = optimal_estimate_talagrand(data, dimension, params)
#     avg_estimates = np.mean(estimate)
#     avg_estimates_params.append(avg_estimates)
#     print(f"For parameters {params}, the average optimal estimate is {avg_estimates:.3f}")

# param_labels = [f"c={p['c']}, K={p['K']}" for p in parameters_list]

# plt.figure(figsize=(8,6))
# plt.bar(param_labels, avg_estimates)
# plt.xlabel('Parameter Values')
# plt.ylabel('Average Optimal Estimate')
# plt.title('Average Optimal Estimate for Different Paramter Values')
# plt.xticks(rotation=45)
# plt.grid(True)
# plt.show()
