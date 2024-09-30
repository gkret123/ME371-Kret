# Gabriel Kret
# 09/29/2024
#ME-371
#Project 1 -- Beam Analysis -- Template 2

import csv
import math

def read_beam_data(filename):
    """
    Read beam data from a CSV file.
    
    Args:
    filename (str): Name of the CSV file
    
    Returns:
    tuple: (length, width, height, elastic_modulus, loads)
    where loads is a list of tuples (position, magnitude)
    """
    
    
    try:
        with open(filename, 'r') as file:
            properties_reader = csv.DictReader(file)
            data = [row for row in properties_reader]
            length = float(data[0]["length"])
            width = float(data[0]["width"])
            height = float(data[0]["height"])
            elastic_modulus = float(data[0]["elastic_modulus"])
            loads = [(float(row["length"]), float(row["width"])) for row in data[1:]]

            return (length, width, height, elastic_modulus, loads)
            
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        return []

"""-----------------------------------------------------------------------------------------------------------------"""

def calculate_bending_moment(length, loads):
    """
    Calculate the maximum bending moment in the beam.
    
    Args:
    length (float): Length of the beam
    loads (list): List of (position, magnitude) tuples for each load
    
    Returns:
    float: Maximum bending moment
    """
    try:

        for i in range(len(loads)):
            loads[i] = (float(loads[i][0]), float(loads[i][1]))
        # calc reactions
        R1 = sum(load[1] * (length - load[0]) / length for load in loads)
        R2 = sum(load[1] * load[0] / length for load in loads)
        print(f"Calculated reaction forces: R1 = {R1}, R2 = {R2}")
        # dont include R1 or R2 in the bending moments b/c moments arm is 0
        bending_moments = []
        for load in loads:
            x = load[0]
            M = R1 * x - sum(load_dist[1] * (x - load_dist[0]) for load_dist in loads if load_dist[0] < x)
            bending_moments.append(M)
            print(f"Bending moment at position {x}: {M}")

        max_moment = max(bending_moments)
        print(f"Maximum bending moment: {max_moment}")
        return max_moment
    
    except Exception as e:
        print(f"An error occurred while calculating the maximum bending moment: {str(e)}")
        return 0
"""-----------------------------------------------------------------------------------------------------------------"""

def calculate_shear_force(length, loads):
    """
    Calculate the maximum shear force in the beam.
    
    Args:
    length (float): Length of the beam
    loads (list): List of (position, magnitude) tuples for each load
    
    Returns:
    float: Maximum shear force
    """
    try:
        for i in range(len(loads)):
            loads[i] = (float(loads[i][0]), float(loads[i][1]))
        # calc reactions
        R1 = sum(load[1] * (length - load[0]) / length for load in loads)
        R2 = sum(load[1] * load[0] / length for load in loads)

        # R1 and R2 are reaction forces at ends AND are representative of the shears
        shear_forces = [R1, R2]
        for load in loads:
            x = load[0]
            # V = R1 - sum of all loads left of x
            V = R1 - sum(load_dist[1] for load_dist in loads if load_dist[0] < x)
            shear_forces.append(V)
            print(f"Shear force at position {x}: {V}")

        max_shear = max(shear_forces)
        print(f"Maximum shear force: {max_shear}")
        return max_shear
        
    except Exception as e:
        print(f"An error occurred while calculating the maximum shear force: {str(e)}")
        return 0

"""-----------------------------------------------------------------------------------------------------------------"""

def calculate_max_bending_stress(max_moment, moment_of_inertia, y_max):
    """
    Calculate the maximum bending stress in the beam.
    
    Args:
    max_moment (float): Maximum bending moment
    moment_of_inertia (float): Moment of inertia of the beam cross-section
    y_max (float): Distance from neutral axis to extreme fiber
    
    Returns:
    float: Maximum bending stress
    """
    try:
        #sigma = M * y / I
        max_bending_stress = max_moment * y_max / moment_of_inertia
        return max_bending_stress
    
    except ZeroDivisionError:
        print("Error: Moment of Inertia cannot be zero.")
        return 0
    except Exception as e:
        print(f"An error occurred while calculating the maximum bending stress: {str(e)}")
        return 0

"""-----------------------------------------------------------------------------------------------------------------"""

def calculate_max_shear_stress(max_shear, first_moment, moment_of_inertia, width):
    """
    Calculate the maximum shear stress in the beam.
    
    Args:
    max_shear (float): Maximum shear force
    first_moment (float): First moment of area of the beam cross-section
    moment_of_inertia (float): Moment of inertia of the beam cross-section
    width (float): Width of the beam at the neutral axis
    
    Returns:
    float: Maximum shear stress
    """
    try:
        #tau = V * Q / (I * b)
        tau = max_shear * first_moment / (moment_of_inertia * width)
        return tau
    
    except ZeroDivisionError:
        print("Error: Width and/or Moment of Inertia cannot be zero.")
        return 0
    except Exception as e:
        print(f"An error occurred while calculating the maximum shear stress: {str(e)}")
        return 0

"""-----------------------------------------------------------------------------------------------------------------"""

def calculate_max_deflection(length, loads, elastic_modulus, moment_of_inertia):
    """
    Calculate the maximum deflection of the beam.
    
    Args:
    length (float): Length of the beam
    loads (list): List of (position, magnitude) tuples for each load
    elastic_modulus (float): Elastic modulus of the beam material
    moment_of_inertia (float): Moment of inertia of the beam cross-section
    
    Returns:
    float: Maximum deflection
    """
    try:
    # homemade linspace func
        start = 0.0
        stop = length
        step = 0.01  
        x_values = []
        current = start
        while current <= stop:
            x_values.append(round(current, 2))
            current += step
        
        total_deflection = [0.0 for _ in x_values]
        E = elastic_modulus
        I = moment_of_inertia
        L = length

        for load in loads:
            a = load[0]
            b = L - a
            P = load[1]

            for id_x, x in enumerate(x_values):
                if x <= a:
                    y = ((P * b) / (6 * E * I * L)) * (x**3 - (L**2 - b**2)*x)
                else:  # x > a
                    y = ((P * a) / (6 * E * I * L)) * ((L-x)**3 - ((L**2 - a**2)*(L-x)))
                print(f"Deflection at load {load} x = {x}: {y}")
                total_deflection[id_x] += y  # sum deflections from all loads at each point on beam
            
        # Find the maximum deflection
        max_defl = min(total_deflection)
        max_defl_idx = total_deflection.index(max_defl)
        x_max = x_values[max_defl_idx]
        print(f"Maximum deflection: {max_defl} meters at x = {x_max} meters")
        
        return max_defl
    except ZeroDivisionError:
        print("Error: Moment of Inertia, Modulus of Elasticity, and/or Length cannot be zero.")
        return 0
    except Exception as e: 
        print(f"An error occurred while calculating the maximum deflection: {str(e)}")
        return 0

"""-----------------------------------------------------------------------------------------------------------------"""

def write_results(filename, results_data):
    """
    Write calculation results to a CSV file.
    
    Args:
    filename (str): Name of the output CSV file
    results_data (dict): Dictionary containing results to be written
    """
    try:
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['Parameter', 'Value']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for key, value in results_data.items():
                writer.writerow({'Parameter': key, 'Value': value})
        print(f"Results successfully written to {filename}")
   
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")

    except Exception as e:
        print(f"An error occurred while writing the results: {str(e)}")

"""-----------------------------------------------------------------------------------------------------------------"""

def main():
    input_file = "Project1/beam_data.csv"
    output_file = "beam_analysis_results.csv"

    try:
        # Read beam data
        length, width, height, elastic_modulus, loads = read_beam_data(input_file)

        # Calculate beam properties
        moment_of_inertia = (width * height**3) / 12
        y_max = height / 2
        first_moment = (width * height**2) / 8

        # Perform calculations
        max_moment = calculate_bending_moment(length, loads)
        max_shear = calculate_shear_force(length, loads)
        max_bending_stress = calculate_max_bending_stress(max_moment, moment_of_inertia, y_max)
        max_shear_stress = calculate_max_shear_stress(max_shear, first_moment, moment_of_inertia, width)
        max_deflection = calculate_max_deflection(length, loads, elastic_modulus, moment_of_inertia)

        # Prepare results
        results = {
            "max_bending_stress": max_bending_stress,
            "max_shear_stress": max_shear_stress,
            "max_deflection": max_deflection
        }

        # Write results to file
        write_results(output_file, results)
        print(f"Results written to {output_file}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()