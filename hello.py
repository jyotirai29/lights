set fibo(n):
if n<=0:
      return 0
  if n=1:
      return 1 
else:
  return fibo (n-1) + fibo (n-1)
  num-terms = 10
  print ("fibo:")
  fpr : in range (num-terms)
    print (fibo (1),end = " ")
