#/usr/bin/python
#_*_ coding:utf-8

import re

obj = re.match('\d+', '111ddd')

if obj:
    print obj.group()