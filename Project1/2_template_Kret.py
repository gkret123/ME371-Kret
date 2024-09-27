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
    
        R1 = sum(load[1] * (length - load[0]) / length for load in loads)
        R2 = sum(load[1] * load[0] / length for load in loads)
        print(f"Calculated reaction forces: R1 = {R1}, R2 = {R2}")

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

        R1 = sum(load[1] * (length - load[0]) / length for load in loads)
        R2 = sum(load[1] * load[0] / length for load in loads)

        shear_forces = []
        for load in loads:
            x = load[0]
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
        max_bending_stress = max_moment * y_max / moment_of_inertia
        return max_bending_stress
    
    except ZeroDivisionError:
        print("Error: Moment of Inertia cannot be zero.")
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
        print("Error: Width and/ or Moment of Inertia cannot be zero.")
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
    max_deflection = 0.0
    try:
        for position, magnitude in loads:
            
            #delta= P*x*(L−x)^2 / (6*E*I*L) (From Beer and Johnston, Mechanics of Materials)
            deflection = (magnitude * position * (length - position) * (3 * length - position)) / (6 * elastic_modulus * moment_of_inertia * length)
            max_deflection += deflection
        print(f"Maximum deflection: {max_deflection}")
        return max_deflection

    except ZeroDivisionError:
        print("Error: Moment of inertia cannot be zero.")
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