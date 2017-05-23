# coding: utf-8

'''创业邦事件的parser'''

from parserbase import ParserBase
from bs4 import BeautifulSoup
from lzm.settings import Mongo_Root_Name
from lzm.log import getlogger
from lxml import etree
from scrapy.selector import Selector

logger = getlogger(__file__)


class CYeventParser(ParserBase):

    def __init__(self):
        super(CYeventParser, self).__init__()
        self.tag = 'CYevent'

    def can(self, parername):
        if parername == self.tag:
            return True
        else:
            return False

    def detailparse(self, doc):
        mgcollname = doc.get('collname', '')
        theid = doc.get('theid')
        if not mgcollname:
            return
        self.mgcoll = self.mg[mgcollname]
        content = doc.get('rootpage', '')
        soup = BeautifulSoup(content, 'html.parser')
        baseurl = doc.get('baseurl', '')

        blocks = soup.find_all('tr', attrs={'class': 'table-plate3'})
        for block in blocks:
            href = block.td.a.get('href')
            title = block.find('td', attrs={'class': 'tp2'}).find('span', attrs={'class': 'tp2_tit'}).text
            tit_name = block.find('td', attrs={'class': 'tp2'}).find('span', attrs={'class': 'tp2_com'}).text
            money = block.find('td', attrs={'class': 'tp-mean'}).find('div', attrs={'class': 'money'}).text
            rounds = block.contents[7].text
            try:
                investors = block.find('td', attrs={'class': 'tp3'}).text
            except:
                investors = ''
            data = {'theid': theid, 'baseurl': baseurl, 'title': title, 'tit_name': tit_name, 'money': money,
                    'rounds': rounds, 'investors': investors}
            # 将所得数据存入mongo
            self.mgcoll.update({'href': href}, {'$set': data}, upsert=True)
            logger.info('parsed data, href : %s ' % href)


'''---------test part-----------'''
if __name__ == '__main__':
    l = CYeventParser()
    mgcoll = l.mg['rootpages']
    for doc in mgcoll.find({'theid': 'e52d40ca8bf26ea0e882f3545d3859b2'}):
        l.detailparse(doc)
