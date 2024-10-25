# shop:tata car service(2 and 4 wheeler)

# 4 wheels(4 choice types of 4 whellers)
# sumo>per hr charges---500>6hr taken

# 500*6+tax    
# name of customer>charges per>no.of hr taken>name of car


print("****************TATA CAR SERVICE*****************")
print("*************************************************")
print("Types of Vehicles available for rent::")
print("               1. 2 Wheelers")
print("               2. 4 Wheelers")
print("*************************************************")
enter=int(input("Enter your choice::"))
if enter==1:
    print("You have selected 2 Wheelers")
    print("There are 4 types of 2 wheelers:")
    print("       1. Bullet")
    print("       2. KTM")
    print("       3. Hayabusa")
    print("       4. Scooty")
    twowheeler=int(input("Please enter which 2 Wheeler you want::"))
    if twowheeler==1:
        print("You have selected Bullet")
        print("Per hr charges for bullet is 500")
        bullet=int(input("Enter the number of hr you have borrowed::"))
        hr=500
        tax=0.18
        total=hr*bullet+tax
        print("*******Invoice*******")
        print("Bike name::Bullet")
        print("No. of Hrs::"f'{bullet}')
        print("Tax::"f'{tax}')
        print("The total bill::"f'{total}')
        print("Thankyou Vist Again")
        
    elif twowheeler==2:
        print("You have selected KTM")
        print("Per hr charges for KTM is 780")
        ktm=int(input("Enter the number of hr you have borrowed::"))
        hr=780
        tax=0.15
        total=hr*ktm+tax
        print("*******Invoice*******")
        print("Bike name::KTM")
        print("No. of Hrs::"f'{ktm}')
        print("Tax::"f'{tax}')
        print("The total bill::"f'{total}')
        print("Thankyou Vist Again")
        
    elif twowheeler==3:
        print("You have selected Hayabusa")
        print("Per hr charges for Hayabusa is 1200")
        haya=int(input("Enter the number of hr you have borrowed::"))
        hr=1200
        tax=0.25
        total=hr*haya+tax
        print("*******Invoice*******")
        print("Bike name::KTM")
        print("No. of Hrs::"f'{haya}')
        print("Tax::"f'{tax}')
        print("The total bill::"f'{total}')
        print("Thankyou Vist Again")
        
    elif twowheeler==4:
        print("You have selected Scoooty")
        print("Per hr charges for Hayabusa is 450")
        scootyy=int(input("Enter the number of hr you have borrowed::"))
        hr=450
        tax=0.15
        total=hr*scootyy+tax
        print("*******Invoice*******")
        print("Bike name::KTM")
        print("No. of Hrs::"f'{scootyy}')
        print("Tax::"f'{tax}')
        print("The total bill::"f'{total}')
        print("Thankyou Vist Again")
else:
    print("You have selected 4 Wheelers")
    print("There are 4 types of 4 wheelers:")
    print("       1. Fortuner")
    print("       2. Thar")
    print("       3. XUV")
    print("       4. Suzuki")
    fourwheeler=int(input("Please enter which 4 Wheeler you want::"))
    if fourwheeler==1:
        print("You have selected Fortuner")
        print("Per hr charges for Fortuner is 1200")
        fortuner=int(input("Enter the number of hr you have borrowed::"))
        hr=700
        tax=0.18
        total=hr*fortuner+tax
        print("*******Invoice*******")
        print("Bike name::Fortuner")
        print("No. of Hrs::"f'{fortuner}')
        print("Tax::"f'{tax}')
        print("The total bill::"f'{total}')
        print("Thankyou Vist Again")
        print("***************************")
    elif fourwheeler==2:
        print("You have selected Thar")
        print("Per hr charges for Thar is 1200")
        thar=int(input("Enter the number of hr you have borrowed::"))
        hr=600
        tax=0.18
        total=hr*thar+tax
        print("*******Invoice*******")
        print("Bike name::Thar")
        print("No. of Hrs::"f'{thar}')
        print("Tax::"f'{tax}')
        print("The total bill::"f'{total}')
        print("Thankyou Vist Again")
        print("***************************")
    elif fourwheeler==3:
        print("You have selected XUV")
        print("Per hr charges for XUV is 1200")
        xuv=int(input("Enter the number of hr you have borrowed::"))
        hr=750
        tax=0.18
        total=hr*xuv+tax
        print("*******Invoice*******")
        print("Bike name::Thar")
        print("No. of Hrs::"f'{xuv}')
        print("Tax::"f'{tax}')
        print("The total bill::"f'{total}')
        print("Thankyou Vist Again")
        print("***************************")
    elif fourwheeler==4:
        print("You have selected Suzuki")
        print("Per hr charges for Suzuki is 1200")
        suz=int(input("Enter the number of hr you have borrowed::"))
        hr=850
        tax=0.18
        total=hr*suz+tax
        print("*******Invoice*******")
        print("Bike name::Thar")
        print("No. of Hrs::"f'{suz}')
        print("Tax::"f'{tax}')
        print("The total bill::"f'{total}')
        print("Thankyou Vist Again")
        print("***************************")
    
