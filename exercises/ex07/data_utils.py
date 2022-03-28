"""Some helpful utility functions for working CSV files."""
__author__ = "730479707"


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a table."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
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


def head(N: dict[str, list[str]], row: int) -> dict[str, list[str]]:
    """See just the first few rows."""
    empty: dict[str, list[str]] = {}
    for column in N:
        list_1: list = []
        i: int = 0
        if row > len(N[column]):
            row = len(N[column])
        while i < row:
            list_1.append(N[column][i])
            i = i + 1
        empty[column] = list_1 
    return empty 


def select(fun: dict[str, list[str]], never: list[str]) -> dict[str, list[str]]:
    """Select only columns we care about."""
    empty: dict[str, list[str]] = {}
    for column in never:
        empty[column] = fun[column]
    return empty


def concat(one: dict[str, list[str]], two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table from two column-based tables."""
    empty: dict[str, list[str]] = {}
    for column_one in one:
        empty[column_one] = one[column_one]
    for column in two:
        if column in empty:
            i: int = 0
            while i < len(two[column]): 
                empty[column].append(two[column][i])
                i = i + 1
        else:
            empty[column] = two[column]
    return empty


def count(xs: list[str]) -> dict[str, int]:
    """List values in function is keys, while the number of times they appear are values."""
    empty = dict[str, int]() 
    for i in xs:
        if i in empty:
            empty[i] += 1
        else:
            empty[i] = 1
    return empty
