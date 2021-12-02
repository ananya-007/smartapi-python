######
# Example to get order status over web sockets

from smartapi import SmartConnect
from smartapi import SmartWebSocketOrder
import time

CLIENT_ID = "fill_your_client_id"
CLIENT_PASSWORD = "your_password"
PRIVATE_KEY = "your_api_key"


def create_session():
    # create object of call
    session = SmartConnect(api_key=PRIVATE_KEY,
                           # optional
                           # access_token = "your access token",
                           # refresh_token = "your refresh_token"
                           )

    # login api call
    data = session.generateSession(CLIENT_ID, CLIENT_PASSWORD)
    return session, data


def place_order(session):
    # place order
    try:
        orderparams = {
            "variety": "AMO",
            "tradingsymbol": "ITC-EQ",
            "symboltoken": "1660",
            "transactiontype": "BUY",
            "exchange": "NSE",
            "ordertype": "LIMIT",
            "producttype": "DELIVERY",
            "duration": "DAY",
            "price": "220",
            "squareoff": "0",
            "stoploss": "0",
            "quantity": "1"
        }
        orderId = session.placeOrder(orderparams)
        print("The order id is: {}".format(orderId))
    except Exception as e:
        print("Order placement failed: {}".format(e.message))


def on_message(ws, message):
    print("-----------------------------------------------------------------------------------------")
    print("on message")
    print("Status: {}".format(message))


def on_open(ws):
    print("-----------------------------------------------------------------------------------------")
    print("on open")
    ss.subscribe()
    time.sleep(2)
    place_order(session)


def on_error(ws, error):
    print("-----------------------------------------------------------------------------------------")
    print("on error")
    print(error)
    print("-----------------------------------------------------------------------------------------")


def on_close(ws):
    print("-----------------------------------------------------------------------------------------")
    print("on close")


session, data = create_session()
ss = SmartWebSocketOrder(data['data']['jwtToken'], CLIENT_ID, PRIVATE_KEY)
# Assign the callbacks.
ss._on_open = on_open
ss._on_message = on_message
ss._on_error = on_error
ss._on_close = on_close
ss.connect()
