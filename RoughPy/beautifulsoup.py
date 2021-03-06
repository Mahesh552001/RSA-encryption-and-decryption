# =============================================================================
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import ssl
# 
# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
# 
# url = input('Enter - ')
# html = urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, "html.parser")
# 
# tags = soup('a')
# for tag in tags:
#     # Look at the parts of a tag
#     print('TAG:', tag)
#     print('URL:', tag.get('href', None))
#     print('Contents:', tag.contents[0])
#     print('Attrs:', tag.attrs)
# http://py4e-data.dr-chuck.net/comments_677369.html
# 
# =============================================================================
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
count=1
url = input('Enter - ')
for i in range(0,7):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
    tags = soup('a')
    a=[]
    a.clear()
    for tag in tags:
        a.append(tag.get('href', None))
    url=a[17]
    print(url)
    
#http://py4e-data.dr-chuck.net/known_by_Dacia.html
