import csv

def modify_csv(input_file, output_file, modify_func):
    """
    Reads data from `input_file`, applies `modify_func` to each row,
    and writes the modified data to `output_file`.

    Parameters:
    - input_file (str): The path to the input CSV file.
    - output_file (str): The path to the output CSV file.
    - modify_func (function): A function that takes a row (dict) and modifies it in place.

    """
    # Open the input CSV file for reading
    with open(input_file, 'r') as infile:
        reader = csv.DictReader(infile)
        
        # Open the output CSV file for writing
        with open(output_file, 'w', newline='') as outfile:
            # Get fieldnames from the reader and write headers to the output file
            fieldnames = reader.fieldnames
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()

            # Modify data row by row
            for row in reader:
                modify_func(row)  # Apply the modification function to each row
                writer.writerow(row)

    print(f"Data has been modified and written to {output_file}")
