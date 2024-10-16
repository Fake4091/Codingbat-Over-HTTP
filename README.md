Warmup 1/ near-hundred
Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.
near_hundred(93) → True
near_hundred(90) → True
near_hundred(89) → False


Warmup 2/ String-Splosion
Given a non-empty string like "Code" return a string like "CCoCodCode".
string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'


String 2/ cat-dog
Return True if the string "cat" and "dog" appear the same number of times in the given string.
cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True


Logic 2/ lone-sum
Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.
lone_sum(1, 2, 3) → 6
lone_sum(3, 2, 3) → 2
lone_sum(3, 3, 3) → 0
