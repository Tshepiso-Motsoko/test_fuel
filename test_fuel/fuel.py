# Import necessary modules
import csv
import sys

def main():
    # Check the number of command-line arguments
    if len(sys.argv) != 3:
        # Print usage message if arguments are not exactly 2
        print("Usage: python scourgify.py input.csv output.csv")
        # Exit with an error
        sys.exit(1)

    # The first command-line argument is the input file
    input_file = sys.argv[1]
    # The second command-line argument is the output file
    output_file = sys.argv[2]

    # Attempt to open the input file and read data
    try:
        with open(input_file, 'r') as csvfile:
            # Use csv.DictReader for easy access to fields
            reader = csv.DictReader(csvfile)

            # Open the output file to write cleaned data
            with open(output_file, 'w') as output:
                # The new csv will have three columns: first, last, and house
                fieldnames = ['first', 'last', 'house']
                writer = csv.DictWriter(output, fieldnames=fieldnames)

                # Write the header row
                writer.writeheader()
                # Loop over rows in the input csv
                for row in reader:
                    # Split the name into last and first
                    name = row['name'].split(',')
                    first = name[1].strip()
                    last = name[0].strip()
                    # Get the house
                    house = row['house']
                    # Write the new row to the output csv
                    writer.writerow({'first': first, 'last': last, 'house': house})

    # Catch the FileNotFoundError if input file is not found
    except FileNotFoundError:
        # Print an error message and exit
        print(f"Could not read {input_file}")
        sys.exit(1)

# If this file is executed directly, run the main function
if __name__ == "__main__":
    main()
