*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  kaali
    Set Password  hahaha12
    Set Password Confirmation  hahaha12
    Click  button >> text=Register
    Register Should Succeed

Register With Password Containing Numbers
    Set Username  numero
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click  button >> text=Register
    Register Should Succeed

Register With Password Containing Special Characters
    Set Username  erikois
    Set Password  kalle#abc
    Set Password Confirmation  kalle#abc
    Click  button >> text=Register
    Register Should Succeed

Register With Matching Password Confirmation
    Set Username  sama
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click  button >> text=Register
    Register Should Succeed

Register With Nonmatching Password Confirmation
    Set Username  eri
    Set Password  kalle123
    Set Password Confirmation  kalle321
    Click  button >> text=Register
    Register Should Fail With Message  message=Passwords do not match

Register With Password Containing Only Lowercase Letters
    Set Username  pelkkalower
    Set Password  kallekalle
    Set Password Confirmation  kallekalle
    Click  button >> text=Register
    Register Should Fail With Message  message=Invalid username or password

Register With Password Containing Only Uppercase And Lowercase Letters
    Set Username  upperlower
    Set Password  KalleKalle
    Set Password Confirmation  KalleKalle
    Click  button >> text=Register
    Register Should Fail With Message  message=Invalid username or password


Register With Too Short Username And Valid Password
    Set Username  ab
    Set Password  anatawa123
    Set Password Confirmation  anatawa123
    Click  button >> text=Register
    Register Should Fail With Message  message=Invalid username or password

Register With Valid Username And Too Short Password
    Set Username  kaali
    Set Password  ab
    Set Password Confirmation  ab
    Click  button >> text=Register
    Register Should Fail With Message  message=Invalid username or password

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  hahaha12
    Set Password Confirmation  hahaha12
    Click  button >> text=Register
    Register Should Fail With Message  message=Username in use

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Get Text  body  *=  ${message}

Set Username
    [Arguments]  ${username}
    Fill Text  id=username  ${username}

Set Password
    [Arguments]  ${password}
    Fill Secret  id=password  $password

Set Password Confirmation
    [Arguments]  ${password}
    Fill Secret  id=password_confirmation  $password

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page
