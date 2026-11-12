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
    Main Page Should Be Open

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
