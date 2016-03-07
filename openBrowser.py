import webbrowser
import time
i = 0
breaks = 0
while breaks < 3:
    time.sleep(i+30)
    webbrowser.open("http://jaynejacobs.com")
    breaks = breaks + 1
    i=i+5
print "i is" , i



    
