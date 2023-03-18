import argparse


def initialize_parameters():
    parser = argparse.ArgumentParser()
    parser.add_argument('--start_id', type=int, 
                        default=None,
                        help='input start rsid. For example, if rs61737737, please use --start_id 61737737')
    parser.add_argument('--end_id', type=int, 
                        default=None,
                        help='input end rsid. For example, if rs61737837, please use --end_id 61737837')
    parser.add_argument('--reference_genome',
                        choices=['GRCh38', 'GRCh37'],
                        default='GRCh38')
    parser.add_argument('--input_path', type=str, 
                        default='input/rsid_list.txt')
    parser.add_argument('--output_path', type=str, 
                        default='output/rsid_genomesvn.csv')
    options = parser.parse_args()
    return options

def create_rsid_list(options) -> list:
    rsid_list = None
    if options.start_id and options.end_id:
        rsid_list =  ['rs' + str(ind) for ind in range(options.start_id, options.end_id+1)]
    else:
        try:
            fi = open(options.input_path, 'r')
            rsid_list = [standardize(rsid) for rsid in fi.readlines()]
        except:
            print("Can't read input file")
    return rsid_list

def standardize(rsid: str) -> list:
    rsid = rsid.strip().lower()
    return rsid