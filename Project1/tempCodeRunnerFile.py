import csv
import json


book_data = []

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
            book_data = [row for row in reader]
            return book_data
        
    except FileNotFoundError:
        print(f"'\n' The file {filename} could not be found. Please check the file input and try again.") 

    # TODO: Implement CSV file reading
    pass
book_data = load_book_data('Project1/books.csv')
print(f'Here is a list of dictionaries containg books and their properties: "\n" {book_data} "\n" ')



def calculate_discount_price(books, discount_rate):
    """
    Calculate and add discounted price for each book.
    Args:
        books (list of dict): List of book dictionaries
        discount_rate (float): Discount rate to apply
    Returns:
        list of dict: Updated list of book dictionaries with discounted price
    """
    for book in books:
        
        book["price"] = format((float(book["price"]) - (float(book["price"]) * (discount_rate/100))),'.2f')

        print(book)
    # TODO: Implement discounted price calculation
    return books
    
    pass
book_data_discount = calculate_discount_price(book_data, 10)
print(f'Here is a list of dictionaries containg books and their properties with a discount applied: "\n" {book_data_discount} "\n"')





genres = {}
def find_unique_genres(books):
    """
    Find unique genres from the data.
    Args:
        books (list of dict): List of book dictionaries
    Returns:
        set: Set of unique genres
    """
    for book in books:
        genres_list = book.get("genre")
        genres.update(genres_list)

    return genres
    # TODO: Implement unique genres extraction
    pass
print(find_unique_genres(book_data))


