import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k1.html"
driver.get(URL)
time.sleep(1)

# elemek kigyujtese
input_a = driver.find_element_by_id("a")
input_b = driver.find_element_by_id("b")
submit_btn = driver.find_element_by_id("submit")
result = driver.find_element_by_id("result")

# tesztadat listák
test_data_list = [["", ""], [2, 3], ["", ""]]
exp_results_list = ["10", "NaN"]


def clear_and_fill(element1, element2, t_data):
    element1.clear()
    element1.send_keys(t_data[0])
    element2.clear()
    element2.send_keys(t_data[1])
    submit_btn.click()
    time.sleep(2)


def return_result():
    return driver.find_element_by_id("result")


def test_initial_state_correct():
    """ TC1 - Helyesen jelenik meg az applikáció betöltéskor:
            a: <üres>
            b: <üres>
            c: <nem látszik> """
    assert input_a.text == test_data_list[0][0]
    assert input_b.text == test_data_list[0][1]
    assert not result.is_displayed()


def test_calculation_correct():
    """ TC2 - Számítás helyes, megfelelő bemenettel
            a: 2
            b: 3
            c: 10 """
    clear_and_fill(input_a, input_b, test_data_list[1])
    current_res = return_result()
    assert current_res.text == exp_results_list[0]


def test_empty_fill():
    """ TC3 - Üres kitöltés:
            a: <üres>
            b: <üres>
            c: NaN """
    clear_and_fill(input_a, input_b, test_data_list[2])
    current_res = return_result()
    assert current_res.text == exp_results_list[1]

    driver.quit()
