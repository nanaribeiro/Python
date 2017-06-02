import urllib.request

#Read a file
def read_text():
    quotes = open("movie_quotes.txt")
    contentsOfFile = quotes.read()
    print(contentsOfFile)
    quotes.close()
    check_profanity(contentsOfFile)

def check_profanity(textToCheck):
    url = "http://www.wdylike.appspot.com/?q=" + textToCheck 
    connection = urllib.request.urlopen(url)
    output = connection.read()
    print(output)
read_text()
