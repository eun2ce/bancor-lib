from bclib import bancor

bancor_1 = bancor(300000, 1, 0.2)
bancor_1.issue_by_reserve_token(300)
bancor_1.issue_by_reserve_token(700)
bancor_1.destroy_by_reserve_token(1302)
bancor_1.issue_by_reserve_token(100)
