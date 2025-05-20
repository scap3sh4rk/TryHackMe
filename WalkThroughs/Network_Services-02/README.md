# NFS
- NFS stands for Network File System. Port is `2049`
- This is Used to share files accross devices in the network.
- Utility `nfs-common` is used.

## Identifying the shares:

```
# Command
# We can find the shares by 
showmount -e <Server IP address>

```

## Creating The mounting Directory

## Mounting the Share

![Reference_Image](./.asstes/MountingNFS.png)

Or 

We can also go with this,

```
sudo mount 10.10.107.216:/home MountPoint
### Where the IP address is the server IP address, The directory is mentioned after the ":" and the target Mount point is mentioned at the last 
```

--- 
# SMTP

The SMTP service has two internal commands that allow the enumeration of users: 
- VRFY (confirming the names of valid users) and 
- EXPN (which reveals the actual address of users aliases and lists of e-mail (mailing lists). 
Using these SMTP commands, we can reveal a list of valid users.

## Enumerating SMTP
- We can do this manually, over a telnet connection- however Metasploit comes to the rescue again, providing a handy module appropriately called "smtp_enum" that will do the legwork for us! Using the module is a simple matter of feeding it a host or range of hosts to scan and a wordlist containing usernames to enumerate.

---
# MySQL

- You will want to have MySQL installed on your system to connect to the remote MySQL server
- In MySQL, physically, a schema is synonymous with a database. You can substitute the keyword "SCHEMA" instead of DATABASE in MySQL SQL syntax, for example using CREATE SCHEMA instead of CREATE DATABASE. It's important to understand this relationship because some other database products draw a distinction. For example, in the Oracle Database product, a schema represents only a part of a database: the tables and other objects owned by a single user.

### Modules Used
- `mysql_sql`
- `auxiliary/scanner/mysql/mysql_schemadump` -> Dumps the whole databases in the target.
- `mysql_hashdump` -> Dumps the hashes of the target database
