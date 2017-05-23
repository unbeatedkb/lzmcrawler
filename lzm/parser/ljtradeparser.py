# coding: utf-8

'''链家成交记录的parser'''

from parserbase import ParserBase
from bs4 import BeautifulSoup
from lzm.log import getlogger

logger = getlogger(__file__)


class LJtradeParser(ParserBase):

    def __init__(self):
        super(LJtradeParser, self).__init__()
        self.tag = 'LJtrade'

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

        for block in soup.find_all('div', attrs={'class': 'info'}):
            href = block.a.get('href')
            title = block.find('div', attrs={'class': 'title'}).a.text
            houseInfo = block.find('div', attrs={'class': 'houseInfo'}).text
            positionInfo = block.find('div', attrs={'class': 'positionInfo'}).text
            source = block.find('div', attrs={'class': 'source'}).text
            unitPrice = block.find('div', attrs={'class': 'unitPrice'}).span.text
            totalPrice = block.find('div', attrs={'class': 'totalPrice'}).span.text
            dealCycleeInfo = block.find('div', attrs={'class': 'dealCycleeInfo'}).text
            dealDate = block.find('div', attrs={'class': 'dealDate'}).text
            try:
                dealHouseInfo = block.find('div', attrs={'class': 'dealHouseInfo'}).text
            except:
                dealHouseInfo = ''

            data = {'theid': theid, 'baseurl': baseurl, 'title': title, 'houseInfo': houseInfo, 'positionInfo': positionInfo,
                    'source': source, 'unitPrice': unitPrice, 'totalPrice': totalPrice,
                    'dealCycleeInfo': dealCycleeInfo, 'dealDate': dealDate, 'dealHouseInfo': dealHouseInfo}
            # 将所得数据存入mongo
            self.mgcoll.update({'href': href}, {'$set': data}, upsert=True)
            logger.info('parsed data, href : %s ' % href)


'''---------test part-----------'''
if __name__ == '__main__':
    l = LJtradeParser()
    doc = {}
    l.detailparse(doc)

