import lib
import MySQLdb
import datetime


class Inventory(lib.BasePage):

    def gramsinventory(self, productid, qty, forecastqty):
        today = format(datetime.date.today(), "%y-%m-%d")
        db= MySQLdb.connect(host="139.162.51.169", user="root", passwd="!qazmlp)5", db="v3_5", port=3306)
        cur = db.cursor()
        deletequery="""DELETE FROM graminventory WHERE product_id=193"""
        query = """INSERT INTO graminventory (date,product_id,store_id,opening,qty,expiringtoday,forecastqty) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
        cur.execute(deletequery)
        cur.execute(query, (today,productid,7,100.0000,qty,00.0000,forecastqty))
        db.commit()

    def storecreditamount(self):
        db= MySQLdb.connect(host="139.162.51.169", user="root", passwd="!qazmlp)5", db="v3_5", port=3306)
        cur = db.cursor()
        updatequery="""UPDATE m_credit_balance SET amount=0 WHERE customer_id=50263"""     
        query = """UPDATE m_credit_balance SET amount =100 WHERE customer_id=50263"""
        cur.execute(updatequery)
        cur.execute(query)
        db.commit()
