import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    # if browser == 'chrome':
    driver = webdriver.Chrome('Drivers/chromedriver.exe')
    print("Launching chrome browser")
    # else:
    #     driver = webdriver.Firefox('D:\OrangeHRM\Drivers\geckodriver.exe')
    #     print("Launching firefox browser")


    driver.maximize_window()
    return driver


# This will get the values from CLI/hooks
def pytest_addoption(parser):
    parser.addoption("--browser")


# This will return the browser value to setup method
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


###### Pytest HTML Reports ############

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Orange HRM'
    config._metadata['Module Name'] = 'Employees'
    config._metadata['Tester'] = 'Sanjaya Ruwan'


# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
