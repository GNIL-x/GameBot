import requests


def steam_pr(text):
    text = '+'.join(text.split())
    site = f'https://store.steampowered.com/search/?term={text}'
    r = requests.get(site)
    if r.status_code == 200:
        try:
            rt = r.text[
                 r.text.index('<div class="col search_price') + 20: r.text.index('<div class="col search_price') + 500]
            if '<span style="color: #888888;">' in rt:
                rt = rt[rt.index('<span style="color: #888888;">') + 38:rt.index('<span style="color: #888888;">') + 90]
                origin = rt[:rt.index('</strike></span><br>')]
                discount = rt[rt.index('</strike></span><br>') + len('</strike></span><br>'):]
                return origin, discount
            elif '<div class="col search_price  responsive_secondrow">' in rt:
                rt = rt[rt.index('<div class="col search_price  responsive_secondrow">') + 60:rt.index(
                    '<div class="col search_price  responsive_secondrow">') + 100].lstrip(' ').rstrip(' ')
                return rt
            else:
                rt = 'Такой игры не существует😭😭😭😭'
                return rt
        except:
            return 'Такой игры не существует😭😭😭😭'
