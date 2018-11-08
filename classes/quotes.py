class Quotes:

    quotes = {"main_quotes": [], "bolt_ons": []}

    def __init__(self, quotes, product):
        for quote in quotes:
            if quote["businessLineId"] == "product":
                self.quotes["main_quotes"].append(quote)
            else:
                self.quotes["bolt_ons"].append(quote)

    def is_broker(self, broker_name):
        for quote in self.quotes["main_quotes"]:
            if not quote["businessId"]["productName"].str.contains(broker_name):
                Exception("Quote is not from expected broker")

    def get_bolt_ons(self):
        return self.quotes["bolt_ons"]
