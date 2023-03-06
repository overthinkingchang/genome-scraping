import argparse

def initialize_parameters():
    parser = argparse.ArgumentParser()
    parser.add_argument('--start_id', type=int, required=True)
    parser.add_argument('--end_id', type=int, required=True)
    parser.add_argument('--output_path', type=str, required=True)
    
    options, unknown_args = parser.parse_known_args()
    return options, unknown_args

def file_input():
    parser = argparse.ArgumentParser()
    parser.add_argument('--filepath', type=str, required=True)
    parser.add_argument('--output_path', type=str, required=True)
    input_file = parser.parse_args()
    return input_file


def option():
    operation_choices = ['list', 'loop']
    parser = argparse.ArgumentParser()
    parser.add_argument("--input",
                    choices = operation_choices,
                    default = operation_choices[0],
                    required = True)
    input_options = parser.parse_args()
    return input_options 

