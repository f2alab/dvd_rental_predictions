

# Draw a line of stars with a specified character and margin
from pandas import DataFrame


def draw_stars_line(n=50, char='*', margin=2):
    """
    Draw a line of stars with a specified character and margin.
    Parameters:
    n (int): Number of characters to print.
    char (str): Character to print.
    margin (int): Number of new lines to print after the line.
    Returns:
    None
    """
    padding  = "\n" * margin

    print(f"{padding}{char * n}", end= padding if margin > 0 else '')


# Searc specific string in columns of a DataFrame
def search_string_in_columns(df : DataFrame, search_string: str) -> list:
    """
    Search for a specific string in all columns of a DataFrame.
    Parameters:
    df (pd.DataFrame): The DataFrame to search in.
    search_string (str): The string to search for.
    Returns:
    list: A list of columns contains search_string.
    """
    return [col for col in df.columns if search_string in col]