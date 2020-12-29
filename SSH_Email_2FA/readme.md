# SSH_Email_2FA

*Two-factor authentication solution for adding security to an SSH server using email*

## Setup:

1. You will need a gmail account with third party access enabled for the mechanism to send emails with.
* Note, the script cannot authenticate to gmail accounts with 2FA (ironic, I realise :wink:)

2. Fill in the <>'s in the email_2fa.py and bashrc.txt files with the correct details.

3. Append the contents of the bashrc.txt file to ~/.bashrc, like this:

> 'cat bashrc.txt >> ~/.bashrc'.

## Troubleshooting:

1. You can debug by uncommenting the print statement found in the 'gen_and_send()' function.

## Tested on Ubuntu 18.04 LTS

## Developed by Jack
![Alt Text](https://raw.githubusercontent.com/jacksec/jacksec.github.io/master/assets/img/logo.png)

https://jacksec.uk
