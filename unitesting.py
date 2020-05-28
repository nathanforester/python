import unittest
#from unittest import TestCase
# from new_bizz_buzz import *

# def check_if_digit_div_num(digit, num_div):
#     return digit % num_div == 0

# def assertTrue(arg1, arg2):
#     print(arg1 == arg2)
#

class Tests(unittest.TestCase):

    def test(self):
        self.assertTrue(check_if_digit_div_num('bread', 'water'), True)
        self.assertTrue(check_if_digit_div_num('water', 'bread'), True)
        self.assertTrue(check_if_digit_div_num('bread', 'bread'), False)
        self.assertTrue(check_if_digit_div_num('water', 'water'), False)
        self.assertTrue(check_if_digit_div_num('bread', 'paraffin'), False)
        self.assertTrue(check_if_digit_div_num('paraffin', 'water'), False)
        self.assertTrue(check_if_digit_div_num('paraffin', 'paraffin'), True)
        # print(check_if_digit_div_num(5, 5) == True)
        if __name__ == '__main__':
            # print("I was called directly")
            unittest.main()

# from new_bizz_buzz import check_if_digit_div_num
#
# known_number_1 = 5
# known_number_2 = 5
# expected_number_output = 0
#
# print("Testing function check_if_digit_div_num() with '5, 5' ---> '0'")
# print(check_if_digit_div_num(known_number_1, known_number_2), (expected_number_output))



