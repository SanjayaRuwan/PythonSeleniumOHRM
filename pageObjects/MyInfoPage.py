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
    select_natinality_id= "personal_cmbNation"
    select_blood_name ="//select[@name='custom1']"
    btn_editBlood_id="btnEditCustom"

    #Contact Details objects
    link_contact_linktext="Contact Details"
    text_address1_id="contact_street1"
    text_address2_id="contact_street2"
    text_city_id="contact_city"
    text_zip_id="contact_emp_zipcode"
    text_mobile_id="contact_emp_mobile"
    text_workemail_id="contact_emp_work_email"

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

    def selectNatinality(self,national):
        self.driver.find_element_by_id(self.select_natinality_id).click
        self.driver.find_element_by_id(self.select_natinality_id).send_keys(national)

    def clickSave(self):
        self.driver.find_element_by_id(self.btn_edit_id).click()

    def selectblood(self,blood):
        self.driver.find_element_by_xpath(self.select_blood_name).click
        self.driver.find_element_by_xpath(self.select_blood_name).send_keys(blood)

    def clickBloodSave(self):
        self.driver.find_element_by_id(self.btn_editBlood_id).click()

    #Contact Details methods
    def clickContact(self):
        self.driver.find_element_by_link_text(self.link_contact_linktext).click()

    def setAddress1(self,address1):
        self.driver.find_element_by_id(self.text_address1_id).clear()
        self.driver.find_element_by_id(self.text_address1_id).send_keys(address1)

    def setAddress2(self,address2):
        self.driver.find_element_by_id(self.text_address2_id).clear()
        self.driver.find_element_by_id(self.text_address2_id).send_keys(address2)

    def setCity(self,city):
        self.driver.find_element_by_id(self.text_city_id).clear()
        self.driver.find_element_by_id(self.text_city_id).send_keys(city)

    def setZip(self,zip):
        self.driver.find_element_by_id(self.text_zip_id).clear()
        self.driver.find_element_by_id(self.text_zip_id).send_keys(zip)

    def setMobile(self,mobile):
        self.driver.find_element_by_id(self.text_mobile_id).clear()
        self.driver.find_element_by_id(self.text_mobile_id).send_keys(mobile)

    def setEmail(self, email):
        self.driver.find_element_by_id(self.text_workemail_id).clear()
        self.driver.find_element_by_id(self.text_workemail_id).send_keys(email)