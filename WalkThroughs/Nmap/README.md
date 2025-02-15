# Nmap
Cheat sheet for nmap
----
## Scanning
Scanning the target to get information
### Pinging
```bash
nmap -sn <Target Ip address>
```
----
## Hide Identity

### Stealth
- `-sS` flag used for stealth scan
### Decoy 
Put up an decoy ip address which nmap uses to duplicate packets with source as the decoy IP and send it to server making the server learn that the ip addresses are coming >

```bash
sudo nmap -sS -D <Any decoy Ip address <Target ip address>>
