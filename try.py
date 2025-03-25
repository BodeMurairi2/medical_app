#!/usr/bin/env python3
import datetime

year = datetime.datetime.strptime('1960', '%Y').year
this_year = datetime.datetime.now().year
age = this_year - year
print(type(age))