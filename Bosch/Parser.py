from bs4 import BeautifulSoup


def str_connect(items):
    return ''.join([item.get_text() for item in items.find_all('span', recursive=False)])


def search_chapter(path):
    with open(path, 'r') as f:
        soup = BeautifulSoup(f, "html.parser")
    return (str_connect(items) for items in soup.find_all('h1'))


def search_table(path):
    with open(path, 'r') as f:
        soup = BeautifulSoup(f, "html.parser")
        for table in soup.find_all('table'):
            formula = {}
            for tr in table.tbody.find_all('tr'):
                item = [td.string for td in tr.find_all('td')]
                try:
                    formula[item[0]] = item[1]
                except IndexError:
                    print item
            yield formula


def search_tabletitle(path):
    with open(path, 'r') as f:
        soup = BeautifulSoup(f, "html.parser")
        for tabletitle in soup.find_all('p', class_="rgTableTitle"):
            print tabletitle


def search_toc(path):
    with open(path, 'r') as f:
        soup = BeautifulSoup(f, "html.parser")
    return soup.find_all("div", class_="TOC")


if __name__ == '__main__':
    for title in search_toc(r'C:\Users\sd\Desktop\sldemo_engine\root.html'):
        print title
