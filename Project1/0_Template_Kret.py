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
    for book in range(len(books)):
        
        book["price"] = format((float(book["price"]) - (float(book["price"]) * (discount_rate/100))),'.2f')

        print(book)
    # TODO: Implement discounted price calculation
    return books
    pass
book_data_discount = calculate_discount_price(book_data, 10)
print(f'Here is a list of dictionaries containg books and their properties with a discount applied: "\n" {book_data_discount} "\n"')








def find_unique_genres(books):
    """
    Find unique genres from the data.
    Args:
        books (list of dict): List of book dictionaries
    Returns:
        set: Set of unique genres
    """
    unique_genres = set()
    
    for book in books:
        # Get the genre, assuming it's stored under the key 'genre'
        genre = book.get('genre')
        if genre:
            unique_genres.add(genre)
    
    return unique_genres

print(find_unique_genres(book_data))





def filter_books_by_year(books, start_year, end_year):
    """
    Filter books based on publication year range.
    Args:
        books (list of dict): List of book dictionaries
        start_year (int): Start year of the range
        end_year (int): End year of the range
    Returns:
        list of dict: Filtered list of book dictionaries
    """
    books_in_range = list(filter(lambda x: x["year"] < end_year and x["year"] > start_year, books))
    # TODO: Implement book filtering by year
    pass

def sort_books(books, sort_by, reverse=False):
    """
    Sort books based on a specified property.
    Args:
        books (list of dict): List of book dictionaries
        sort_by (str): Property to sort by
        reverse (bool): Sort in descending order if True
    Returns:
        list of dict: Sorted list of book dictionaries
    """
    # TODO: Implement book sorting
    pass

def find_most_prolific_author(books):
    """
    Find the author with the most books in the dataset.
    Args:
        books (list of dict): List of book dictionaries
    Returns:
        str: Name of the most prolific author
    """
    # TODO: Implement finding the most prolific author
    pass

def calculate_average_price_by_genre(books):
    """
    Calculate average book price for each genre.
    Args:
        books (list of dict): List of book dictionaries
    Returns:
        dict: Dictionary of average prices by genre
    """
    # TODO: Implement average price calculation by genre
    pass

def generate_book_report(books, output_filename):
    """
    Generate a formatted report of books and their properties.
    Args:
        books (list of dict): List of book dictionaries
        output_filename (str): Name of the output text file
    """
    # TODO: Implement report generation
    pass

def update_book_properties(books, updates):
    """
    Update book properties based on provided updates.
    Args:
        books (list of dict): List of book dictionaries
        updates (dict): Dictionary of updates for books
    Returns:
        list of dict: Updated list of book dictionaries
    """
    # TODO: Implement book property updates with error handling
    pass

def convert_currency(books, exchange_rate):
    """
    Convert book prices to a different currency.
    Args:
        books (list of dict): List of book dictionaries
        exchange_rate (float): Exchange rate to apply
    Returns:
        list of dict: Updated list of book dictionaries with converted prices
    """
    # TODO: Implement currency conversion with error handling
    pass

def main():
    input_file = "books.csv"
    output_file = "book_analysis_report.txt"
    
    try:
        # Load data
        books = load_book_data(input_file)
        
        # Process data
        books = calculate_discount_price(books, 0.1)  # 10% discount
        unique_genres = find_unique_genres(books)
        
        # Perform analysis
        recent_books = filter_books_by_year(books, 2000, 2023)
        sorted_books = sort_books(books, 'price', reverse=True)
        top_author = find_most_prolific_author(books)
        
        # Generate statistics
        avg_prices = calculate_average_price_by_genre(books)
        
        # Generate report
        generate_book_report(books, output_file)
        
        # Perform updates and conversions
        updates = {'To Kill a Mockingbird': {'year': 1960}, 'Pride and Prejudice': {'price': 12.99}}
        books = update_book_properties(books, updates)
        books = convert_currency(books, 0.85)  # Convert to GBP
        
        print(f"Analysis complete. Report generated: {output_file}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
