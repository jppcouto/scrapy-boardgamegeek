# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
#from itemadapter import ItemAdapter
import sqlite3

# Scrapy would try and run this otherwise!

if __name__ == "__main__":

    conn = sqlite3.connect('jogos.db')
    cur = conn.cursor()
    a = cur.execute("""select * from  jogos_sqlite """)
    for rows in a.fetchall():
        print(rows)
    conn.close()