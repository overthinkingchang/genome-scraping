import argparse

def initialize_parameters():
    parser = argparse.ArgumentParser()
    parser.add_argument('--start_id', type=int, required=True)
    parser.add_argument('--end_id', type=int, required=True)
    parser.add_argument('--output_path', type=str, required=True)
    options = parser.parse_args()
    return options