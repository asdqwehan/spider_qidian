from bs4 import BeautifulSoup
import requests
import json
import time

def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False)+'\n')

def get_html(url):
    response = requests.get(url)
    return response.text

def parse_html(html):
    soup = BeautifulSoup(html, 'lxml')
    book_info = soup.find_all(attrs={'class': 'book-mid-info'})
    for each_book in book_info:
        yield [
            each_book.find(attrs={'data-eid': 'qd_C40'}).text,
            each_book.find(attrs={'data-eid': 'qd_C41'}).text,
            each_book.find(attrs={'data-eid': 'qd_C42'}).text,
            each_book.find('span').text,
        ]

if __name__ == '__main__':
    page_nums = 25
    page_num = 1
    while page_num <= page_nums:
        url = 'https://www.qidian.com/rank/recom' + '?page=' + str(page_num)
        html = get_html(url)
        for each in parse_html(html):
            write_to_file(each)
        print('page%d done.'%page_num)
        time.sleep(1)
        page_num += 1
    print('All done.')