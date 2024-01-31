import unittest

def process_list(input_list):
    if len(input_list) % 10 != 0:
        raise ValueError("Input list length must be a multiple of 10")

    output_list = [x for i, x in enumerate(input_list) if (i + 1) % 2 != 0 and (i + 1) % 3 != 0]
    return output_list

class TestProcessList(unittest.TestCase):
    def test_valid_input(self):
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        expected_output = [1, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20]
        self.assertEqual(process_list(input_list), expected_output)

    def test_invalid_input(self):
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        with self.assertRaises(ValueError):
            process_list(input_list)

    def test_empty_input(self):
        input_list = []
        self.assertEqual(process_list(input_list), [])

if __name__ == "__main__":
    try:
        input_list = list(map(int, input("Enter a list of integers: ").split()))
        processed_list = process_list(input_list)
        print("Processed list:", processed_list)
    except ValueError as ve:
        print("Error:", ve)
