import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k2.html"
driver.get(URL)

# elemek kigyujtese
random_color_name = driver.find_element_by_id("randomColorName")
test_color_name = driver.find_element_by_id("testColorName")
start_btn = driver.find_element_by_id("start")
stop_btn = driver.find_element_by_id("stop")
result = driver.find_element_by_id("result")

msgs_text_list = ["Correct!", "Incorrect!"]


def return_result():
    return driver.find_element_by_id("result")


def start_and_stop():
    start_btn.click()
    stop_btn.click()
    time.sleep(1)


def test_initial_state_correct():
    """ TC1 - Helyesen jelenik meg az applikáció betöltéskor:
        Alapból egy random kiválasztott szín jelenik meg az == bal oldalanán.
        A jobb oldalon csak a [ ] szimbólum látszik. <szín neve> [ ] == [ ] """
    assert random_color_name.text != ""
    assert test_color_name.text == ""


def test_start_and_stop_correct():
    """ TC2 - El lehet indítani a játékot a start gommbal.
        Ha elindult a játék akkor a stop gombbal le lehet állítani. """
    start_and_stop()
    current_test_color_name = driver.find_element_by_id("testColorName")
    assert current_test_color_name.text != ""


def test_play_works_correctly():
    """ TC3 - Eltaláltam, vagy nem találtam el.
        Ha leállítom a játékot két helyes működés van, ha akkor állítom épp le amikor a bal és a jobb oldal
        ugyanazt a színt tartalmazza akkor a Correct! felirat jelenik meg.
        Ha akkor amikor eltérő szín van a jobb és bal oldalon akkor az Incorrect! felirat kell megjelenjen. """
    # nem találtam el:
    start_and_stop()
    current_res = return_result()
    assert current_res.text == msgs_text_list[1]

    # eltaláltam:
    start_btn.click()
    current_rdm_clr = driver.find_element_by_id("randomColorName")
    test_clrs = driver.find_elements_by_id("testColorName")
    for color in test_clrs:
        if color.text == current_rdm_clr.text:
            stop_btn.click()
    time.sleep(1)
    current_res = return_result()
    assert current_res.text == msgs_text_list[0]

    driver.quit()
