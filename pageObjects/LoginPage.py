class LoginPage:
    textbox_username_id = "txtUsername"
    textbox_password_id = "txtPassword"
    btn_login_id = "btnLogin"
    btn_welcome_id = "welcome"
    btn_logout_xpath = "//a[text()='Logout']"
    #btn_dashboard_id = "menu_dashboard_index"
    lable_dashboard_xpath = "//h1[text()='Dashboard']"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_id(self.btn_login_id).click()

    # def clickDashboard(self):
    #     self.driver.find_element_by_id(self.btn_dashboard_id).click()

    def visibleText(self):
        text = self.driver.find_element_by_xpath(self.lable_dashboard_xpath).text
        return text

    def clickLogout(self):
        self.driver.find_element_by_id(self.btn_welcome_id).click()

    def clickLogoutLink(self):
        self.driver.find_element_by_xpath(self.btn_logout_xpath).click()


