import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
import sys


class MyInfo:
    def __init__(self, year):
        self.year = year
        self.scorelist = {}
        self.ranklsit = []

    def extract_name(self, yeardata):
        patt = re.compile(r"([A-Za-z]+ [A-Za-z]+) batted [0-9]+ times with")
        self.playerlist = patt.findall(yeardata)
        self.playerlist = list(set(self.playerlist))

    def getdata(self, yeardata):
        for name in self.playerlist:
            my_regex = r"\b{0} batted ([0-9]*) times with ([0-9]*) hits and ([0-9]*) runs\b".format(name)
            pat = re.compile(my_regex)
            match_text = pat.findall(yeardata)
            total_hits = 0
            total_bats = 0
            # print(name)
            for item in match_text:
                total_hits += int(item[1])
                total_bats += int(item[0])
            self.scorelist[name] = round(total_hits/total_bats, 3)
        self.ranklist = [
            (k, self.scorelist[k]) for k in 
            sorted(self.scorelist, key=self.scorelist.get, reverse=True)]


init_url = "https://classes.engineering.wustl.edu/cse330/content/cardinals/"
infolist = {}
html = urlopen(init_url)

bsobj = BeautifulSoup(html.read(), "lxml")
filelist = bsobj.body.table.find_all('a')[5:]
for item in filelist:
    link = item['href']
    pat = re.compile(r"([0-9]{4})")
    year = pat.findall(link)[0]
    new_url = init_url + link
    html = urlopen(new_url)
    bsobj_new = BeautifulSoup(html.read(), "lxml")
    baseball_data = bsobj_new.body.get_text()
    yearinfo = MyInfo(year)
    yearinfo.extract_name(baseball_data)
    yearinfo.getdata(baseball_data)
    infolist[year] = yearinfo

if len(sys.argv) < 2:
    sys.exit(
        "Usage: %s year (namely 1930, 1940, 1941, 1942, 1943, 1944)"
        % sys.argv[0])

filename = sys.argv[1]

try:
    info = infolist[filename]
except KeyError as e:
    print("Please input the proper year!")
else:
    for k, v in info.ranklist:
        line = "%s: %.3f" % (k, v)
        print(line)
