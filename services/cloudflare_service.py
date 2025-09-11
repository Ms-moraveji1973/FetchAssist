import cloudscraper

def cloudflare(url:str):
    print('this function is called')
    scraper = cloudscraper.create_scraper()
    print('--- scraper created ---')
    response = scraper.get(url)
    content = response.content
    status = response.status_code
    return  content, status