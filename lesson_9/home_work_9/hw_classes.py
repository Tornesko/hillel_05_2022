exchange_rates = [
    {"from": "UAH", "to": "USD", "value": 0.034},
    {"from": "USD", "to": "UAH", "value": 29.4},
    {"from": "RUB", "to": "USD", "value": 0},
    {"from": "USD", "to": "RUB", "value": 9999999999999999999},
    {"from": "ZL", "to": "USD", "value": 0.22},
    {"from": "USD", "to": "ZL", "value": 4.45},
]


class Price:
    def __init__(self, amount: int, currency: str):
        self.amount: int = amount
        self.currency: str = currency

    def buy_usd(self):
        loc_lst = []
        if self.currency != "USD":
            for dct in exchange_rates:
                if dct.get("from") == self.currency:
                    loc_lst.append(dct.get("value"))

            return self.amount * loc_lst[0]
        return self.amount

    def __add__(self, other):

        if self.currency == other.currency:
            return self.amount + other.amount
        elif self.currency == "USD":
            return self.amount + other.buy_usd()
        elif other.currency == "USD":

            loc_lst = []
            a = self.buy_usd() + other.ammount
            for dct in exchange_rates:
                if dct.get("to") == self.currency:
                    loc_lst.append(dct.get("value"))
            return a * loc_lst[0]

        else:
            loc_lst = []
            a = self.buy_usd() + other.buy_usd()
            for dct in exchange_rates:
                if dct.get("to") == self.currency:
                    loc_lst.append(dct.get("value"))
            return a * loc_lst[0]

    def __sub__(self, other):
        if self.currency == other.currency:
            return self.amount - other.amount
        elif self.currency == "USD":
            return self.amount - other.buy_usd()
        elif other.currency == "USD":

            loc_lst = []
            a = self.buy_usd() - other.ammount
            for dct in exchange_rates:
                if dct.get("to") == self.currency:
                    loc_lst.append(dct.get("value"))
            return a * loc_lst[0]

        else:
            loc_lst = []
            a = self.buy_usd() - other.buy_usd()
            for dct in exchange_rates:
                if dct.get("to") == self.currency:
                    loc_lst.append(dct.get("value"))
            return a * loc_lst[0]


# _______________ tests ____________
us = Price(1000, "USD")
hr = Price(10000, "UAH")
us2 = Price(400, "USD")
hr2 = Price(2000, "UAH")
zl = Price(500, "ZL")
print(us - us2, us + hr, hr + hr2, us2 - hr2, zl + hr2, sep="\n")
# ----------------------------------------
# 600
# 1340.0
# 12000
# 332.0
# 792.1
# ----------------------------------------
