import urllib.request
import urllib.parse #quote = To transform the raw text into a valid url parameter

#Read a file
def read_text():
    quotes = open("movie_quotes.txt")
    contentsOfFile = quotes.read()
    quotes.close()
    check_profanity(contentsOfFile)

def check_profanity(textToCheck):
    url = "http://www.wdylike.appspot.com/?q=" + urllib.parse.quote(textToCheck)
    connection = urllib.request.urlopen(url)
    output = connection.read()
    if b'true' in output:
        print("Profanaty Alert!!")
    elif b'false' in output:
        print("This document has no curse words!")
    else:
        print("Could not scan the document properly.")
read_text()
