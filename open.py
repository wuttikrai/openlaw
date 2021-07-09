import sys
import webbrowser
import os

# get current username
username = os.getlogin()

# browser list support only 2
msedge = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"
chrome = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

# changing browser that you desire (default=chrome)
web = chrome

path = 'C:/Users/' +username+ '/law/'+str(sys.argv[1])+'/'+str(sys.argv[2])+'.pdf'
webbrowser.get(web).open_new(path)

path = 'C:/Users/' +username+ '/law/'+str(sys.argv[1])+'/'+str(sys.argv[3])+'.pdf'
webbrowser.get(web).open_new(path)

path = 'C:/Users/' +username+ '/law/'+str(sys.argv[1])+'/'+str(sys.argv[4])+'.pdf'
webbrowser.get(web).open_new(path)

path = 'C:/Users/' +username+ '/law/'+str(sys.argv[1])+'/'+str(sys.argv[5])+'.pdf'
webbrowser.get(web).open_new(path)

path = 'C:/Users/' +username+ '/law/'+str(sys.argv[1])+'/'+str(sys.argv[6])+'.pdf'
webbrowser.get(web).open_new(path)


