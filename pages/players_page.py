from pages.base_page import BasePage


class Players(BasePage):
    filter_button_xpath = "//button[@title = 'Filter Table']"
    name_filter_field_xpath = "//div[2]/div[1]/div/div/div/input"
    surname_filter_field_xpath = "//div[2]/div[1]/div/div/input"
    result_of_filtering_xpath = "//*[@data-testid='MUIDataTableBodyRow-0']"
    close_button_xpath = "//*[@aria-label = 'Close']"

    def click_on_the_filter_button(self):
        self.click_on_the_element(self.filter_button_xpath)

    def type_in_name(self, name):
        self.field_send_keys(self.name_filter_field_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_filter_field_xpath, surname)

    def click_on_the_result_of_filtering(self):
        self.click_on_the_element(self.result_of_filtering_xpath)

    def wait_for_button_will_be_clickable(self):
        self.wait_for_element_to_be_clickable(self.result_of_filtering_xpath)

    def click_on_the_close_filter_button(self):
        self.click_on_the_element(self.close_button_xpath)
