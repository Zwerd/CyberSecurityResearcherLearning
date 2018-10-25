#this script is for checking the live address in the segment
import os
segment = str(input("Please enter segment address: "))
respons = os.system("nmap -sn -PE " + segment +"/24 | grep report ")
print (respons)
