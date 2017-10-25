def adder(x, y):
   return x + y

def subtractor(x, y):
   return x - y

def test_adder():
   assert abs(adder(2.0, 3.0) - 5.0) < 1e-13

def test_subtractor():
   assert abs(subtractor(2.0, 3.0) - -1.0) < 1e-13
