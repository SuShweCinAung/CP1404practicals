"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"

def main():
    data = get_data()
    print(data)
    display_details()

def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data_list = []
    input_file = open(FILENAME)
    for line in input_file:
        repr(line)
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        data_list.append(parts)
    input_file.close()
    return data_list

def display_details():
    input_file = open(FILENAME)
    for line in input_file:
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])
        print("{} is taught by {:12} and has {:>3} students".format(parts[0], parts[1], parts[2]))

main()