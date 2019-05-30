class bancor:
    total_supply = 0
    reserved_token = 0
    price = 0
    cw = 0

    def __init__(self, token, rate, cw):
        bancor.total_supply = token * rate
        bancor.reserved_token = (bancor.total_supply * cw)
        bancor.price = bancor.reserved_token / (bancor.total_supply * cw)
        bancor.cw = cw

    @staticmethod
    def issue_by_reserve_token(amount):
        smart_token_amount = bancor.total_supply * (((1 + (amount / bancor.reserved_token)) ** bancor.cw) -1)
        bancor.reserved_token = bancor.reserved_token + amount
        bancor.total_supply = bancor.total_supply + smart_token_amount
        bancor.price = bancor.reserved_token / (bancor.total_supply * bancor.cw)
        return smart_token_amount

    @staticmethod
    def destroy_by_reserve_token(amount):
        smart_token_amount = bancor.reserved_token * (1 - ((1 - (amount / bancor.total_supply)) ** (1/bancor.cw)))
        bancor.reserved_token = bancor.reserved_token -smart_token_amount
        bancor.total_supply = bancor.total_supply - amount
        bancor.price = bancor.reserved_token / (bancor.total_supply * bancor.cw)
        return smart_token_amount
