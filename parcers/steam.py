import requests


def steam_pr(text):
    text = '+'.join(text.split())
    site = f'https://store.steampowered.com/search/?term={text}'
    r = requests.get(site)
    if r.status_code == 200:
        try:
            rt = r.text[
                 r.text.index('<div class="col search_price') + 20: r.text.index('<div class="col search_price') + 500]
            print(rt)
        except:
            pass
