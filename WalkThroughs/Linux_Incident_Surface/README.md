# Linux Incident Surface report
[![](./assets/Header.png)](https://tryhackme.com/r/room/linuxincidentsurface)

## Processes 
`ps aux`
screenshot 1
Flags of `ps`
`lsof -p <processID>`
`lsof` stands for list of open files
This command will return with all the connections assoiciated with the process running with the processID
## Process with Network Connection
`ps aux`
`lsof -i -n -P`
screenshot 2
flags of `lsof`
## Osquery command: 
```bash
SELECT pid, fd, socket, local_address, remote_address FROM process_open_sockets WHERE pid = 267490;
```
Learn more on OsQuary 
[url](https://tryhackme.com/r/why-subscribe?roomCode=osqueryf8)
[url](https://tryhackme.com/r/why-subscribe?roomCode=linuxliveanalysis)
Note : Both the rooms above are premium

## Persistence 
Malware often tries to keep a footprint in the system such that it keeps running even after a system restart. This is called persistence. For example, If a malware adds itself to the startup registry keys, it will persist even after a system restart.
1. We go ahead and create a account. and examine the stuff.
```zsh
ubuntu@tryhackme:/home$ sudo useradd attacker -G sudo
ubuntu@tryhackme:/home$ sudo passwd attacker
New password: 
Retype new password: 
passwd: password updated successfully
ubuntu@tryhackme:/home$ echo "attacker ALL=(ALL:ALL) ALL" | sudo tee -a /etc/sudoers
attacker ALL=(ALL:ALL) ALL
```
### Logs Examining
```text
1. `System Logs`: System-related logs, such as kernel messages, boot logs, and general system activity logs, are stored directly in the /var/log directory.

2. `Application Logs`: Logs generated by specific applications, such as Apache web server logs (/var/log/apache2/), MySQL database server logs (/var/log/mysql/), and mail server logs (/var/log/mail/), are stored in separate subdirectories.

3. `Service Logs`: Logs generated by system services, daemons, and background processes are typically stored in subdirectories named after the corresponding services. For example, logs for the SSH service may be found in /var/log/sshd/.

4. `User Logs`: Logs related to user activities, such as login/logout records and command history, are stored in the /var/log/ directory or its subdirectories, such as /var/log/auth.log.
```
2. Another persistence method is cron jobs, which attackers can use to maintain persistent access to a compromised system. Cron is a time-based job scheduler in Unix-like systems that allows tasks (scripts, commands, or programs) to be executed automatically at specified intervals.

To create a malicious cron job, we can modify the crontab file or use the crontab command to edit scheduled jobs for the current user or system using the following command:
**I have used this in one of the rooms i have solved**

#### creating a cronjob
```bash
cronjob -e
```
Now add the following line at the end of the file 
```bash
@reboot sudo /path/to/script.sh 
```
This will execute the command for each minute.

#### Examining Malicious Cornjob
```bash
 /var/spool/cron/crontabs/[username]
```
Navigate to the above directory to find the leads of `cron` for that particular user.

### services
`sudo nano /etc/systemd/system/suspicious.service`
```bash
[Unit]
Description=Suspicious_Service
After=network.target

[Service]
ExecStart=/home/activities/processes/suspicious
Restart=on-failure
User=nobody
Group=nogroup

[Install]
WantedBy=multi-user.target
```
`ExecStart`: Specifies the command to run the collector program. Adjust the path as necessary.
`Restart=on-failure`: Ensures the service restarts if it fails.
Once its done we can start the service and check for the logs related to system to find any leads over a malicious service 

### Journalctl
This is a tool that is used to analyse the system services. the start time and the end time the service pid and many more 
`sudo journalctl -u <service name>`
Refer the help of the Journalctl
**Questions**
1. What is the default path that contains all the installed services in Linux?
A. /etc/systemd/system
2. Which suspicious service was found to be running on the host?
A. benign.service
3. What process does this service point to?
A. benign
4. Before getting this service stopped on 11th Sept, how many log entries were observed in the journalctl against this service?
A. 7

## Footprints on Disk
This mostly involves forensics
### Package Creation and Analysis
#### Creating a .deb Package
1. Create a folder with the name of the Package
```bash
mkdir <package name>
```
2. In tthe folder, create a folder named, `DEBIAN`
```bash
cd <package name> && mkdir DEBIAN`
```
3. Now create a `control` and a `postinst` files in which the control file will have the meta data of the deb file and then the `postinst` as the name suggests, it contains the script to be executed after the installations of the debian package.
the contents will be,

```control
Package: malicious-package
Version: 1.0
Section: base
Priority: optional
Architecture: all
Maintainer: attacker@test.com
Description: This is a malicious Package
```

```postins
#!/bin/bash
# Malicious post-installation script
# It will run this script after installation

# Print a suspicious message - for demonstration
echo "something suspicious"
```

Now make the postinst executable and type in thye following in the parent directory
```root
dpkg-deb --build <package name>
```
This returns the package `.deb`

This is a thing how an attacker can attack a machine and create a package. We now analyse the packages

#### Analysing the package
Here we consider the installed packages,
If we know the name of the installed package, you can joust grep it using the following command
```bash
dpkg -l | grep <package name>
```
This returns the installed package name and its details.
If you want to know the details, the dependencies it tried to install, you can just examine the logs of the file `/var/log/dpkg.logs` and grep over it.

### Questions 
1. Create a suspicious Debian package on the disk by following the steps mentioned in the task. How many log entries are observed in the dpkg.log file associated with this installation activity? 
A. **6**
2. What package was installed on the system on the 17th of September, 2024?
A. **c2comm**

