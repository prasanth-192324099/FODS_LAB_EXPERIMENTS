
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'City A': np.random.randint(15, 35, 365),
    'City B': np.random.randint(10, 40, 365),
    'City C': np.random.randint(20, 30, 365)
})

mean_temps = df.mean()
std_temps = df.std()
temp_ranges = df.max() - df.min()

print("Mean Temperatures:\n", mean_temps)
print("\nTemperature Ranges:\n", temp_ranges)
print("\nStandard Deviations:\n", std_temps)

print("\nMost consistent city:", std_temps.idxmin())
print("City with highest temp range:", temp_ranges.idxmax())