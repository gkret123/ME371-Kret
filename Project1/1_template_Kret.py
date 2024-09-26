import csv

def read_mechanical_data(filename):
    """
    Read mechanical data from a CSV file.
    
    Args:
    filename (str): Name of the CSV file
    
    Returns:
    list of tuples: List of (time, position, force) tuples
    """
    try:
        open_file = open(filename, 'r')
        csv_reader = csv.reader(open_file)
        data = []
        next(csv_reader)
        for row in csv_reader:
            time = float(row[0])
            position = float(row[1])
            force = float(row[2])
            data.append((time, position, force))
        open_file.close()
        return data
    
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        return []

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
#This assignment can be interpreted in two ways. The first way is to calculate the maximum force as the maximum positive force.
#The second is the find the largest force which could be positive or negative. I chose to implement the first interpretation.
#If you want to implement the second interpretation, you can change the if statement in the find_max_force function to:
# if abs(force) > abs(max_force):

def find_max_force(force_data):
    """
    Find the maximum force applied to the system.
    
    Args:
    force_data (list of tuples): List of (time, force) tuples
    
    Returns:
    tuple: (time, max_force)
    """
    max_force = 0.0
    max_force_time = 0.0
    for i in range(1, len(force_data)):
        time = force_data[i][0]
        force = force_data[i][1]
        if force > max_force: # or write --> if abs(force) > abs(max_force): --> to find the force of the largest mangnitude.
            max_force = force
            max_force_time = time
    return (max_force_time, max_force)

"""-------------------------------------------------------------------------------------------------------------------------"""

def calculate_work_done(force_data, position_data):
    """
    Calculate the total work done on the system.
    
    Args:
    force_data (list of tuples): List of (time, force) tuples
    position_data (list of tuples): List of (time, position) tuples
    
    Returns:
    float: Total work done
    """
    work = 0.0
    for i in range(1, len(force_data)):
        position = position_data[i][1]
        force = force_data[i][1]
        prev_position = position_data[i-1][1]
        distance = position - prev_position
        work += force * distance
    return work
    
"""-------------------------------------------------------------------------------------------------------------------------"""

def write_results(filename, results_data):
    """
    Write calculation results to a CSV file.
    
    Args:
    filename (str): Name of the output CSV file
    results_data (dict): Dictionary containing results to be written
    """
    velocity_data = results_data.get('velocity', [])
    acceleration_data = results_data.get('acceleration', [])

    velocity_dict = dict(velocity_data)
    acceleration_dict = dict(acceleration_data)
    try:
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            headers = ['time', 'velocity', 'acceleration']
            writer.writerow(headers)

            for time in sorted(set(velocity_dict.keys())):
                velocity = velocity_dict.get(time, '')
                acceleration = acceleration_dict.get(time, '')
                writer.writerow([time, velocity, acceleration])
            writer.writerow([])
            writer.writerow(['Results:'])
            for key, value in results_data.items():
                if key in ['max_force_time', 'max_force', 'work_done']:
                    writer.writerow([key.replace("_", " ").capitalize(), value])
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")

    except Exception as e:
        print(f"An error occurred while writing the results: {str(e)}")
    

"""-------------------------------------------------------------------------------------------------------------------------"""

def main():
    input_file = "Project1/mechanical_data.csv"
    output_file = "analysis_results.csv"
    time_step = 0.1  # s

    try:
        # Read mechanical data
        data = read_mechanical_data(input_file)

        # Extract position and force data
        time_data = [item[0] for item in data]
        position_data = [(item[0], item[1]) for item in data]
        force_data = [(item[0], item[2]) for item in data]
      
        # Calculate velocity and acceleration
        velocity_data = calculate_velocity(position_data, time_step)
        acceleration_data = calculate_acceleration(velocity_data, time_step)

        # Find maximum force
        max_force_time, max_force = find_max_force(force_data)
        
        # Calculate work done
        work_done = calculate_work_done(force_data, position_data)
        print(work_done)
        # Prepare results
        results = {
            "velocity": velocity_data,
            "acceleration": acceleration_data,
            "max_force_time": max_force_time,
            "max_force": max_force,
            "work_done": work_done
        }

        # Write results to file
        write_results(output_file, results)
        print(f"Results written to {output_file}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()