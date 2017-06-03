import urllib2
from bs4 import BeautifulSoup

url = "https://www.nseindia.com/products/dynaContent/common/productsSymbolMapping.jsp?symbol=%s&segmentLink=3&symbolCount=1&series=EQ&dateRange=+&fromDate=%s&toDate=%s&dataType=PRICEVOLUMEDELIVERABLE"
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive',
       'Referer':'https://www.nseindia.com/products/content/equities/equities/eq_security.htm'}

def get_historical_data(symbol, startdate, enddate, outfile):
    req = urllib2.Request(url %(symbol, startdate, enddate), headers=hdr)
    page = urllib2.urlopen(req)
    soup = BeautifulSoup(page, "lxml")

    content = soup.find("div", {"id": "csvContentDiv"}).string
    headers = content[:content.index(':')]
    with open(outfile, 'wb') as f:
        f.write(headers.strip() + "\n")
        data = content[content.index(':'):]
        for row in data.split(":"):
            line = ""
            for col in row.split(","):
                line = line + col[1:-1].strip() + ","
            line = line[:-1] + "\n"
            f.write(line)
            f.flush()

if __name__ == "__main__":
    get_historical_data("SBIN", "01-01-2016", "31-12-2016", "data/sbi_2016.csv")