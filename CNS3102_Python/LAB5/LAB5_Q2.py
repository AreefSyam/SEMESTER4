#'a' mode: This mode is used to open a file in append mode.
#If the file already exists, the data is written at the end of the file.
#If the file doesn't exist, a new file is created.
#You can open a file in append mode using the 'a' mode.
#
#'x' mode: This mode is used to create a new file and open it for writing.
#If the file already exists, it raises a FileExistsError exception.
#You can use the 'x' mode to create a new file only if the file doesn't already exist.
#
#'r' mode: This mode is used to open a file for reading.
#If the file doesn't exist, a FileNotFoundError exception is raised.
#You can use the 'r' mode to read the contents of an existing fil


def create_file(file_name):

    """
    Create a new file with the given name
    """
    with open(file_name, 'x') as f:
            print(f"File '{file_name}' created successfully.")


def check_file_exists(file_name):
    """
    Check if the file already exists or not
    """
    try:
        with open(file_name, 'r'):
            print(f"File '{file_name}' exists.")
            return 1
    except FileNotFoundError:
        return 0


def append_data_on_file(file_name, data):
    """
    Append the file with new data
    """

    try:
        with open(file_name, 'a') as f:
            f.write(data + "\n")
            print(f"Data appended to the file '{file_name}' successful.")
    except FileNotFoundError:
        print(f"File '{file_name}' does not exist.")


# Test File and Function

file_name = "example.txt"
if check_file_exists(file_name) == 0:
    create_file(file_name)

append_data_on_file(file_name, "This is the first line of data.")