import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k5.html"
driver.get(URL)
time.sleep(1)

# elemek kigyujtese
cells = driver.find_elements_by_xpath('//input[@name="number"]')
nums = driver.find_elements_by_xpath('//ol[@id="numbers-list"]/li')
play_btn = driver.find_element_by_id("spin")
init_btn = driver.find_element_by_id("init")
msg = driver.find_element_by_id("messages")


def test_initial_state_correct():
    """ Az applikáció helyesen megjelenik:
        A bingo tábla 25 darab cellát tartalmaz
        A számlista 75 számot tartalmaz """
    assert len(cells) == 25
    assert len(nums) == 75


def test_correct_operation():
    """ Bingo számok ellenőzrzése:
        Addig nyomjuk a play gobot amíg az első bingo felirat meg nem jelenik
        Ellenőrizzük, hogy a bingo sorában vagy oszlopában lévő számok a szelvényről tényleg
        a már kihúzott számok közül kerültek-e ki """
    for _ in range(25):
        play_btn.click()
        if msg.is_displayed():
            break


def test_start_new_game():
    """ Új játékot tudunk indítani
        az init gomb megnyomásával a felület visszatér a kiindulási értékekhez
        új bingo szelvényt kapunk más számokkal. """

    driver.quit()
