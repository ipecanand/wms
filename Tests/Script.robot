*** Settings ***
Documentation  This is main Script file where our Workstation and RDT will open
Resource  ../Resources/WSkeyword.robot
Resource  ../Resources/Common.robot



*** Variables ***
# pybot -d results Tests/Script.robot
&{WS_ADMIN_USER}  Username=admin  Password=made4net
&{WS_BROWSER}  Browser=ie  Url=http://dal-v-de-wms15.ncr.com/WS_LBBASE
&{RDT_ADMIN_USER}  Username=anand  Password=made4net
&{RDT_BROWSER}  Browser=internetexplorer  Url=http://dal-v-de-wms15.ncr.com/RDT_LBBASE


*** Test Cases ***
Workstation Login
    [Documentation]  We have to login workstation
    [Tags]  Smoke Workstation
    Launch Browser  &{WS_BROWSER}
    WS Login  &{WS_ADMIN_USER}
    Quit Browser

Device Login
    [Documentation]  We have to login RDT
    [Tags]  Smoke RDT
    Launch Browser  &{RDT_BROWSER}
    RDT Login  &{RDT_ADMIN_USER}
    Quit Browser
