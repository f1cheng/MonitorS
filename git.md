
## git basic
```

[root@cfBareos pyy]# ls
mysql_query.py
[root@cfBareos pyy]# git config --global user.email "184918308@qq.com"
[root@cfBareos pyy]# git config --global user.name "f1cheng"
[root@cfBareos pyy]# git commit -m -$'mysql first commit'
[master 8d6e631] -mysql first commit
 1 file changed, 44 insertions(+)
 create mode 100755 pyy/mysql_query.py
[root@cfBareos pyy]# git push origin HEAD:master
Username for 'https://github.com': f1cheng
Password for 'https://f1cheng@github.com': 
Counting objects: 5, done.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (4/4), 785 bytes | 0 bytes/s, done.
Total 4 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/f1cheng/MonitorS.git
   e0aeb7b..8d6e631  HEAD -> master

```

