from selenium import webdriver
from time import sleep


def get_qrator_jsid(repeat_num: int) -> str:
    """
    Получаем qrator_jsid через selenium для обхода защиты

    :param repeat_num: количество попыток соединения
    :return: Код qrator_jsid
    """
    url = 'https://www.dns-shop.ru/'

    options = webdriver.ChromeOptions()
    options.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.2271 YaBrowser/23.9.0.2271 Yowser/2.5 Safari/537.36')
    options.add_argument("--disable-blink-features=AutomationControlled") # маскируемся, что бы сайт не видел нас как бота
    options.add_argument("--headless") # Запуск в фоновом режиме
    driver = webdriver.Chrome(options=options)
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        'source': '''
    delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
    delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
    delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
    '''
    })

    try:
        for i in range(repeat_num):
            driver.get(url=url)
            sleep(2)
            qrator_jsid = driver.get_cookie('qrator_jsid')['value']
            print(qrator_jsid)
            return qrator_jsid
    except Exception as ex:
        print('Не смог получить qrator_jsid')
        raise ex
    finally:
        driver.close()
        driver.quit()
