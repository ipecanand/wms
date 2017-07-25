*** Settings ***
Documentation  Keywords are defined here
Library  Selenium2Library


*** Keywords ***
WS Login
    [Arguments]  ${Username}  ${Password}
    wait until page contains  Username
    input text  Xpath = //input[@id='LoginBox1_user_tb']  ${Username}
    input text  CSS = input[id='LoginBox1_pass_tb']  ${Password}
    click image  Xpath = //input[@id='LoginBox1_LoginImageButton']
    wait until page contains  Warehouse
    click image  Xpath = //input[@id='btnGo']
    wait until page contains  Setup
    set browser implicit wait  5 seconds
    execute javascript  javascript:__doPostBack('_ctl6','')
    sleep  10s

RDT Login
    [Arguments]  ${Username}  ${Password}
    sleep  10s
    input text  Xpath = //input[@id='UserName']  ${Username}
    input text  Xpath = //input[@id='Password']  ${Password}
    click button  Xpath = //input[@id='Submit']
    sleep  10s
    click link  Xpath = //a[@class='logout']
    sleep  10s




