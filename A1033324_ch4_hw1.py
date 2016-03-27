#!/usr/bin/env python
#coding=utf-8
girl={'Mary':'Honey','Lynn':'Baby','Jannie':'Little sweetie'}
str="Honey, you are always on my mind. Your love makes me blind .When I first met you I knew it was a sign."
name=input('which one:(1.Mary,2.Lynn,3.Jannie)')
if name==1:
	print str
if name==2:
	str=str.replace("Honey",girl['Lynn'])
	print str
if name==3:
	str=str.replace("Honey",girl['Jannie'])
	print str



