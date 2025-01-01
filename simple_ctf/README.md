# Report for simple CTF
![Head](/simple_ctf/assets/Head.png)
Link : [simpleCtf](https://tryhackme.com/r/room/easyctf)
### 1. Services running under port 1000
This means not on port 1000; It means the services that are running with port number less than 1000;
Its obvyously 2 
### 2. What is runnnig on Higher port 
Normal scan of the nmap doesnt give the excat service runnning on the port and defaults with default port number service binding,
there the normal doesnt give correct answer.
```bash
nmap -sV -p 2222 10.10.114.190 | file.txt
```
The flag `-sV` is to determine service version. This looks deep into the service running on the port.

### 3. Enumiration 
Enumirate the port http and we get the location of server `cmsms` [CMSMS cms made simple].
the version can be seen beneeth the logo `v2.2.8` 
Go ahed and search for the explots this version is vulnerable to.
```web
exploit db
```
__make a note of the name `mitch` posted some news may be mitch is a username for the ssh port if thats true, lets try some hydra here__

### 4. Hydra
```bash
hydra -l mitch -P /usr/share/wordlists/rockyou.txt ssh://10.10.114.190:2222
```
Yup! we got i the password is `secret`
But still we got to know that this is vulnerable to some attack lets check what that vulnerability is about.
### What's the CVE you're using against the application?
Clearly shown in the search. 

### 5. To what kind of vulnerability is the application vulnerable?
Read the vulnerability report 
examining the payload from `exploit-db` we observe some sort of bruteforce can happen using `sqli`
### 6. Exploiting the webpage
We can download the exploit from the link [url](https://www.exploit-db.com/exploits/46635) and execute it
The help menu speaks somethig about `TIME` meaning the `nth` time the exploit is being executed on the server.
- If you fail to get the credentilas first time and plan to execute for the second time, make sure you change the `TIME` variable to 2. and so on.

Once i got the username and password. `The same as the once we got with hydra`
This is what the text file in the ftp server corresponds to maybe.
That says,
```text
Dammit man... you'te the worst dev i've seen. You set the same pass for the system user, and the password is so weak... i cracked it in seconds. Gosh... what a mess!
```
if we closely observe the username is here itself `ForMitch.txt`.

### 7. What's the password?
We Got it Already.

### 8. Where can you login with the details obtained?
Its obvyous `SSH`

### 9. What's the user flag?
G00d j0b, keep up!

### 10. Is there any other user in the home directory? What's its name?
sunbath

### 11. Just like that
```bash
sudo -l 
```
use the above command to search what all stuff can a user can execute with sudo previlages and..
found `vim` can do that and thats it i have tried the following command.
```bash
sudo /usr/bin/vim root/root.txt
```
### 12. What can you leverage to spawn a privileged shell?
vim

### 13. What's the root flag?
W3ll d0n3. You made it!


Thankyou
scap3sh4rk
