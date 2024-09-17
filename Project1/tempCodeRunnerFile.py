def load_book_data(filename):
    """
    Read book data from a CSV file.
    Args:
        filename (str): Name of the CSV file
    Returns:
        list of dict: List of dictionaries containing book properties
    """
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
        
    except FileNotFoundError:
        print(f"'\n' The file {filename} could not be found. Please check the file input and try again.") 

    # TODO: Implement CSV file reading
    pass
print(load_book_data('Project1/books.csv'))