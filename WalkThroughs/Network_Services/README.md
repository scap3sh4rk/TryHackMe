# Network Services

![[Network Services](https://tryhackme.com/room/networkservices)](https://github.com/user-attachments/assets/0217ac4b-9f9d-4e73-8b3a-7565d13793c9)

##
SMB : stands for server message block which is used to access the files and file syustems remotly over the internet
widely used in windows

### Task 3: Enumirating SMB
1. 3
2. 139/445
3. WORKGROUP
4. polosmb
5. 6.1
6. profiles

### Task 4: 
1. smbclient //10.10.10.2/secret -U suit -p 445
2. Y
3. John Cactus
4. SSH
5. .ssh
6. id_rsa
7. THM{smb_is_fun_eh?}

## Tenlet
Tenlet is
### Task 5: Understanding Tenlet

1. application protocol
2. ssh
3. telnet 10.10.10.3 23
4. encryption

### Task 6: Enumerating Telnet
1. 1
2. 8012
3. tcp
4. 0
5. -
6. A Backdoor
7. skidy
8. -

### Task 7: Exploiting Telnet
1. -
2. SKIDY'S BACKDOOR.
3. N
4. -
#### Tcp Dump
```
sudo tcpdump ip proto \\icmp -i tun0
```
This command dumps all the traffic to the terminal and that is specific to icmp protocol on the interface tun0
5. -
6. N
7. -
8.  
#### msfvenom 
9. mkfifo
10. nc -lnvp 4444
11. -
12. THM{y0u_g0t_th3_t3ln3t_fl4g}
