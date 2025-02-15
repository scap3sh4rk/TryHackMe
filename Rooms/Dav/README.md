![image](https://github.com/user-attachments/assets/79c68b65-b994-4e8d-bfb5-1d51c9390bcb)

# webDEV Writeup
Here is the web dev challange from TryHackMe [link](https://tryhackme.com/r/room/bsidesgtdav)
## Enumiration
Used nmap to find the open ports in the server.
```bash
nmap -sV -sC 10.10.209.142 | tee nmap.scan 
```
```nmap.scan
PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
```
## Enumirate the hidden directories
Enumirating for the hidden directories using dirsearch 
```bash
dirsearch -u http://10.10.209.142
```
I found that there is a webserver with the name `WebDAV`.
## Thats a webDev server 
__New Learning__ 
WebDAV is a webserver that can be used to host websites using apache.
Remember to check whether the server hosted is a standard server. Because if its a standard server we may have chance to check the vulnerabilities.
## Into the webserver
- I have checked for the address `http://10.10.209.142/webdav/`. There is a prompt for authentication.
- I have used burpsuite to bruterforce the login.
- Since we dont know the username i tried it with `admin` and passwords for `rockyou.txt`. But whatif the user called admin doesnt exsist?
- Hence aborted the bruteforce and checked the writeups
- Found that the `WebDAV` server is a standard server and googled up for the default crediantials for the webserver.
- Their defaults are username `wampp` password `xampp`.
WebDAV server -> default crediantiasls -> logged in
## Found a hash in there of type apache 
__New Learning__
```bash
cadaver http://10.10.209.142/webdav/ 
put /revrseshell.php/
```
Used cadaver to upload the revershell script into a directory.``
listen to the ip address and then we can access the shell
## sudo -l
I saw that the /bin/cat command can be accessed by the `www-data` used with sudo previlags and thats it we can cat the crediantials in root.
## Here are the flags
user.txt -> 449b40fe93f78a938523b7e4dcd66d2a

root.txt -> 101101ddc16b0cdf65ba0b8a7af7afa5
