import time
from subprocess import Popen, PIPE, STDOUT
import os
from selenium import webdriver
import psutil
from selenium.common.exceptions import WebDriverException, NoSuchElementException

current_dir = os.getcwd()
ipynb_dir = os.path.abspath('./Python')
html_dir = os.path.abspath('./Python_html')

print(html_dir)

notebook_run = Popen(["python3","-m","jupyter", "notebook","Python/00_Setup.ipynb", "--NotebookApp.password=''", "--NotebookApp.token=''", "--NotebookApp.iopub_msg_rate_limit=2000"], stdout=PIPE)


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

for counter in range(5):
    try:
        driver = webdriver.Chrome(options=chrome_options)
        print("WebDriver and WebBrowser initialized...")
        break
    except WebDriverException:
        #Cross platform
        PROCNAME = "chromedriver"
        for proc in psutil.process_iter():
            # check whether the process name matches
            if proc.name() == PROCNAME:
                proc.kill()        
        print("Retrying driver...")

for counter in range(5):
    try:
        driver.get('http://localhost:8888/notebooks/00_Setup.ipynb')
        print("Got notebook...")
        break
    except WebDriverException:
        #Cross platform
        time.sleep(5)
        print("Retrying browser...")

# time.sleep(5) # Let the user actually see something!
# driver.find_element_by_id("login_submit").click()
time.sleep(10)
cell_mnu = driver.find_element_by_id("celllink").click()
time.sleep(10)
run_cells = driver.find_element_by_id("run_all_cells").click()
for wait_counter in range(10):
    try:
        time.sleep(10)
        print(driver.find_element_by_class_name("kernel_idle_icon"))
        print("00_Setup.ipynb done!")
        break
    except NoSuchElementException:
        print("Waiting on kernel...")

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