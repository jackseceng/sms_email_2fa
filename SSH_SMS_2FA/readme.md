# SSH_SMS_2FA

*Two-factor authentication solution for adding security to an SSH server using text messages*

## Setup:

1. You will need a textlocal account, with an API key for the SMS service;
* Details about textlocal can be found here: https://www.textlocal.com.

2. Fill in the *<>*'s in *email_2fa.py* and *bashrc.txt* with the correct details.

3. Append the contents of the bashrc.txt file to ~/.bashrc, like this:

* > 'cat bashrc.txt >> ~/.bashrc'.

## Troubleshooting:

1. You can debug by uncommenting the print statement found in the 'gen_and_send()' function.

## Tested on Ubuntu 18.04 LTS

## Developed by Jack
![Alt Text](https://raw.githubusercontent.com/jacksec/jacksec.github.io/master/assets/img/logo.png)

https://jacksec.uk
