"""Dictionary related utility functions."""

__author__ = "730409578"

# Define your functions below

from csv import DictReader


SAMPLE_ROW_TABLE_FOR_TESTING: list[dict[str, str]] = [{'school': 'UNC', 'location': 'Chapel Hill', 'type': '4-year'}, 
                                                      {'school': 'Duke', 'location': 'Durham', 'type': '4-year'},
                                                      {'school': 'UNC-W', 'location': 'Wilmington', 'type': '4-year'},
                                                      {'school': 'Cape Fear Community College', 'location': 'Wilmington', 'type': '2-year'},
                                                      {'school': 'Miller-Motte College', 'location': 'Wilmington', 'type': '2-year'},
                                                      {'school': 'App State', 'location': 'Asheville', 'type': '4-year'}]


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Reads the rows of a csv into a table."""
    result: list[dict[str, str]] = []
    
    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)
    
    # Close the file once we're done, to free its resources
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        result.append(row[column])
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def rowlumnar(column_table: dict[str, list[str]]) -> list[dict[str, str]]:
    """Given a column-oriented table, produce a row-oriented table."""
    result: list[dict[str, str]] = []

    # By finding the first key and taking the length of that, in while i < len(column_table[first_key]), we find out how many indexes to loop through 
    first_key: str = list(column_table)[0]

    # Works by selecting a single index, i, of the column-table, to loop though all the column headings for
    i: int = 0
    while i < len(column_table[first_key]):
        initialized: bool = False
        for column in column_table:
            # If there's no indexes in a list, then you can't just pick an index and assign a dictionary to it, even if it'll end up ordered
            # Therefore you have to set up that index with an initial key-value pair using the append method and then you can just add pairs to that dictionary
            # It works. I'm a literal genius
            if not initialized:
                result.append({column: column_table[column][i]})
                initialized = True
            else:
                result[i][column] = column_table[column][i]
        i += 1
        
    return result


def head(n: int, column_table: dict[str, list[str]] = {}, column_table_int: dict[str, list[int]] = {}) -> dict[str, list[str]] | dict[str, list[int]]:
    """Purpose: to produce a new column-based (dict[str, list[str]]) table with only the first n rows of data for each column."""
    def string(n: int) -> dict[str, list[str]]:
        result: dict[str, list[str]] = {}
        for column in column_table:
            n_results: list[str] = []  # Establishes an empty list that will become empty again after the column is looped through
            
            i: int = 0
            while i < n:  # Loops from list index 0 to the parameter number of values
                n_results.append(column_table[column][i])
                i += 1

            result[column] = n_results  # Assigns the resulting list to the key in the result dictionary
        return result

    def integer(n: int) -> dict[str, list[int]]:
        result_int: dict[str, list[int]] = {}
        for column in column_table_int:
            n_results_int: list[int] = []  # Establishes an empty list that will become empty again after the column is looped through
            
            i: int = 0
            while i < n:  # Loops from list index 0 to the parameter number of values
                n_results_int.append(column_table_int[column][i])
                
                i += 1
            
            result_int[column] = n_results_int  # Assigns the resulting list to the key in the result dictionary
        return result_int

    if column_table != {}:
        return string(n)
    else:
        return integer(n)


def select(table: dict[str, list[str]], headings: list[str]) -> dict[str, list[str]]:
    """Produces a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    
    for key in headings:
        result[key] = table[key]

    return result


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produces a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}

    for column in table1:  # Creates a new result table that matches table 1
        result[column] = table1[column]
    
    for column in table2:  # Cycles through the second table
        matches: bool = False  # A bool that will change if table 2's key matches a key in table 1
        for column_to_check in table1: 
            if column == column_to_check:  # Check to see if table 2's key matches a key in table 1
                matches = True  # If there is a match, records it by changing matches to true and adding the list from table 2 to the list from table 1
                result[column] += table2[column]
        if not matches:  # Adds the column onto the end if it didn't have a match 
            result[column] = table2[column]
    
    return result


def count(values: list[str]) -> dict[str, int]:
    """Given a list[str], produces a dict[str, int], where each key is a unique value in the given list and each value assosciated is the count of the number of times that value appeared in the input list."""
    result: dict[str, int] = {}

    for value in values:
        if value in result:
            result[value] += 1
        else:
            result[value] = 1

    return result


def list_subset(row_table: list[dict[str, str]], column: str, acceptable_values: list[str], inclusive: bool = True) -> list[dict[str, str]]:
    """Given a table in row format, a column within the table, and a list of acceptable values for that column, removes columns that don't contain the acceptable values."""
    result_table: list[dict[str, str]] = []
    i: int = 0
    
    if inclusive:
        # Runs through every row in the table
        while i < len(row_table):
            in_subset: bool = False
            ii: int = 0
            # Checks the value of that column in the row against every value in the acceptable_values list 
            while ii < len(acceptable_values):
                # If they match, and they haven't matched before, append that row to the new table
                if row_table[i][column] == acceptable_values[ii] and not in_subset:
                    in_subset = True
                    result_table.append(row_table[i])
                ii += 1
            i += 1

    else:
        # Runs through every row in the table
        while i < len(row_table):
            in_subset: bool = False
            ii: int = 0
            # Checks the value of that column in the row against every value in the acceptable_values list 
            while ii < len(acceptable_values):
                # If they don't match, and they haven't not matched before, append that row to the new table
                if row_table[i][column] == acceptable_values[ii]:
                    in_subset = True
                ii += 1
            if not in_subset:
                result_table.append(row_table[i])
            i += 1

    return result_table

# schools_not_in_wilmington: list[dict[str, str]] = list_subset(SAMPLE_ROW_TABLE_FOR_TESTING, 'location', ['Wilmington', 'Durham'], False)
# print(schools_not_in_wilmington)
# schools_in_chapel_hill: list[dict[str, str]] = list_subset(SAMPLE_ROW_TABLE_FOR_TESTING, 'location', ['Chapel Hill'], False)
# print(schools_in_chapel_hill)


def change_list_str_to_int(str_list: list[str]) -> list[int]:
    """Changes a list of type str to a list of type int."""
    result: list[int] = []

    i: int = 0
    while i < len(str_list):
        if str_list[i] == '':
            i += 1
        else:
            result.append(int(str_list[i]))
            i += 1

    return result


def multi_str_to_int(column_table: dict[str, list[str]]) -> dict[str, list[int]]:
    """Changes multiple columns of data from type str to type int."""
    return_table: dict[str, list[int]] = {}
    for column in column_table:
        return_table[column] = change_list_str_to_int(column_table[column])
    return return_table


def average_columns(column_table: dict[str, list[str]], list_keys: list[str] = ['']) -> list[float] | float:
    """Returns a list of average column values. Can take the name of an initialized list to pass the column names to."""
    averages = []

    # Converting tables of strings to tables of integers
    column_table_int: dict[str, list[int]] = multi_str_to_int(column_table)

    # Averaging the columns
    for column in column_table_int:
        averages.append(sum(column_table_int[column]) / len(column_table_int[column]))

    # If the column is just one float, convert it to a float
    if len(averages) == 1:
        averages = str(averages)
        averages = averages[1:-1]
        averages = float(averages)
 
    # Adding column names to pre-initialized list (so it will be in the previous frame)
    if list_keys != ['']:
        for column in column_table_int:
            list_keys.append(column)
        
    return averages