# Installation

## Download chromedriver
```
mkdir downloads
cd downloads
wget https://chromedriver.storage.googleapis.com/111.0.5563.19/chromedriver_linux64.zip
unzip chromedriver_linux64.zip 
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

Run script:
```
genomesvn-crawler  --start_id START_ID --end_id END_ID --output_path OUTPUT_PATH
```

optional arguments:
  -h, --help            show this help message and exit
  --start_id START_ID
  --end_id END_ID
  --output_path OUTPUT_PATH

Examples:
```
genomesvn-crawler --start_id 61737737 --end_id 61737837 --output_path output/test_csv_data.csv
```