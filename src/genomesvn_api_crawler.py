import requests
import json
import csv
from constants.constant_variables import API_URL, COLUMN_LIST
from src.genomesvn_crawler_helper import create_rsid_list, initialize_parameters


def is_not_found(dict1):
    return ('err' in dict1)

def get_info_from_api(json_data, reference_genome):
    rows = []
    alt = json_data['snp']['alt']
    for i in range(len(alt)):
        rsid = json_data['snp']['rsid']
        ref = json_data['snp']['ref']
        pos = json_data['snp']['pos']
        chrom = json_data['snp']['chrom']
        allele = alt[i]['allele']
        AAchange = alt[i]['info']['AA Change']
        Gene = alt[i]['info']['Gene']
        Impact = alt[i]['info']['Impact']
        KHV = alt[i]['info']['KHV']
        KHVG = alt[i]['info']['KHV-G']
        Region = alt[i]['info']['Region']
        rows.append([chrom, pos, rsid, ref, allele, KHV,
                      KHVG, Region, Gene, Impact, AAchange, reference_genome])
    return rows

def get_rsid_info_from_api(data, rsid, reference_genome):
    info_row = [['None', 'None', rsid, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', reference_genome]]
    parse_json = json.loads(data)
    if is_not_found(parse_json) == False:
        info_row = get_info_from_api(parse_json, reference_genome)
    return info_row

def query_by_api(options, rsid_list):
    with open(options.output_path, mode='w') as output_file:
        output_writer = csv.writer(output_file, delimiter=',')
        output_writer.writerow(COLUMN_LIST)
        for rsid in rsid_list:
            response_API = requests.get(
                API_URL + rsid + '&ref='+options.reference_genome)
            data = response_API.text
            rsid_info = get_rsid_info_from_api(data, rsid, options.reference_genome)
            output_writer.writerows(rsid_info)
        output_file.close()

def main():
    options = initialize_parameters()
    rsid_list = create_rsid_list(options)
    if rsid_list:
        query_by_api(options, rsid_list)
    else:
        raise Exception('Please provide rsid list by input file or start-end id.')

if __name__ == "__main__":
    main()
