import json
import ssl
from urllib.request import urlopen

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url=input('enter-')
data = urlopen(url, context=ctx).read()
info = json.loads(data)
ans=0
for item in info["comments"]:
    ans+=int(item['count'])
print(ans)  



#http://py4e-data.dr-chuck.net/comments_677372.json




