import requests
import lib


class Verifymagento(lib.BasePage):

    def sales_ordercard(self, orderid, ordertype,paymenttype):

        response = requests.get("https://staging.tendercuts.in:82/sale_order/order_data?order_id={}".format(orderid), headers={'Authorization': 'Token f3326e5621bcb0448bfeb5d4e70442dba8feee38'})
        data = response.json()[0]
        payment_type=data['payment_method']
        store_name=data['store']
        increment_id=data['increment_id']
        shipping_amount=data['shipping_amount']
        total_amount=data['total_amount']
        sku=data['product_list'][0]['sku']
        qty=data['product_list'][0]['ordered_qty']
        unitprice=data['product_list'][0]['unit_price']
        weight=data['product_list'][0]['weight']
        customer_phoneno=data['customer']['phone']

        if ordertype == "express" and paymenttype == "juspay":             
            assert payment_type == "juspay"
            assert "tambaram" == store_name
            assert "9710243651" == customer_phoneno
            assert orderid == increment_id
            assert shipping_amount== 39.0
            # assert unitprice == 115.0
            assert sku == "CHK_WHL_SKIN_OFF"

        elif ordertype == "schedule" and paymenttype == "juspay":
            assert payment_type == "juspay"
            assert "tambaram" == store_name
            assert "9710243651" == customer_phoneno
            assert orderid == increment_id
            assert shipping_amount== 29.0
            assert unitprice == 199.0
            assert sku == "MRT_KOLA_URUNDAI"

        elif ordertype == "express" and paymenttype == "cashondelivery":
            assert payment_type == "cashondelivery"
            assert "tambaram" == store_name
            assert "9710243651" == customer_phoneno
            assert orderid == increment_id
            assert shipping_amount== 39.0 
            # assert unitprice == 115.0
            assert sku == "CHK_WHL_SKIN_OFF"

        elif ordertype == "schedule" and paymenttype == "cashondelivery":
            assert payment_type == "cashondelivery"
            assert "tambaram" == store_name
            assert "9710243651" == customer_phoneno
            assert orderid == increment_id
            assert shipping_amount== 29.0
            assert unitprice == 199.0
            assert sku == "MRT_KOLA_URUNDAI"
