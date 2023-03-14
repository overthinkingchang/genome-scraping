import requests
import json 
import csv
from src.genomesvn_crawler_helper import initialize_parameters 

def err(dict1):
    return ('err' in dict1)
def info(json_data):
    result = []
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
        result.append([chrom, pos, rsid, ref, allele, KHV, KHVG, Region, Gene, Impact, AAchange])
    return result
def main():
    with open('output.csv', mode='w') as output_file:
        output_writer = csv.writer(output_file, delimiter=',')
        output_writer.writerow(['CHROM', 'POS', 'RSID', 'REF', 'ALLELE', 'KHV', 'KHVG', 'REGION', 'GENE', 'IMPACT', 'AA_CHANGE'])
        options = initialize_parameters()
        start_rsid = options.start_id
        end_rsid = options.end_id
        for rsid in range(start_rsid, end_rsid+1):
            rsid_query = "rs" + str(rsid)
            response_API = requests.get('https://genomes.vn/api/search?query='+ rsid_query + '&ref=GRCh38')
            data = response_API.text
            parse_json = json.loads(data)
            if err(parse_json):
                output_writer.writerow(['None','None',rsid_query,'None','None','None','None','None','None','None','None'])
                #os.system("echo 'None, None, $i, None, None, None, None, None, None, None, None'>> csv_data.csv")
            else:
                final_result = info(parse_json)
                output_writer.writerows(final_result)
                #info(parse_json)
        output_file.close()



if __name__ == "__main__":
    main()   
                
    
