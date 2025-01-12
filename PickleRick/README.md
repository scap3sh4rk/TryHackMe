# Report for PickelRick
[![](./assets/header)](https://tryhackme.com/r/room/picklerick)
While inspecting the web page, I got this in the home page 
`R1ckRul3s`.
## Tool
`Nikto` -> A free opensource command line tool that scans the webserver for vulnerabilities.

## Directory Enumiration
Used dirsearch to enumirate the directories and found a /robots.txt which has a weard thing.
I used the thing i got in the homepage as username and the weard thing as password and yes LoggedIn!!.

## Into the page
I got a command pannel and triggered a reverse shell using php and got the root shell.
also `sudo -l` and found that the current user has the full system access.
Hence i could able to trigger a reverse shell
## Sup3rS3cretPickl3Ingred.txt
mr. meeseek hair

## 2nd 
/home/rick
1 jerry tear

## 3rd
pwd && cat 3rd.txt
/root
3rd ingredients: fleeb juice

