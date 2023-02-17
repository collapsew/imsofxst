from requests_html import HTMLSession

s = HTMLSession()

def weather(query):
    url = f'https://www.google.ru/search?q=weather+{query}'
    r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41'})

    try:

        temp = r.html.find('span#wob_tm', first=True).text
        unit = r.html.find('div.vk_bk,wob-unit span.wob_t', first=True).text
        desc = r.html.find('div.VQF4g', first=True).find('span#wob-dc', first=True).text
        print(f'The weather is now "{temp}\n{desc}"')
        print(query)
    except:
        print(f'The city "{query}" was not found, try again"')

query = input('Type a city: ')
weather(query)