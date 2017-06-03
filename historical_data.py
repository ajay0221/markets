import urllib2, cookielib

url = "https://www.nseindia.com/products/dynaContent/common/productsSymbolMapping.jsp?symbol=SBIN&segmentLink=3&symbolCount=1&series=EQ&dateRange=+&fromDate=01-01-2017&toDate=28-05-2017&dataType=PRICEVOLUMEDELIVERABLE"
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive',
       'Referer':'https://www.nseindia.com/products/content/equities/equities/eq_security.htm'}

req = urllib2.Request(url, headers=hdr)
page = urllib2.urlopen(req)

from bs4 import BeautifulSoup
soup = BeautifulSoup(page, "lxml")

content = soup.find("div", {"id": "csvContentDiv"}).string
headers = content[:content.index(':')]
print headers

data = content[content.index(':'):]
for row in data.split(":"):
    for col in row.split(","):
        print col[1:-1].strip(),
    print
