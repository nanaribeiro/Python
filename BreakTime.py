import webbrowser
import time
totalBreaks = 3
breakCount = 0
print("The program begun on " + time.ctime())
while breakCount < totalBreaks:
    time.sleep(3600)
    webbrowser.open("https://www.youtube.com/watch?v=YQHsXMglC9A&list=PLBrbKtPlBbNc4XP_O9T1x55QnRh51hYuM")
    breakCount = breakCount + 1
