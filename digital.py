from csv import DictWriter
from bs4 import BeautifulSoup
from requests import get


def parse(mes):
    new = 'catalog/?q=' + mes
    rel = []
    with open('base.csv', mode='w', encoding='utf8') as f:
        tt = DictWriter(f, fieldnames=['title', 'link'], delimiter=';')
        tt.writeheader()
        row = {}
        res = get('https://diskomir.ru/' + new)
        soup = BeautifulSoup(res.text, 'html.parser')
        for tag in soup.find_all('li'):
            tag = str(tag).split('><')[0]
            for i, t in enumerate(tag.split('<a')):
                t = t[t.find('href') + 5: t.find('a>') - 16]
                if i > 2:
                    row['link'] = t.split('">')[0][1:]
                    row['title'] = t.split('">')[1][36:-18]
                    rel.append((row['title'], row['link']))
                    tt.writerow(row)
    return rel