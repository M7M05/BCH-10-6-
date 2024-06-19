
from time import sleep

#Function for finding the mudular root value.
def modularRoot(x):
    if x == 2 or x == 6 or x == 7 or x == 8 or x == 10:
        print("\nMorethan2_no_sqrt")
        sleep(5)
        exit()
    #xValue represents the numbr to root and rootValue is the sqrt(x)%11 of that value using a finate field root table.
    elif x == 1:
        return 1
    elif x == 3:
        return 5
    elif x == 4:
        return 2
    elif x == 5:
        return 4
    elif x == 9:
        return 3
    
def modularInverse (x):
    if x == 1:
        return 1
    if x == 2:
        return 6
    if x == 3:
        return 4
    if x == 4:
        return 3
    if x == 5:
        return 9
    if x == 6:
        return 2
    if x == 7:
        return 8
    if x == 8:
        return 7
    if x == 9:
        return 5
    if x == 10:
        return 10
        

#We need the user to inout a 6 digit string for the algorithm to work.
while True:
    BCHencode = (input("\nPlease input a 6 digit number: "))
    if 6==len(BCHencode) and BCHencode.isdigit:
        break
    
#Now we create a list for the input so we can generate checking digits.
BCHarr = list(map(int, BCHencode))

#Creating checking digits
c1 = (4*BCHarr[0]+10*BCHarr[1]+9*BCHarr[2]+2*BCHarr[3]+BCHarr[4]+7*BCHarr[5])%11
c2 = (7*BCHarr[0]+8*BCHarr[1]+7*BCHarr[2]+BCHarr[3]+9*BCHarr[4]+6*BCHarr[5])%11
c3 = (9*BCHarr[0]+BCHarr[1]+7*BCHarr[2]+8*BCHarr[3]+7*BCHarr[4]+7*BCHarr[5])%11
c4 = (BCHarr[0]+2*BCHarr[1]+9*BCHarr[2]+10*BCHarr[3]+4*BCHarr[4]+BCHarr[5])%11
print("\nD1 is: ",BCHarr[0]," D2 is: ",BCHarr[1]," D3 is: ",BCHarr[2]," D4 is: ",BCHarr[3],"D5 is: ",BCHarr[4],"D6 is: ",BCHarr[5]," D7 is: ",c1," D8 is: ",c2," D9 is: ",c3," D10 is: ",c4)
BCHarr.append(c1); BCHarr.append(c2); BCHarr.append(c3); BCHarr.append(c4)
tenexist = BCHarr.count(10) #Checks the list array for any ten values.
if tenexist > 0:
    print("\nMorethan2 a digit has been corrected to 10")
    sleep(5)
    exit()
#If any of the digits are 10, the code is not accepted.

#BCH Decoding.
newInp = input("\nWould you like to use use a new input for decoding? ")
if str.lower(newInp) == "yes":
    BCHdecode = input("\nPlease enter a ten digit code for decoding: ")
    BCHarr = list(map(int, BCHdecode))
    
#If the user wants to decode a different code they mey enter a new input
S1 = (BCHarr[0]+BCHarr[1]+BCHarr[2]+BCHarr[3]+BCHarr[4]+BCHarr[5]+BCHarr[6]+BCHarr[7]+BCHarr[8]+BCHarr[9])%11
S2 = (BCHarr[0]+2*BCHarr[1]+3*BCHarr[2]+4*BCHarr[3]+5*BCHarr[4]+6*BCHarr[5]+7*BCHarr[6]+8*BCHarr[7]+9*BCHarr[8]+10*BCHarr[9])%11
S3 = (BCHarr[0]+2**2*BCHarr[1]+3**2*BCHarr[2]+4**2*BCHarr[3]+5**2*BCHarr[4]+6**2*BCHarr[5]+7**2*BCHarr[6]+8**2*BCHarr[7]+9**2*BCHarr[8]+10**2*BCHarr[9])%11
S4 = (BCHarr[0]+2**3*BCHarr[1]+3**3*BCHarr[2]+4**3*BCHarr[3]+5**3*BCHarr[4]+6**3*BCHarr[5]+7**3*BCHarr[6]+8**3*BCHarr[7]+9**3*BCHarr[8]+10**3*BCHarr[9])%11
print("\nS1 is : ", S1, " ","S2 is : ", S2, " ","S3 is : ", S3, " ","S4 is : ", S4)

#Calculating P, Q and R
P = (S2**2-S1*S3)%11;   Q=(S1*S4-S2*S3)%11;   R=(S3**2-S2*S4)%11
print("\nP:",P," Q: ",Q," R: ",R,)
#Now that we have generated the required variables we can begin error checking.

#First we will check if there are no errors using the syndrome variables.
if S1 == 0 and S2 == 0 and S3 == 0 and S4 == 0:
    print("\nNo_error... \n")

#Next we need to check if there is a single error.
elif P == Q == R == 0:
    
    print("\nSingle_err at position ", (modularInverse(S2)*modularInverse(S1))%11,".", " The magnitude is ", S1,"... \n")

#Next we need to check for a double error.
if P != 0 or Q != 0 or R != 0:
       xValue = (Q**2-4*P*R)%11  
       twotimesp = (2*P)%11
       
       i = ((- Q + (modularRoot(xValue))) * modularInverse(twotimesp))%11 #The function will find the square root of the numbber in the equation.
       j = ((- Q - (modularRoot(xValue))) * modularInverse(twotimesp))%11 #The other function finds the inverse of two times the value of p which allows us to multiply where we need to divide.
       ijinverse = (i-j)%11
       
       b = ((i*S1-S2) * (modularInverse(ijinverse)))%11 #The function finds the inverse of i-j in the modular of eleven.
       a = (S1-b)%11
       
       print("\ni is : ", i, " ","a is : ", a, " ","j is : ", j, " ","b is : ", b)
       print("\nDouble_err the error positions are ", i, " and ", j, ". The magnitudes are ", a, " and ", b, ". \n") #Prints the results for the user.
       sleep(5)
       
    #There is at least a double error if P,Q,R are not all zeroes.
       if i == 0 or j == 0:
           print("\nMorethan2 _no_sqrt\n")
           sleep(5)
           exit()
            #If either i or j is equal to 0 there are at least three errors present.
       else:
           exit()
           
       
