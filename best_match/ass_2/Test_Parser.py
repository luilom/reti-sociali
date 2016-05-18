#!/usr/bin/python

from Impl_Parser import read_wibbi
from HTMLParser import HTMLParser
#from re import findall, sub
import re
import sys

reload(sys)

tag = True
parser = HTMLParser()
sys.setdefaultencoding('UTF8')
output = open("output.txt", "w")
topic = []
topic.append("sport")
topic.append("games")
index=0

toPrint = topic[index]+"\n"
#index+=1
#topic = "test"
topic_graph,topic_db = read_wibbi()
#graph,db = read_wibbi("./"+filename)
for topic in topic_graph.keys():
    toPrint = topic+"{"
    for i in topic_graph[topic].keys():
        toPrint += i+ "["
        for val in topic_db[topic][i]:
            if '<' in val:
                tag = False
            elif '/>' in val:
                tag = True
            elif re.match("^[A-Za-z0-9]*$", val):
                html_decoded_string = parser.unescape(val)
                toPrint += html_decoded_string + ","
        toPrint += "]"
    toPrint +="}"
print >> output,  toPrint
output.close()
