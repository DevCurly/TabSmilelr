#Import browser to open webpages in browser
import webbrowser as browser    
import os
import time
Links = [
    "https://www.github.com/DevCurly", # Follow me on GitHub :)

]

# browser.open_new_tab(Links[0]) 

#for link in Links:

#    browser.open_new_tab(link)

# If the user closes the tab, open a new tab
#browser.open_new_tab(Links[0])

#while True:
#    time.sleep(1)
#    if browser.open_new_tab(Links[0]) == None:
#       browser.open_new_tab(Links[0])
def OpenAllLinks():
    linksOpened = []
    for link in Links:
        browser.open_new_tab(link)
        linksOpened.append(link)
        
    return linksOpened
# If the link is closed, open a new tab
linksOpened = OpenAllLinks()
for link in linksOpened:
    while True:
        
        if browser.open_new_tab(link) == None:
            browser.open_new_tab(link)
        time.sleep(1)


