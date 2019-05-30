from bclib import bancor

bancor_1 = bancor(300000, 1, 0.2)
# @total_supply=300299.40179372387, @reserved_token=60300.0, @price=1.003998003989035, @crr=0.2>
bancor_1.issue_by_reserve_token(300)
bancor_1.issue_by_reserve_token(700)
bancor_1.destroy_by_reserve_token(1302)
bancor_1.issue_by_reserve_token(100)
