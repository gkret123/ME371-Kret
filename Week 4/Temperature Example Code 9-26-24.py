# Given the following daily temperature data
import numpy as np

temps = np.array([20,25,22,30,28,27,26])

avg_temp = np.mean(temps)
median_temp = np.median(temps)
std_dev_temp = np.std(temps)

print(f"The average temperature is {avg_temp:.2f}")
print(f"The median temperature is {median_temp}")
print(f"The standard deviation of the temperature is {std_dev_temp:.2f}")

norm_temps = (temps - avg_temp) / std_dev_temp
print(f"The normalized temperature data is {norm_temps}")

mask = temps > avg_temp
days = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"]
for i in range(len(mask)):
    if mask[i]:
        print(f"{days[i]} is above average")


    
        
    