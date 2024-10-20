# Exercise 2 - - NUMPY and PANDAS FOR DATA ANALYSIS
# Gabriel Kret
# Due: 10/21/2024

#This exercise is about using numpy and pandas to analyze data.

#Part I
import numpy as np
import pandas as pd

def calculate_fluid_statistics(root_dir):
    """
    Calculate statistics for fluid experiments from CSV files.

    This function loads data from fluids.csv, experiments.csv, and fluid_measurements.csv, merges the data, and calculates mean, median, and standard deviation of pressure, velocity, temperature, and flow_rate for each unique fluid.

    Parameters:
    root_dir (str): The root directory containing the CSV files.

    Returns:
    np.array: A structured NumPy array containing the calculated statistics for each fluid.
        The array has the following fields:
        - fluid_id (int): The unique identifier for each fluid.
        - fluid_name (str): The name of the fluid.
        - pressure_mean, pressure_median, pressure_std (float): Statistics for pressure.
        - velocity_mean, velocity_median, velocity_std (float): Statistics for velocity.
        - temperature_mean, temperature_median, temperature_std (float): Statistics for temperature.
        - flow_rate_mean, flow_rate_median, flow_rate_std (float): Statistics for flow rate.
    """
    #read data
    fluids = pd.read_csv(root_dir + '/fluids.csv')
    experiments = pd.read_csv(root_dir + '/experiments.csv')
    fluid_measurements = pd.read_csv(root_dir + '/fluid_measurements.csv')
    
    #merge data
    data = pd.merge(fluids, experiments, on='fluid_id')
    data = pd.merge(data, fluid_measurements, on='experiment_id')
    data = pd.DataFrame(data)
    #calculate statistics
    stats = data.groupby('fluid_id').agg({'pressure': ['mean', 'median', 'std'],
                                         'velocity': ['mean', 'median', 'std'],
                                         'temperature': ['mean', 'median', 'std'],
                                         'flow_rate': ['mean', 'median', 'std']}).reset_index()
    

    print(data)

    pass

# Call the function and print the results
result_array = calculate_fluid_statistics(root_dir='exercise_data') # change root_dir to where your data for this exercise is
print(result_array)