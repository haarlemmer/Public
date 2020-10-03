import bs4,requests,re

debug = True

def readCode(soup):
    code = soup.find("div",class_="code").string
    return code
def readSiteId(soup):
    r = re.compile("""(?<=blogId: ').*(?=')""")
    script = soup.find_all("script")
    for s in script:
        scriptstr=s.string
        if scriptstr == None:
            pass
        else:
            s2 = r.findall(scriptstr)
            for s3 in s2:
                if s2 == None:
                    pass
                else:
                    return s3
siteUrl = input("URL: ")
if debug == True:
    print(f"[Debug] Get: {siteUrl}")
site = requests.get(siteUrl)
site.encoding = site.apparent_encoding
if debug == True:
    print(f"[Debug] HTTP Status Code: {site.status_code}")
siteSoup = bs4.BeautifulSoup(site.text,"html.parser")
siteId = readSiteId(siteSoup)
if debug == True:
    print(f"[Debug] Blog ID: {siteId}")
codeUrl = f"https://my.openwrite.cn/code/generate?blogId={siteId}"
if debug == True:
    print(f"[Debug] Generate Code URL: {codeUrl}")
    print(f"[Debug] Get: {codeUrl}")
codeSite = requests.get(codeUrl)
if debug == True:
    print(f"[Debug] HTTP Status Code: {codeSite.status_code}")
codeSite.encoding = codeSite.apparent_encoding
codeSoup = bs4.BeautifulSoup(codeSite.text,"html.parser")
print(f"Code: {readCode(codeSoup)}")
