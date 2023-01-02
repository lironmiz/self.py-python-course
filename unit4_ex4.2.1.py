# exercise 4.2.1 from unit 4
'''
Here are a couple of code snippets. For each couple, complete whether the couple's output
will be the same or different. 
(Write the word "same" or "different" in the box, without quotation marks)

Guidelines
Assume that the variable rain_mm is of type integer (int).
Assume that the variable in both code snippets has the same value.
Recommendation: Test each pair of code sections using different variable values.
Recommendation: use a truth table.
'''
# first code:
if rain_mm < 6 and rain_mm > 4:
  print("illegal")
else:
  print("legal")
  
# second code:
if not (rain_mm == 5):
  print("legal")
else:
  print("illegal")
  
# Enswer: same

# first code:
if rain_mm > 20 and rain_mm < 40:
  print("legal")
else:
  print("illegal")
  
# second code:
if not (rain_mm < 20 and rain_mm > 40):
  print("legal")
else:
  print("illegal")
  
# Enswer: different

# first code:
if rain_mm > 6 and rain_mm < 4:
  print("illegal")
else:
  print("legal")
  
# second code:
if not (False):
  print("legal")
else:
  print("illegal")
  
# Enswer: same  
  
  
