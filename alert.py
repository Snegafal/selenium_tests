'''from selenium import webdriver
import time, math

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/alert_accept.html')

    button = browser.find_element_by_css_selector('button')
    button.click()

    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()

    num_element = browser.find_element_by_id('input_value')
    num = num_element.text

    func_result = str(math.log(abs(12*math.sin(int(num)))))

    form_element = browser.find_element_by_id('answer')
    form_element.send_keys(func_result)

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

    alert2 = browser.switch_to.alert
    alert_text = alert2.text
    alert_num = alert_text.split(': ')
    print(alert_num[-1])


finally:
    time.sleep(2)
    browser.quit()

'''

from selenium import webdriver
import time, math

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/redirect_accept.html')

    main_window = browser.current_window_handle #имя текущего окна
    print(main_window)
    button = browser.find_element_by_css_selector('button')
    button.click()

    first_window = browser.window_handles[0]
    second_window = browser.window_handles[1]

    change_window = browser.switch_to.window(second_window)
    num_element = browser.find_element_by_id('input_value')
    num = num_element.text
    func_result = str(math.log(abs(12*math.sin(int(num)))))

    form_element = browser.find_element_by_id('answer')
    form_element.send_keys(func_result)

    submit = browser.find_element_by_css_selector('button')
    submit.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text.split(': ')[-1])
    alert.accept()

finally:
    time.sleep(2)
    browser.quit()
