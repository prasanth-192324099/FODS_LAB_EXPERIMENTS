import numpy as np
from scipy.stats import ttest_ind

# Simulated conversion rates (e.g., 1 = converted, 0 = not converted)
design_A = np.random.binomial(1, 0.15, 1000)
design_B = np.random.binomial(1, 0.20, 1000)

# t-test
t_stat, p_value = ttest_ind(design_A, design_B)

print("T-statistic:", t_stat)
print("P-value:", p_value)

if p_value < 0.05:
    print("Significant difference in conversion rates.")
else:
    print("No significant difference.")