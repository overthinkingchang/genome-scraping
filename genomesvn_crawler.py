import argparse
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pandas as pd

column_list = ['Chrom', 'Pos', 'ID', 'Ref', 'Alt', 'KHV', 'KHV-G',
               'Region', 'Gene', 'Impact', 'AAChange', 'Pos_Grch37']
df = pd.DataFrame(columns=column_list)
driver = webdriver.Chrome(r'C:\Users\DELL\Desktop\chromedriver.exe')
url = 'https://genomes.vn/'
driver.get(url)
wait = WebDriverWait(driver, 20)


def check_exists(sequence):
    driver.find_element(By.ID, "query").clear()
    driver.implicitly_wait(10)
    driver.find_element(By.ID, "query").send_keys(sequence)
    driver.find_element(By.ID, 'search-btn').click()
    driver.implicitly_wait(20)
    check_sequence = driver.find_elements(By.XPATH, "//*[@id='result']/div[1]")
    driver.implicitly_wait(20)
    return len(check_sequence) > 0


def genome_scraping(sequence):
    if (check_exists(sequence)):
        driver.find_element(
            By.XPATH, "//*[@id='main']/div[3]/label[1]/input").click()
        driver.find_element(By.ID, 'search-btn').click()
        driver.implicitly_wait(20)
        table_body_grch37 = driver.find_element(
            By.XPATH, "//*[@id='result']/div[1]/table/tbody")
        entries_grch37 = table_body_grch37.find_elements(By.TAG_NAME, 'tr')
        Pos_value_grch37 = entries_grch37[1].find_element(
            By.TAG_NAME, 'td').text
        driver.find_element(
            By.XPATH, "//*[@id='main']/div[3]/label[2]/input").click()
        driver.find_element(By.ID, 'search-btn').click()
        driver.implicitly_wait(20)
        table_body = driver.find_element(
            By.XPATH, "//*[@id='result']/div[1]/table/tbody")
        entries = table_body.find_elements(By.TAG_NAME, 'tr')
        Chrom_value = entries[0].find_element(By.TAG_NAME, 'td').text
        Pos_value = entries[1].find_element(By.TAG_NAME, 'td').text
        ID_value = entries[2].find_element(By.TAG_NAME, 'td').text
        Ref_value = entries[3].find_element(By.TAG_NAME, 'td').text
        small_table_body = driver.find_element(
            By.XPATH, "//*[@id='result']/div[1]/table/tbody/tr[5]/td/table/tbody")
        small_entries_row = small_table_body.find_elements(By.TAG_NAME, 'tr')
        for i in range(0, len(small_entries_row)):
            small_entries_index = small_entries_row[i].find_elements(
                By.TAG_NAME, 'td')
            Alt = small_entries_row[i].find_element(By.TAG_NAME, 'th').text
            KHV_value = small_entries_index[0].text
            KHVG_value = small_entries_index[1].text
            Region_value = small_entries_index[2].text
            Gene_value = small_entries_index[3].text
            Impact_value = small_entries_index[4].text
            AAChange_value = small_entries_index[5].text
            df.loc[len(df.index)] = [Chrom_value, Pos_value, ID_value, Ref_value, Alt, KHV_value, KHVG_value,
                                     Region_value, Gene_value, Impact_value, AAChange_value, Pos_value_grch37]
    # except NoSuchElementException:
    else:
        df.loc[len(df.index)] = ['None', 'None', sequence, 'None', 'None', 'None',
                                 'None', 'None', 'None', 'None', 'None', 'None']


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--start_id', type=int, required=True)
    parser.add_argument('--end_id', type=int, required=True)
    parser.add_argument('--output_path', type=str, required=True)
    args = parser.parse_args()
    start_rsid = args.start_id
    end_rsid = args.end_id
    output = args.output_path
    for rsid in range(start_rsid, end_rsid+1):
        sequence = "rs" + str(rsid)
        genome_scraping(sequence)
        print(rsid)
    df.to_csv(output)


if __name__ == "__main__":
    main()
