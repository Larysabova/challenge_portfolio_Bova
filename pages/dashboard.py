from pages.base_page import BasePage


class Dashboard(BasePage):
    menu_button_xpath = "//button[@aria-label="menu"]"
    main_page_button_xpath = "//*[text()="Main page"]"
    players_button_xpath = "//*[text()="Players"]"
    language_button_xpath = "//*[text()="English" or text()="Polski"]"
    sign_out_button_xpath = "//*[text()="Sign out"]"
    dev_team_contact_button_xpath = "//span[contains(text(),'Dev t')]"
    add_player_button_xpath = "//span[contains(text(),'Add pl')]"
    last_created_player_hyperlink_xpath = "//h6[text()="Last created player"]/following::span[1]"
    last_updated_player_hyperlink_xpath = "//h6[text()="Last updated player"]/following::span[1]"
    last_created_match_hyperlink_xpath = "//h6[text()="Last created match"]/following::span[1]"
    last_updated_match_hyperlink_xpath = "//h6[text()="Last updated match"]/following::span[1]"
    last_updated_report_hyperlink_xpath = "//h6[text()="Last updated report"]/following::span[1]"

