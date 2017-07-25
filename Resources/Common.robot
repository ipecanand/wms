*** Settings ***
Documentation  Common Keywords defined here
Library  Selenium2Library



*** Variables ***
#${Browser} =  ie
#${WS_Url} =  http://dal-v-de-wms15.ncr.com/WS_LBBASE

*** Keywords ***
Launch Browser
    [Arguments]  ${Browser}  ${Url}
    open browser  ${Url}  ${Browser}

Quit Browser
    close browser