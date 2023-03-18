# Installation

## Download chromedriver
```
mkdir downloads
cd downloads
wget https://chromedriver.storage.googleapis.com/111.0.5563.19/chromedriver_linux64.zip
unzip chromedriver_linux64.zip 
sudo apt update -y
sudo apt install chromium-chromedriver -y
```

or just use:
```
chmod +x chromedriver_download.sh
bash chromedriver_download.sh
```

# Usage

## With anaconda
```
conda env create -n genomesvn python=3.8
conda activate genomesvn
```

Install poetry and packages
```
pip install poetry
poetry install
```

### Run with selenium
```
genomesvn-crawler  --start_id START_ID --end_id END_ID --output_path OUTPUT_PATH

optional arguments:
  -h, --help            show this help message and exit
  --start_id START_ID
  --end_id END_ID
  --output_path OUTPUT_PATH
```

Examples:
```
genomesvn-crawler --start_id 61737737 --end_id 61737837 --output_path output/test_csv_data.csv
```

### Run with API
```
genomesvn-api-crawler [-h] [--start_id START_ID] [--end_id END_ID] [--reference_genome {GRCh38,GRCh37}]
                             [--input_path INPUT_PATH] [--output_path OUTPUT_PATH]

optional arguments:
  -h, --help            show this help message and exit
  --start_id START_ID   input start rsid. For example, if rs61737737, please use --start_id 61737737
  --end_id END_ID       input end rsid. For example, if rs61737837, please use --end_id 61737837
  --reference_genome {GRCh38,GRCh37}
  --input_path INPUT_PATH
  --output_path OUTPUT_PATH
```

Examples:
```
genomesvn-api-crawler --input_path input/rsid_list.txt --output_path output/rsid_genomesvn.csv
```