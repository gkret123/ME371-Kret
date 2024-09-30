# Gabriel Kret
# 09/19/2024
#ME-371
#Project 1 -- Book Analysis -- Template 0

import csv
import json

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
            print("CSV file has been read successfully! \n")
            return book_data
                    
    except FileNotFoundError:
        print(f"\n The file {filename} could not be found. Please check the file input and try again.")
        return []
    except Exception as e:
        print(f"Error reading the file {filename}: {e}")
        return [] 

'''--------------------------------------------------------------------------------------------------------------------'''

def calculate_discount_price(books, discount_rate):
    """
    Calculate and add discounted price for each book.
    Args:
        books (list of dict): List of book dictionaries
        discount_rate (float): Discount rate to apply
    Returns:
        list of dict: Updated list of book dictionaries with discounted price
    """
    try:
        for book in books:
            book["price"] = format((float(book["price"]) - (float(book["price"]) * (discount_rate))),'.2f')

    except (KeyError, ValueError):
        print(f"Skipping book {book.get('title', 'Unknown')} due to invalid or missing price.")

    print("Discount price has been calculated successfully! \n")
    return books


    """--------------------------------------------------------------------------------------------------------------------"""

def find_unique_genres(books):
    """
    Find unique genres from the data.
    Args:
        books (list of dict): List of book dictionaries
    Returns:
        set: Set of unique genres
    """
    try:
        unique_genres = {book['genre'] for book in books if 'genre' in book}
        print("Unique genres found successfully! \n")
        return unique_genres 
    except KeyError:
        print("Cannot find unique genres. Invalid key.")
        return set()
    except Exception as e:
        print(f"Error finding unique genres: {e}")
        return set()

    """--------------------------------------------------------------------------------------------------------------------"""

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
    try:
        books_in_range = list(filter(lambda x: int(x["year"]) <= end_year and int(x["year"]) >= start_year, books))
        print("Books have been filtered by year successfully! \n")
        return books_in_range
    except KeyError:
        print("Cannot filter by year. Invalid key.")
        return []
    except ValueError:
        print("Cannot convert year to numeric value for filtering.")
        return []
    except Exception as e:
        print(f"Error filtering books by year: {e}")
        return []

"""--------------------------------------------------------------------------------------------------------------------"""

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
    try:
        sorted_books = sorted(books, key=lambda book: float(book[sort_by]), reverse=reverse) 
        print("Books have been sorted successfully! \n")
        return sorted_books
    
    except KeyError:
        print(f"Cannot sort by {sort_by}. Invalid key.")
        return []
    except ValueError:
        print(f"Cannot convert field {sort_by} to numeric value for sorting.")
        return []
    


"""--------------------------------------------------------------------------------------------------------------------"""

def find_most_prolific_author(books):
    """
    Find the author with the most books in the dataset.
    Args:
        books (list of dict): List of book dictionaries
    Returns:
        str: Name of the most prolific author
    """
    author_count = {}
    try:
        if not books:
            print("The book list is empty. No prolific author found.")
            return None
        
        for book in books:
            author = book['author']
            
            if author in author_count:
                author_count[author] += 1
            
            else:
                author_count[author] = 1

        if not author_count:
            print("No valid authors found in the dataset.")
            return None
        
        most_prolific_author = max(author_count, key=author_count.get)
        print("Most prolific author has been found successfully! \n The most prolific author is: ", most_prolific_author, "\n")
        return most_prolific_author
    except Exception as e:
        print(f"Error finding most prolific author: {e}")

"""--------------------------------------------------------------------------------------------------------------------"""

def calculate_average_price_by_genre(books):
    """
    Calculate average book price for each genre.
    Args:
        books (list of dict): List of book dictionaries
    Returns:
        dict: Dictionary of average prices by genre
    """
    genre_prices = {}
    genre_counts = {} 
    try:
        for book in books:
            genre = book['genre']
            price = float(book['price'])
    #loop through the books and calc avg price for each genre
            if genre in genre_counts:
                genre_counts[genre] += 1
                genre_prices[genre] += price
            else: 
                genre_counts[genre] = 1
                genre_prices[genre] = price

        average_prices = {genre: format(float(genre_prices[genre] / genre_counts[genre]), '.2f') for genre in genre_prices}
        print("Average prices by genre have been calculated successfully! \n")
        return average_prices
    except ZeroDivisionError:
        print("Cannot calculate average price for genre with no books.")
        return {}

"""--------------------------------------------------------------------------------------------------------------------"""

def generate_book_report(books, output_filename):
    """
    Generate a formatted report of books and their properties.
    Args:
        books (list of dict): List of book dictionaries
        output_filename (str): Name of the output text file
    """
    try:
        with open(output_filename, 'w') as file:
            for book in books:
                file.write(str(book) + '\n')
        print("Book report has been generated successfully! \n")

    except FileNotFoundError:
        print(f"Error writing to file {output_filename}.")
    except Exception as e:
        print(f"Error generating book report: {e}")


"""--------------------------------------------------------------------------------------------------------------------"""

def update_book_properties(books, updates):
    """
    Update book properties based on provided updates.
    Args:
        books (list of dict): List of book dictionaries
        updates (dict): Dictionary of updates for books
    Returns:
        list of dict: Updated list of book dictionaries
    """
    for book in books:
        
        if 'title' not in book:
            raise ValueError(f"Book {book} does not contain ana 'title' key.")
        
        book_title = book.get('title')

        for title in updates:
            if title not in [book['title'] for book in books]:
                raise ValueError(f"Title '{title}' not found in the books database.")
        
        if book_title in updates:
            update_info = updates[book_title]
            if not isinstance(update_info, dict):
                raise ValueError(f"Updates for book with Title {book_title} must be a dictionary. Found: {type(update_info)}")
            
            for key, value in update_info.items():
                book[key] = value
            print(f"Book: {book_title} has been updated successfully! \n")

    return books
    
"""--------------------------------------------------------------------------------------------------------------------"""

def convert_currency(books, exchange_rate):
    """
    Convert book prices to a different currency.
    Args:
        books (list of dict): List of book dictionaries
        exchange_rate (float): Exchange rate to apply
    Returns:
        list of dict: Updated list of book dictionaries with converted prices
    """
    try:
        for book in books:
            book['price'] = format(float(book['price']) * exchange_rate, '.2f')
        print("Currency conversion has been completed successfully! \n")

    except TypeError:
        print("The exchange rate must be a float value.")
    except Exception as e:
        print(f"Error during currency conversion: {e}")
    return books
"""--------------------------------------------------------------------------------------------------------------------"""


def main():
    input_file = "Project1/books.csv"
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
        updates = {'Book 1': {'year': 1960}, 'Book 2': {'price': 12.99}}
        books = update_book_properties(books, updates)
        books = convert_currency(books, 0.85)  # Convert to GBP
        
        print(f"Analysis complete. Report generated: {output_file}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()