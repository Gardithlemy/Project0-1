AllowedVehicleList=["Ford F-150" , "Chevrolet Silverado" , "Tesla CyberTruck" , "Toyota Tundra" , "Nissan Titan"]
print("*" * 32)
print("Auto Country Vehicle Finder v0.1")
print("*" * 32)
print("Please Enter the following number below from the following menu:")
print()

print("1.PRINT all Authorized Vehicles")
print("2.Exit")

choice=int(input())

if choice==1:
    print("The AutoCountry sales manager has authorized the purchase and sale of the following vehicles:")
    for v in AllowedVehicleList:
        print(v)
else:
    print("Thank you for using the AutoCountry Vehicle Finder,goodbye!") 
