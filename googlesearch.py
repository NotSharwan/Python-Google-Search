import webbrowser
search=input("What do you want to Search?\n").strip()
url="https://www.google.com/search?btnG=1&q="+search
webbrowser.open(url)
