# _*_ coding: utf-8 _*_
__author__ = 'chandler'

import re

#line = "xxx出生于2001年6月1日"
#line = "xxx出生于2001/6/1"
#line = "xxx出生于2001-6-1"
#line = "xxx出生于2001-06-01"
line = "xxx出生于2001-06月-01日"
regex_str = ".*出生于(\d{4}[年/-]\d{1,2}(([月/-]|[月/-][月/-])\d{1,2}[日/-]|[月/-]\d{1,2}|[月/-]$|$))"
match_obj = re.match(regex_str, line)
if match_obj:
    print(match_obj.group(1))
