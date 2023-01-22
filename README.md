### TASK 1: Software configuration

#### Subtask 1: Why did I choose to participate in the Dare IT Challenge?

Because I want to work in IT, I chose to participate. I applied because I might get the chance to work in Poland for an IT company. I think that working on this project will help me get closer to my goal and will give me the basic knowledge in QA that will  guide me in the proper direction.

### TASK 2: Selectors

#### Subtask 1: Searching for selectors on the login pageList all the elements that are on the login page.

    scouts_panel_heading_xpath
    //*[@id="__next"]/form/div/div[1]/h5
    //*[text()="Scouts Panel"]
    //child::div/h5

    login_field_xpath
    //*[@id="login"]
    //*[@name='login']
    //*[contains(@name, "login")]

    password_field_xpath
    //*[@id="password"]
    //*[@name='password']
    //*[contains(@name, "passw")]

    remind_password_hyperlink_xpath
    //*[@id="__next"]/form/div/div[1]/a
    //*[text()="Remind password"]
    //child::div/a
    
    language_button_xpath
    //*[@id="menu-"]/div[3]/ul/li[1]
    //*[@role="button"]
    //*[text()="English" or text()="Polski"]
    
    sign_in_button_xpath
    //*[@id="__next"]/form/div/div[2]/button/span[1]
    //*[text()="Sign in"]
    //child::button/span[2]

