import csv

def read_mechanical_data(filename):
    """
    Read mechanical data from a CSV file.
    
    Args:
    filename (str): Name of the CSV file
    
    Returns:
    list of tuples: List of (time, position, force) tuples
    """
    open_file = open(filename, 'r')
    csv_reader = csv.reader(open_file)
    data = []
    next(csv_reader)
    for row in csv_reader:
        time = (float(row[0]))
        position = (float(row[1]))
        force = (float(row[2]))
        data.append((time, position, force))
    open_file.close()
    return data

"""-------------------------------------------------------------------------------------------------------------------------"""

def calculate_velocity(position_data, time_step):
    """
    Calculate velocity from position data.
    
    Args:
    position_data (list of tuples): List of (time, position) tuples
    time_step (float): Time step between measurements
    
    Returns:
    list of tuples: List of (time, velocity) tuples
    """
    velocity_data = []
    for i in range(1, len(position_data)):
        time = position_data[i][0]
        position = position_data[i][1]
        prev_time = position_data[i - 1][0]
        prev_position = position_data[i - 1][1]
        velocity = (position - prev_position) / (time - prev_time)
        velocity_data.append((time, velocity))
    return velocity_data

"""-------------------------------------------------------------------------------------------------------------------------"""

def calculate_acceleration(velocity_data, time_step):
    """
    Calculate acceleration from velocity data.
    
    Args:
    velocity_data (list of tuples): List of (time, velocity) tuples
    time_step (float): Time step between measurements
    
    Returns:
    list of tuples: List of (time, acceleration) tuples
    """
    acceleration_data = []
    for i in range(1, len(velocity_data)):
        time = velocity_data[i][0]
        velocity = velocity_data[i][1]
        prev_time = velocity_data[i - 1][0]
        prev_velocity = velocity_data[i - 1][1]
        acceleration = (velocity - prev_velocity) / (time - prev_time)
        acceleration_data.append((time, acceleration))
    return acceleration_data

"""-------------------------------------------------------------------------------------------------------------------------"""

def find_max_force(force_data):
    """
    Find the maximum force applied to the system.
    
    Args:
    force_data (list of tuples): List of (time, force) tuples
    
    Returns:
    tuple: (time, max_force)
    """
    for i in range(1, len(force_data)):
        time = force_data[i][0]
        force = force_data[i][2]
        max_force = max(force)
    return (force_data["max_force"][0],max_force)