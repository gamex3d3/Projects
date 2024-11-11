import webbrowser

def open_url(url):
    webbrowser.open(url)
    chrome_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome_proxy.exe'
    webbrowser.get(chrome_path).open(url)

def search(search_query, search_engine):
    try:
        open_url(f"https://www.google.com/search?q=White")
    except IndexError:
        print("ERROR1")

search_query = ("for")[-1]
search_engine = ("for")[0].replace("search", "").strip().lower()
search(search_query, search_engine)