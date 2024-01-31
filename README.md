# RISC-V
# List Processing Program

## Description

This Python program accepts a list of integers from the user and processes it according to the following criteria:

1. Accepts a list of integers from the user.
2. Emits an error message if the length of the list is not a multiple of 10.
3. Returns or prints a list of integers based on the input list, with items at positions that are multiples of 2 or 3 removed.

The program ensures that the input list length is a multiple of 10. If not, it raises a ValueError with an appropriate error message.

The program includes a `process_list` function that implements the processing logic based on the given criteria.

## Usage

1. Run the Python script `list_processing.py`.
2. Enter a list of integers when prompted.
3. The program will process the input list and print the processed list if it meets the criteria. If the input list length is not a multiple of 10, it will emit an error message.

## Testing

The program includes a robust testing suite using the `unittest` module to ensure the correctness of the `process_list` function. The tests cover various scenarios, including valid input, invalid input (length not a multiple of 10), and an empty input list.

To run the tests:
python -m unittest list_processing.py
Feel free to contribute or raise any issues in the repository.
