import urllib.request

res = urllib.request.urlopen("http://placekitten.com/g/200/300")
cat = res.read()

with open('cat_200_300', 'wb') as f:
    f.write(cat)
