import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k3.html"
driver.get(URL)

# elemek kigyujtese
input_field = driver.find_element_by_id("title")

test_data_list = ["abcd1234", "teszt233@", "abcd"]


def return_result():
    return driver.find_element_by_xpath('//span[@class="error active"]')


def input_fill(t_data):
    input_field.send_keys(t_data)
    input_field.send_keys("\t")
    time.sleep(1)


def test_correct_fill():
    """ TC1 - Helyes kitöltés esete:
        title: abcd1234
        Nincs validációs hibazüzenet """
    input_fill(test_data_list[0])
    err_msgs = driver.find_elements_by_xpath('//span[@class="error active"]')
    assert len(err_msgs) == 0


def test_incorrect_fill_char():
    """ TC2 - Illegális karakterek esete:
        title: teszt233@
        Only a-z and 0-9 characters allewed. """
    input_field.clear()
    input_fill(test_data_list[1])
    current_res = return_result()
    msg_text = "Only a-z and 0-9 characters allewed"
    assert current_res.text == msg_text


def test_incorrect_fill_length():
    """ TC3 - Túl rövid bemenet esete:
        title: abcd
        Title should be at least 8 characters; you entered 4. """
    input_field.clear()
    input_fill(test_data_list[2])
    current_res = return_result()
    msg_text = "Title should be at least 8 characters; you entered 4."
    assert current_res.text == msg_text

    driver.quit()
