# coding: utf-8

'''链家二手房的parser'''

from parserbase import ParserBase
from bs4 import BeautifulSoup
from lzm.settings import Mongo_Root_Name
from lzm.log import getlogger

logger = getlogger(__file__)


class LJesfParser(ParserBase):

    def __init__(self):
        super(LJesfParser, self).__init__()
        self.tag = 'LJesf'

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
        blocks = soup.find_all('li', attrs={'class': 'clear'})
        for block in blocks:
            href = block.a.get('href')
            title = block.find('div', attrs={'class': 'title'}).a.text
            introduce = block.find('div', attrs={'class': 'houseInfo'}).a.text
            place = block.find('div', attrs={'class': 'houseInfo'}).text
            buildtime = block.find('div', attrs={'class': 'positionInfo'}).text
            postion = block.find('div', attrs={'class': 'positionInfo'}).a.text
            totalPrice = block.find('div', attrs={'class': 'totalPrice'}).span.text
            unitPrice = block.find('div', attrs={'class': 'unitPrice'}).span.text
            data = {'theid': theid, 'title': title, 'introduce': introduce, 'place': place, 'buildtime': buildtime,
                    'postion': postion, 'totalPrice': totalPrice, 'unitPrice': unitPrice}
            # 将所得数据存入mongo
            self.mgcoll.update({'href': href}, {'$set': data}, upsert=True)
            logger.info('parsed data, href : %s ' % href)
        self.mgcoll_root = self.mg[Mongo_Root_Name]
        self.mgcoll_root.update({'theid': theid}, {'$set': {'parsed': 1}})


'''-----test part-----'''
if __name__ == '__main__':
    with open('d:/work_code/lzmcrawler/lzm/test', 'r') as f:
        doc = f.read()
    doc = doc.replace('\\', '')
    lp = LJesfParser()




