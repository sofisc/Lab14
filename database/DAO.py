from database.DB_connect import DBConnect
from model.orders import Order
from model.store import Store


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllOrdini(store):
        conn = DBConnect.get_connection()

        result = []
        cursor = conn.cursor(dictionary=True)
        query="""
        select o.*
        from orders o , stores s 
        where o.store_id = s.store_id and s.store_name = %s
        """
        cursor.execute(query,(store,))
        for row in cursor:
            result.append(Order(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllStore():
        conn = DBConnect.get_connection()

        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
           select *
           from stores 
           """
        cursor.execute(query)
        for row in cursor:
            result.append(Store(**row))
        cursor.close()
        conn.close()
        return result
