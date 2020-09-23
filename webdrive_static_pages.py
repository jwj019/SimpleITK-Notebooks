import time
from subprocess import Popen, PIPE, STDOUT
import os
from selenium import webdriver

current_dir = os.getcwd()
ipynb_dir = os.path.abspath('./Python')
html_dir = os.path.abspath('./Python_html')

print(html_dir)

notebook_run = Popen(["python3","-m","jupyter", "notebook","Python/00_Setup.ipynb", "--NotebookApp.password=''", "--NotebookApp.token=''"], stdout=PIPE)


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_experimental_option("prefs", {
  "download.default_directory": html_dir,
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing_for_trusted_sources_enabled": False,
  "safebrowsing.enabled": False
})

driver = webdriver.Chrome(options=chrome_options)  # Optional argument, if not specified will search path.
driver.get('http://localhost:8888/notebooks/00_Setup.ipynb')
time.sleep(5) # Let the user actually see something!
driver.find_element_by_id("login_submit").click()
time.sleep(10)
cell_mnu = driver.find_element_by_id("celllink").click()
time.sleep(10)
run_cells = driver.find_element_by_id("run_all_cells").click()
time.sleep(120)
file_menu = driver.find_element_by_id("filelink").click()
time.sleep(10)
download_menu = driver.find_element_by_xpath("//a[text()='Download as']").click()
time.sleep(10)
download_html = driver.find_element_by_id("download_html").click()
# print(driver.get("http://localhost:8888/nbconvert/html/00_Setup.ipynb?download=true"))
time.sleep(10)


# search_box = driver.find_element_by_name('q')
# search_box.send_keys('ChromeDriver')
# search_box.submit()
# print(search_box)
notebook_run.stdout.close()
time.sleep(5) # Let the user actually see something!
driver.quit()