"""Some helpful utility functions for working CSV files."""

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a table."""
    result: list[dict[str, str]] = []
    
    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # prepare to read the data file as a CSV rather than just the strings

    csv_reader = DictReader(file_handle)

    # read each row of the CSV file row by row 
    for row in csv_reader:
        result.append(row)

    # close the file when we're done, to free its resources
    file_handle.close()

    return result 


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str} of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result 


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oreitned table into a coluumn-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column) 

    return result