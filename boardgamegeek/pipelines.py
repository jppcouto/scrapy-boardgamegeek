# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class BoardgamegeekPipeline(object):

    def __init__(self):
        self.create_conn()
        self.create_table()

    def create_conn(self):
        self.conn = sqlite3.connect("jogos.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS jogos_sqlite""")
        self.curr.execute("""create table jogos_sqlite (
            rank text,
            nome text,
            ano text,
            avaliacao text
            )""")

    def store_db(self, item):
        myquery = """INSERT into jogos_sqlite 
        (rank, nome,ano,avaliacao) 
        values (?,?,?,?)
        """
        val = (
            item.get('rank'),
            item.get('nome'),
            item.get('ano'),
            item.get('avaliacao')
        )

        self.curr.execute(myquery, val)
        self.conn.commit()

    def process_item(self, item, spider):
        self.store_db(item)
        print("Pipelines = " + item['nome'] + " (" + item['ano'] + ")")
        return item


"""
import pymongo

class BoardgamegeekPipeline(object):
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['bgg_db']
        self.collection = db['jogos_tb']


        #self.create_connection()
        #self.create_table()


    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        #self.store_db(item)
        return item
"""