# file:classes/bolt_ons_model.py
# -----------------------------------------------------------------------------
# Bolt_ons rules:
# -----------------------------------------------------------------------------
class Bolt_ons(object):
    boltons = {}
    def __init__(self, name, price=None, availabality=None, selected=False):
        if availabality:
        self.boltons[name] = {"price":price, "selected":selected }

    def bolt_ons_validation(self,actual_bolt_ons):
        for actual in actual_bolt_ons:
            if actual["productName"] in self.boltons:
                if self.boltons[actual["productName"]]["selected"] == actual[]:

                else:
                    Exception("Bolton auto selection state is unexpected")
            else:
                Exception("Unexpected bolt-ons in results")

