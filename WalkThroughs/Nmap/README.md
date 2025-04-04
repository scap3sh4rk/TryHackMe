# Nmap
![[nmap](https://tryhackme.com/room/furthernmap)](https://github.com/user-attachments/assets/a3e64bf7-0600-484c-a780-aec808d1c63c)

Cheat sheet for nmap

## Scanning
Scanning the target to get information
### Pinging
```bash
nmap -sn <Target Ip address>
```

## Hide Identity

### Stealth
- `-sS` flag used for stealth scan
### Decoy 
Put up an decoy ip address which nmap uses to duplicate packets with source as the decoy IP and send it to server making the server learn that the ip addresses are coming >

```bash
sudo nmap -sS -D <Any decoy Ip address <Target ip address>
nmap -sS -D RND:10 <Target>
```


### spoofing
Can be used to spoof the ip address of our machine

---
# Nmap [THM]
[Link](https://tryhackme.com/room/furthernmap)

## some important flags 
- `oA` <basename>: Output in the three major formats at once
- `oG` : Greppable format output
- `script=vuln` : executes all the vulnerable scripts

## Scan types

### Most common
1. TCP Connect Scans `(-sT)`
2. SYN "Half-open" Scans `(-sS)`
3. UDP Scans `(-sU)`

### Less Common
1. TCP Null Scans `(-sN)`
2. TCP FIN Scans `(-sF)`
3. TCP Xmas Scans `(-sX)`

## Scan Types in Detail

### Full scan
1. TCP scan (-sT)
- SYN, SYN/ACK, ACK handhake happens and called complete handshake 
2. SYN scan (-sS)
- All scan only syn happens and [RST]. flag is sent
3. NULL scan (-sN)
- Null scan, no flag is set . once the detection happens, [RST, ACK] is sent.
- Not accurate enough
4. FIN scan (-sF)
- FIN scans (-sF) work in an almost identical fashion; however, instead of sending a completely empty packet, a request is sent with the FIN flag (usually used to gracefully close an active connection). Once again, Nmap expects a RST if the port is closed.
5. Xmas (-sX)
- As with the other two scans in this class, Xmas scans (-sX) send a malformed TCP packet and expects a RST response for closed ports. It's referred to as an xmas scan as the flags that it sets (PSH, URG and FIN) give it the appearance of a blinking christmas tree when viewed as a packet capture in Wireshark.














---
### Task 2 Introduction
1. What networking constructs are used to direct traffic to the right application on a server?
Ports
2. How many of these are available on any network-enabled computer?
65535
3. [Research] How many of these are considered "well-known"? (These are the "standard" numbers mentioned in the task)
1024
### Task 3 Nmap Switches
1. What is the first switch listed in the help menu for a 'Syn Scan' (more on this later!)?
-sS
2. Which switch would you use for a "UDP scan"?
-sU
3. If you wanted to detect which operating system the target is running on, which switch would you use?
-O
4. -sV
5. -v
6. -vv
7. -oA
8. -oN
9. -oG
10. -A
11. -T5
12. -p 80
13. -p 1000-1500
14. -p-
15. --script
16. --script=vuln
### Task 5
1. RFC 9293
2. RST

### Task 8 NULL, FIN and Xmas

1. Xmas
2. firewall evasion
3. Microsoft Windows

### Task 9 ICMP Network Scanning

Nmap sending ICMP packets to the possible hosts and detecting whether the host is up with that ip or not is called *ping sweep*
(-sn)
```bash
nmap -sn 192.168.0.0/24
```
1. ping -sn 192.16.0.0/16


### Task 10 Nmap scripts
To show the help menu of the script, use the following
```bash
nmap --script-help ftp-anon.nse
```
Nmap script engine has some catagories in which the scripts are devided and each catagories has a meaning.
Some of the catogories are here.
	safe:- Won't affect the target
	intrusive:- Not safe: likely to affect the target
	vuln:- Scan for vulnerabilities
	exploit:- Attempt to exploit a vulnerability
	auth:- Attempt to bypass authentication for running services (e.g. Log into an FTP server anonymously)
	brute:- Attempt to bruteforce credentials for running services
	discovery:- Attempt to query running services for further information about the network (e.g. query an SNMP server).
1. If we Execute the following command, using nmap script flag,
```bash
nmap --script=vuln <target>
```
Now the `NSE` Executes all the scripts that are unuder a specific catagory that is, `vuln` over the target.

2. We can run a specific script specifying the script name.
```bash
--script=<script-name> 
```
3. we can also execute multple number of scripts using the comma seperated naming.
```bash
--script=<script 1>,<script 2>
```
4. Script arguements.
Some scripts require arguments (for example, credentials, if they're exploiting an authenticated vulnerability). These can be given with the --script-args Nmap switch. An example of this would be with the http-put script (used to upload files using the PUT method). This takes two arguments: the URL to upload the file to, and the file's location on disk
Example:
```bash
nmap -p 80 --script http-put --script-args http-put.url='/dav/shell.php',http-put.file='./shell.php'
```
Note that the arguments are separated by commas, and connected to the corresponding script with periods (i.e.  `<script-name>.<argument>`).


#### Answers
1. maxlist


### Task 12. Finding for scripts
We have a database list of scripts where the script name with its catogories are stored.
```bash
cat /usr/share/nmap/scripts/script.db | grep safe
```
`script.db` has is the name of that nmap script database.

#### Answers
1. smb-os-discovery.nse
2. smb-brute

### Task 13. Firewall Evasion
1. ICMP
2. --data-length

### Task 14. Practical
1. N
2. 999
3. no -respons
4. 5
5. y

