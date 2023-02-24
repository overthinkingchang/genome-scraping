import pandas as pd
from constants.constant_variables import CHOME_DRIVER, COLUMN_LIST, URL, WAIT_LARGE_TIME
from src.genomesvn_crawler_helper import initialize_parameters

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def genome_scraping(df, driver, rsid_query):
    if (check_exists(driver, rsid_query)):
        Chrom_value, Pos_value, ID_value, Ref_value, Pos_value_grch37 = get_chr_pos_id_ref(
            driver)
        small_table_body = driver.find_element(
            By.XPATH, "//*[@id='result']/div[1]/table/tbody/tr[5]/td/table/tbody")
        small_entries_row = small_table_body.find_elements(By.TAG_NAME, 'tr')
        for i in range(0, len(small_entries_row)):
            small_entries_index = small_entries_row[i].find_elements(
                By.TAG_NAME, 'td')
            Alt = small_entries_row[i].find_element(By.TAG_NAME, 'th').text
            small_value_dict = {'KHV': 0,
                                'KHVG': 0,
                                'Region': 0,
                                'Gene': 0,
                                'Impact': 0,
                                'AAChange': 0}
            for index, key in enumerate(small_value_dict.keys()):
                small_value_dict[key] = small_entries_index[index]
            df.loc[len(df.index)] = [Chrom_value, Pos_value, ID_value, Ref_value, Alt, small_value_dict['KHV'], small_value_dict['KHVG'],
                                     small_value_dict['Region'], small_value_dict['Gene'], small_value_dict['Impact'], small_value_dict['AAChange'], Pos_value_grch37]
    else:
        df.loc[len(df.index)] = ['None', 'None', rsid_query, 'None', 'None', 'None',
                                 'None', 'None', 'None', 'None', 'None', 'None']


def check_exists(driver, rsid_query):
    driver.find_element(By.ID, "query").clear()
    driver.implicitly_wait(10)
    driver.find_element(By.ID, "query").send_keys(rsid_query)
    driver.find_element(By.ID, 'search-btn').click()
    driver.implicitly_wait(WAIT_LARGE_TIME)
    check_rsid_query = driver.find_elements(
        By.XPATH, "//*[@id='result']/div[1]")
    driver.implicitly_wait(WAIT_LARGE_TIME)
    return len(check_rsid_query) > 0


def get_chr_pos_id_ref(driver):
    driver.find_element(
        By.XPATH, "//*[@id='main']/div[3]/label[1]/input").click()
    driver.find_element(By.ID, 'search-btn').click()
    driver.implicitly_wait(WAIT_LARGE_TIME)
    table_body_grch37 = driver.find_element(
        By.XPATH, "//*[@id='result']/div[1]/table/tbody")
    entries_grch37 = table_body_grch37.find_elements(By.TAG_NAME, 'tr')
    Pos_value_grch37 = entries_grch37[1].find_element(
        By.TAG_NAME, 'td').text
    driver.find_element(
        By.XPATH, "//*[@id='main']/div[3]/label[2]/input").click()
    driver.find_element(By.ID, 'search-btn').click()
    driver.implicitly_wait(WAIT_LARGE_TIME)
    table_body = driver.find_element(
        By.XPATH, "//*[@id='result']/div[1]/table/tbody")
    entries = table_body.find_elements(By.TAG_NAME, 'tr')
    Chrom_value = entries[0].find_element(By.TAG_NAME, 'td').text
    Pos_value = entries[1].find_element(By.TAG_NAME, 'td').text
    ID_value = entries[2].find_element(By.TAG_NAME, 'td').text
    Ref_value = entries[3].find_element(By.TAG_NAME, 'td').text
    return Chrom_value, Pos_value, ID_value, Ref_value, Pos_value_grch37


def main():
    options = initialize_parameters()
    start_rsid = options.start_id
    end_rsid = options.end_id
    output = options.output_path
    df = pd.DataFrame(columns=COLUMN_LIST)
    driver = webdriver.Chrome(CHOME_DRIVER)
    driver.get(URL)
    WebDriverWait(driver, WAIT_LARGE_TIME)

    for rsid in range(start_rsid, end_rsid+1):
        rsid_query = "rs" + str(rsid)
        genome_scraping(df, driver, rsid_query)
    df.to_csv(output)


if __name__ == "__main__":
    main()
