
import os

def taxes():
    status = int(input("Enter 1 for Single\n Enter 2 for Married Filing Jointly or Qualifying Widow(er)\n "
          "Enter 3 for Married Filing Separately\n Enter 4 for Head of Household\n "))
    income = int(input("Enter your Taxable Income\n"))

    if (status == 1 or status == 3) and ((income >0) and (income <=8350)):
        taxdue= income*(10/100)
        print(f"Your Tax rate is 10% and Your Tax Amount is ${taxdue}")
    elif (status == 1 or status == 3) and ((income >=8351) and (income <=33950)):
        taxdue = income * (15 / 100)
        print(f"Your Tax rate is 15% and Your Tax Amount is ${taxdue}")
    elif (status == 1 or status == 3) and ((income >= 33951) and (income <= 82250)):
        taxdue = income * (25 / 100)
        print(f"Your Tax rate is 25% and Your Tax Amount is ${taxdue}")
    elif (status == 1 or status == 3) and ((income >=82251) and (income <=171550)):
        taxdue = income * (28 / 100)
        print(f"Your Tax rate is 28% and Your Tax Amount is ${taxdue}")
    elif (status == 1 or status == 3) and ((income >=171551) and (income <=372950)):
        taxdue = income * (33 / 100)
        print(f"Your Tax rate is 33% and Your Tax Amount is ${taxdue}")
    elif (status == 1 or status == 3) and (income >=372951):
        taxdue = income * (35 / 100)
        print(f"Your Tax rate is 35% and Your Tax Amount is ${taxdue}")
    elif (status == 2) and ((income > 0) and (income <=16700)):
        taxdue = income * (10 / 100)
        print(f"Your Tax rate is 10% and Your Tax Amount is ${taxdue}")
    elif (status == 2) and ((income >=16701) and (income <=67900)):
        taxdue = income * (15 / 100)
        print(f"Your Tax rate is 15% and Your Tax Amount is ${taxdue}")
    elif (status == 2) and ((income >=67901) and (income <=137050)):
        taxdue = income * (25 / 100)
        print(f"Your Tax rate is 25% and Your Tax Amount is ${taxdue}")
    elif (status == 2) and ((income >=137051) and (income <=208850)):
        taxdue = income * (28 / 100)
        print(f"Your Tax rate is 28% and Your Tax Amount is ${taxdue}")
    elif (status == 2) and ((income >=171551) and (income <=372950)):
        taxdue = income * (33 / 100)
        print(f"Your Tax rate is 33% and Your Tax Amount is ${taxdue}")
    elif (status == 2) and (income >=372951):
        taxdue = income * (35 / 100)
        print(f"Your Tax rate is 35% and Your Tax Amount is ${taxdue}")
    elif (status == 4) and ((income >=0) and (income <=11950)):
        taxdue = income * (10 / 100)
        print(f"Your Tax rate is 10% and Your Tax Amount is ${taxdue}")
    elif (status == 4) and ((income >=11951) and (income <=45500)):
        taxdue = income * (15 / 100)
        print(f"Your Tax rate is 15% and Your Tax Amount is ${taxdue}")
    elif (status == 4) and ((income >=45501) and (income <=117450)):
        taxdue = income * (25 / 100)
        print(f"Your Tax rate is 25% and Your Tax Amount is ${taxdue}")
    elif (status == 4) and ((income >=117451) and (income <=190200)):
        taxdue = income * (28 / 100)
        print(f"Your Tax rate is 28% and Your Tax Amount is ${taxdue}")
    elif (status == 4) and ((income >=190201) and (income <=372950)):
        taxdue = income * (33 / 100)
        print(f"Your Tax rate is 33% and Your Tax Amount is ${taxdue}")
    elif (status == 4) and (income >=372951):
        taxdue = income * (35 / 100)
        print(f"Your Tax rate is 35% and Your Tax Amount is ${taxdue}")





if __name__ == '__main__':
    taxes()