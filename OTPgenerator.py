#import library
import math,random

#Generate OTP

def generateOTP()

#declare variables
  digits="0123456789
  OTP=""
  
  for i in range(4) :
		OTP += digits[math.floor(random.random() * 10)]
    
    return OTP

# Driver code
if __name__ == "__main__" :
	
	print("OTP of 4 digits:", generateOTP())
  
  
