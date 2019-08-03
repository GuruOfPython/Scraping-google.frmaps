from utils import *
from settings import *

class Main_Scraper():
    def __init__(self):
        self.save_directory = os.getcwd() + '/Result'

        if not os.path.exists(self.save_directory):
            os.makedirs(self.save_directory)

        result_file_name = self.save_directory + '/first_result.csv'
        self.create_result_file(result_file_name=result_file_name)

        self.names_list = []
        self.total_cnt = 0

    def start_requests(self):
        self.browser_launch()
        start_url = "https://www.google.com/maps/search/kinésithérapeute+75001"
        self.first_driver.get(start_url)

        self.keyword = "kinésithérapeute 75001"
        self.get_names()

        for i, name in enumerate(self.names_list):
            self.get_details(search_name=name)

    def get_names(self):
        WebDriverWait(self.first_driver, 30).until(
            EC.presence_of_all_elements_located(
                (By.XPATH,
                 '//h3[@class="section-result-title"]/span'))
        )

        rows = self.first_driver.find_elements_by_xpath('//h3[@class="section-result-title"]/span')

        for i, row in enumerate(rows):
            print("{}".format(row.text))
            self.names_list.append(row.text)
        try:
            next_btn = self.first_driver.find_element_by_xpath('//button[contains(@aria-label,"Next page")]')
            next_btn.click()
            time.sleep(3)
            self.get_names()
        except:
            pass

    def get_details(self, search_name):
        search_name_1 = search_name + ' 75001'
        try:
            WebDriverWait(self.first_driver, 20).until(
                EC.element_to_be_clickable(
                    (By.XPATH,
                     '//input[@id="searchboxinput"]'))
            )

            searchbox_input = self.first_driver.find_element_by_xpath('//input[@id="searchboxinput"]')
            searchbox_input.clear()
            action_chain = ActionChains(self.first_driver)
            action_chain.click(searchbox_input).send_keys(search_name_1).send_keys(Keys.ENTER).perform()
            time.sleep(1)

            WebDriverWait(self.first_driver, 30).until(
                EC.presence_of_all_elements_located(
                    (By.XPATH,
                     '//h1[@class="section-hero-header-title" and text()="{}"]'.format(search_name)))
            )

            tree = html.fromstring(self.first_driver.page_source)
            try:
                NAME = tree.xpath('//h1[@class="section-hero-header-title"]/text()')[0].strip()
            except:
                NAME = ""
            try:
                URL = self.first_driver.current_url
            except:
                URL = ""
            try:
                ADDRESS = tree.xpath('//span[contains(@class, "maps-sprite-pane-info-address")]/../following-sibling::span[@class="section-info-text"]//text()')[0].strip()
            except:
                ADDRESS = ""
            try:
                LAT = URL.split('/')[6].replace('@', '').split(',')[0]
            except:
                LAT = ""
            try:
                LNG = URL.split('/')[6].replace('@', '').split(',')[1]
            except:
                LNG = ""
            try:
                REVIEWS = tree.xpath('//button[@jsaction="pane.rating.moreReviews"]/text()')[0].split(' ')[0]
            except:
                REVIEWS = ""
            try:
                SCORE = tree.xpath('//span[@class="section-star-display"]/text()')[0]
            except:
                SCORE = ""
            try:
                PHONE = tree.xpath('//span[contains(@class,"maps-sprite-pane-info-phone")]/../following-sibling::span[@class="section-info-text"]//text()')[0]
            except:
                PHONE = ""

            PHONE = PHONE.replace('Add phone number', '').strip()
            try:
                WEBSITE = tree.xpath('//span[contains(@class,"maps-sprite-pane-info-website")]/../following-sibling::span[@class="section-info-text"]//text()')[0]
            except:
                WEBSITE = ""

            WEBSITE = WEBSITE.replace('Add website', '').strip()

            self.total_cnt += 1
            result_row = [
                self.total_cnt, self.keyword, NAME, URL, ADDRESS, LAT, LNG, REVIEWS, SCORE, PHONE, WEBSITE
            ]
            print("[Details {}] {}".format(self.total_cnt, result_row))
            self.insert_row(result_row=result_row)
        except:
            pass

    def browser_launch(self):
        self.first_driver = webdriver.Chrome(options=CHROME_OPTIONS,
                                             executable_path="WebDriver/chromedriver.exe")
        self.first_driver.set_page_load_timeout(1000)

    def close_browser(self):
        try:
            self.first_driver.quit()
        except:
            pass

    def create_result_file(self, result_file_name):
        heading = [
            "ID", "KEYWORD", "NAME", "URL", "ADDRESS", "LAT", "LNG", "REVIEWS", "SCORE", "PHONE", "WEBSITE"
        ]

        import codecs
        self.result_file = codecs.open(result_file_name, "w", "utf-8")
        self.result_file.write(u'\ufeff')
        self.insert_row(result_row=heading)

    def insert_row(self, result_row):
        result_row = [str(elm) if elm else "" for elm in result_row]
        result_row = [elm.replace('"', '""') for elm in result_row]
        self.result_file.write('"' + '","'.join(result_row) + '"' + "\n")
        self.result_file.flush()

if __name__ == '__main__':
    app = Main_Scraper()
    app.start_requests()