""" Create functions that can find out if number is prime, can find a prime number within a range of values and computes N, used in RSA ecryption """

def isPrime(number):
  for i in range(2, number):
    if number % i == 0:
      return False
  return True

def findPrime(start, end):
  for i2 in range(start, end+1):
    if isPrime(i2):
      return i2


def encrypt():
  x= int(input("Provide a integer: "))
  y= int(input("Provide a second integer (larger): "))
  p1 = findPrime(x,y)
  x= int(input("Provide a integer: "))
  y= int(input("Provide a second integer (larger): "))
  p2 = findPrime(x,y)
  return p1*p2

print(encrypt())

