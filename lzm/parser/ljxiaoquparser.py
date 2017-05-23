# coding: utf-8

'''链家小区详情的parser'''

from parserbase import ParserBase
from bs4 import BeautifulSoup
from lzm.log import getlogger

logger = getlogger(__file__)


class LJxiaoquParser(ParserBase):

    def __init__(self):
        super(LJxiaoquParser, self).__init__()
        self.tag = 'LJxiaoqu'

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

        blocks = soup.find_all('li', attrs={'class': 'clear xiaoquListItem'})
        for block in blocks:
            href = block.a.get('href')
            title = block.find('div', attrs={'class': 'title'}).a.text
            houseInfo = block.find('div', attrs={'class': 'houseInfo'}).text.strip('\n')
            positionInfo = block.find('div', attrs={'class': 'positionInfo'}).text.strip('\t').replace(' ', '').strip('\n')
            totalPrice = block.find('div', attrs={'class': 'totalPrice'}).text
            priceDesc = block.find('div', attrs={'class': 'priceDesc'}).text.strip('\n')
            xiaoquListItemSellCount = block.find('div', attrs={'class': 'xiaoquListItemSellCount'}).text.strip('\n')
            data = {'theid': theid, 'title': title, 'houseInfo': houseInfo, 'positionInfo': positionInfo,
                    'totalPrice': totalPrice,
                    'priceDesc': priceDesc, 'xiaoquListItemSellCount': xiaoquListItemSellCount}
            # print href
            # print title
            # print houseInfo
            # print positionInfo
            # print totalPrice
            # print priceDesc
            # print xiaoquListItemSellCount
            # 将所得数据存入mongo
            self.mgcoll.update({'href': href}, {'$set': data}, upsert=True)
            logger.info('parsed data, href : %s ' % href)


'''---------test part-----------'''
if __name__ == '__main__':
    l = LJxiaoquParser()
    mgcoll = l.mg['rootpages']
    for doc in mgcoll.find({'theid': '7352501f44f3d203501c582b40262af3'}):
        l.detailparse(doc)
        input()

