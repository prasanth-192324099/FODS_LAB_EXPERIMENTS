import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Example Data
control = np.random.normal(5, 2, 50)
treatment = np.random.normal(8, 2, 50)

# t-test
t_stat, p_val = stats.ttest_ind(treatment, control)
print("P-Value:", p_val)

plt.hist(control, alpha=0.5, label='Control')
plt.hist(treatment, alpha=0.5, label='Treatment')
plt.legend()
plt.title("Treatment vs Control Group Distribution")
plt.show()

if p_val < 0.05:
    print("Treatment is significantly effective.")
else:
    print("No significant difference found.")
