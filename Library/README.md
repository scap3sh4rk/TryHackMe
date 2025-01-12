![image](https://github.com/user-attachments/assets/f5c1cd5c-87bf-49ef-91d5-00098e113977)

# Report Library CTF
The machine can be found in TryHackme [Link](https://tryhackme.com/r/room/bsidesgtlibrary)
## Scan
I have used Nmap to find the open ports and found the port 22(SSH) and 80 (http) open.
Once i found the http open port i have visited the link the IP Address it refered to & found a username saying `meliodas`.
## Search 
I have used Dirsearch to find the hidden directories and found the name `rockyou` in the `robots.txt` file which seems to be a clue to Brute Force. 
maybe the wordlist to be used can be `rockyou.txt`.
```bash
dirsearch -u targetIPaddress
```
## Crack !
I just assumed the username for SSH to be meliodas and started hydra over it.
```bash
hydra -l meliodas -P /usr/share/wordlists/rockyou.txt ssh://ta.rg.et.Ip// | tee password.txt
```
The above command will bruteforce the username password and prints it to console and also the file.
## Into the SSH
I have logged into the ssh and i got access to the `meliodas` user and got the user flag.
### Inside the Meliodas
In the home directory i found 2 files `user.txt`-> user flag & `back.py` -> seems to be a backup code.
We need to have sudo privileges to directly execute the back.py.
`sudo -l` will return with the set of commands the user can execute using the sudo previlages.
Here in this case we have permission to execute `/usr/bin/python`,`/home/meliodas/back.py`
with sudo privileges this can be checked by,
```bash
sudo -l
```
The directories with `NOPASSWORD` mentioned can be accessible by meliodas hence running directly `bak.py` will not be accessed but can be executed using the following command
```bash
/usr/bin/python bak.py
```
will have result
now we can modify `bak.py` using echo to bringup the shell by,
```bash
echo 'import pty; pty.spawn("/bin/sh")' > bak.py
```
Now we can execute `bak.py` using the same command
```bash
sudo /usr/bin/python bak.py
```
And can get the root shell.

### Learning
Explore how to add the user to limit the user to execute the commands with sudo privileges.
#### Task
Add the `/usr/share/python` to your current user to execute python files with sudo privileges.
