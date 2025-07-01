import numpy as np

fuel_efficiency = np.array([25, 30, 35, 40, 32])

average_eff = fuel_efficiency.mean()
improvement = ((fuel_efficiency[-1] - fuel_efficiency[0]) / fuel_efficiency[0]) * 100

print("Average efficiency:", average_eff)
print("Improvement (%):", improvement)
