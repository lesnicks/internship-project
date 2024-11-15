from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions


def browser_init(context):
    """
    :param context: Behave context
    """

    # ##Chrome##
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

    ##Firefox##
   # driver_path = GeckoDriverManager().install()
   # service = Service(driver_path)
   # context.driver = webdriver.Firefox(service=service)

    ##Headless##
    # options = webdriver.ChromeOptions()
    # service = Service(ChromeDriverManager().install())
    # options.add_argument('headless')
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service )

    ##BrowserStack##
    bs_user = 'nickolasles_cCUb9E'
    bs_key = '3pedC1xAgjLP1XDz9aKz'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    options = ChromeOptions()
    bstack_options = {
        "os" : "Windows",
        "osVersion" : "11",
        'browserName': 'Chrome',
        'browserVersion': '129.0'
    }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)


    context.driver.maximize_window()
    context.driver.implicitly_wait(5)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()




# options = webdriver.ChromeOptions()
# options.add_argument('--headless')

# driver = webdriver.Chrome(options=options)

#     options= options
#     service= service
#
# options = Options()
# options = webdriver.ChromeOptions()
# options.add_argument('headless')
# service = Service(GeckoDriverManager().install())
# service = Service(GeckoDriverManager().install())
# driver_path = webdriver.Chrome(
