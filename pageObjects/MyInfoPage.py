class MyInfo:
    link_menu_myInfo_id = "menu_pim_viewMyDetails"
    btn_edit_id = "btnSave"
    text_fname_id = "personal_txtEmpFirstName"
    text_mname_id = "personal_txtEmpMiddleName"
    text_lname_id = "personal_txtEmpLastName"
    text_licenseNo_id = "personal_txtLicenNo"
    date_licenseExp_id = "personal_txtLicExpDate"
    radio_male_id = "personal_optGender_1"
    radio_female_id = "personal_optGender_2"
    select_marital_id = "personal_cmbMarital"

    def __init__(self, driver):
        self.driver = driver

    def clickMyInfo(self):
        self.driver.find_element_by_id(self.link_menu_myInfo_id).click()

    def clickEdit(self):
        self.driver.find_element_by_id(self.btn_edit_id).click()

    def setFName(self,fname):
        self.driver.find_element_by_id(self.text_fname_id).clear()
        self.driver.find_element_by_id(self.text_fname_id).send_keys(fname)

    def setMName(self,mname):
        self.driver.find_element_by_id(self.text_mname_id).clear()
        self.driver.find_element_by_id(self.text_mname_id).send_keys(mname)

    def setLName(self,lname):
        self.driver.find_element_by_id(self.text_lname_id).clear()
        self.driver.find_element_by_id(self.text_lname_id).send_keys(lname)

    def setLicenseNo(self,licNo):
        self.driver.find_element_by_id(self.text_licenseNo_id).clear()
        self.driver.find_element_by_id(self.text_licenseNo_id).send_keys(licNo)

    def setLicenseExpDate(self,expDate):
        self.driver.find_element_by_id(self.date_licenseExp_id).clear()
        self.driver.find_element_by_id(self.date_licenseExp_id).send_keys(expDate)

    def selectGender(self):
        self.driver.find_element_by_id(self.radio_female_id).click()

    def selectMarital(self,marital):
        self.driver.find_element_by_id(self.select_marital_id).click
        self.driver.find_element_by_id(self.select_marital_id).send_keys(marital)


    def clickSave(self):
        self.driver.find_element_by_id(self.btn_edit_id).click()
