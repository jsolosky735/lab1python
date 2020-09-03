# Author: Jamys Solosky jjs7331@psu.edu   
# Collaborator: Colton Giordano jcg5896@psu.edu  
# Collaborator: Lauren Hughes lmh5981@psu.edu  
# Collaborator: Timothy Zheng txz5165@psu.edu  
temp = input("Enter temperature: ")
unit = input("Enter unit in F/f or C/c: ")
temp = float(temp)

if unit == "C" or unit =="c":
  print(f"{temp}\N{degree sign} in Celsius is equivalent to {temp*9/5+32}\N{degree sign} Fahrenheit.")
elif unit == "F" or unit == "f":
  print(f"{temp}\N{degree sign} in Fahrenheit is equivalent to {(temp-32)*5/9}\N{degree sign} Celsius.")
else: print(f"Invalid unit({unit}).")