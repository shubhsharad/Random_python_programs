import urllib
import webbrowser
weburl = urllib.request.urlopen("https://www.reddit.com/")
html = weburl.read()
data = weburl.getcode()
url = weburl.geturl()
hd = weburl.info()
print(html)
print(data)
print(url)
print(hd)
webbrowser.open(url)
webbrowser.open_new_tab(url)