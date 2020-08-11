import requests
from bs4 import BeautifulSoup
import pprint


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda key: key['votes'], reverse=True)


def create_custom_hm(links, subtext):
    hn = []

    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


def method_name(page):
    res = requests.get(f'http://news.ycombinator.com/news?p={page}')
    soup = BeautifulSoup(res.text, 'html.parser')
    links = soup.select('.storylink')
    subtext = soup.select('.subtext')

    return links, subtext


result = method_name(2)
result2 = method_name(1)
pprint.pprint(create_custom_hm(result[0] + result2[0], result[1] + result2[1]))

# for vote in votes:
#     score = vote.text.split(' ')[0]
#     print(score)
