import pytest

from bclib import bancor

bancor_test = bancor(300000, 1, 0.2)
assert bancor_test.issue_by_reserve_token(300) == 299.40179372385245
assert bancor_test.issue_by_reserve_token(700) == 693.9974382206417
assert bancor_test.destroy_by_reserve_token(1302) == 1307.966524590907
assert bancor_test.issue_by_reserve_token(100) == 100.34530853232869
