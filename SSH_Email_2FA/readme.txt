This is a two-factor authentication solution for adding security to an SSH server.

Setup:
You will need a gmail account, with third party access enabled.
- Note, this does not work for gmail accounts with 2FA enabled.

Make sure to fill in the <>'s in the email_2fa.py and bashrc.txt files with the correct details.
Append the contents of the bashrc.txt file to ~/.bashrc, like this: 'cat bashrc.txt >> ~/.bashrc'.

Troubleshooting:
You can debug by uncommenting the print statement found in the 'gen_and_send()' function.

> Tested on Ubuntu 18.04 LTS
