import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k4.html"
driver.get(URL)
time.sleep(1)

# elemek kigyujtese
initial_text = driver.find_element_by_xpath('//div[@class="flex-child"]/p[3]')
chr_element = driver.find_element_by_id("chr")
op_element = driver.find_element_by_id("op")
num_element = driver.find_element_by_id("num")
submit_btn = driver.find_element_by_id("submit")

table_text = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"


def return_result():
    return driver.find_element_by_id("result")


def test_initial_state_correct():
    """ Helyesen betöltődik az applikáció:
        Megjelenik az ABCs műveleti tábla, pontosan ezzel a szöveggel:
        !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~ """
    assert initial_text.is_displayed()
    assert initial_text.text == table_text


def test_valid_operation_correct():
    """ Megjelenik egy érvényes művelet:
        chr megző egy a fenti ABCs műveleti táblából származó karaktert tartalmaz
        op mező vagy + vagy - karaktert tartlamaz
        num mező egy egész számot tartalamaz """
    nums = driver.find_elements_by_id("num")
    assert chr_element.text in table_text
    assert op_element == "+" or "-"
    assert len(nums) == 1
    assert int(num_element.text)


def test_random_operation_correct():
    """ Gombnyomásra helyesen végződik el a random művelet a fenti ABCs tábla alapján:
        A megjelenő chr mezőben lévő karaktert kikeresve a táblában
        Ha a + művelet jelenik meg akkor balra lépve ha a - akkor jobbra lépve
        A num mezőben megjelenő mennyiségű karaktert
        az result mező helyes karaktert fog mutatni """
    submit_btn.click()
    time.sleep(1)
    current_res = return_result()
    assert current_res != ""

    driver.quit()
