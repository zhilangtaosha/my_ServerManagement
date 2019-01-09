# -*- coding: utf-8 -*-
# @Time    : 2019/1/9 13:30
# @Author  : dodo8619
# @Email   : lj16888619@gmail.com
# @File    : test.py

import json

# import sys
# reload(sys)
# sys.setdefaultencoding("gbk")
# s="快捷操作".encode("utf-8").decode("utf-8")
url = []
url.append( {
        "title": "",
        "children": [
            {"title": "快捷按钮","href": "/linkButton"},
            {"title": "快捷文件","href": "/linkFile"},
        ]
    } )

# s="快捷操作".encode("utf-8").decode("utf-8")
print (json.dumps(url, encoding="UTF-8", ensure_ascii=False))
print(url)