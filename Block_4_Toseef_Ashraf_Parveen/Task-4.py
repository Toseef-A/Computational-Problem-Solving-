#overall number of kits supplied
OverallKits = 2000
#Number of kits supplied by Uzumaki Safety Suppliers
UzumakiKitsSupplied = 1500
#Number of kits supplied by Khairan Safety Company
KhairanKitsSupplied = 500


#Percentage given of defective kits supplied by Uzumaki Safety Suppliers (20% = 0.2)
UzumakiFaultyPercentage = 0.2
print("The percentage of faulty items supplied by Uzumaki is: ", UzumakiFaultyPercentage * 100, "%")
#Percentage given of defective kits supplied by Khairan Safety Company (10% = 0.1)
KhairanFaultyPercentage = 0.1
print("The percentage of faulty items supplied by Khairan is: ", KhairanFaultyPercentage * 100, "%")


#Calculating the number of defective kits supplied by Uzumaki Safety Suppliers
UzumakiFaultyKits = (UzumakiFaultyPercentage * UzumakiKitsSupplied)
#Calculating the number of defective kits supplied by Khairan Safety Company
KhairanFaultyKits = (KhairanFaultyPercentage * KhairanKitsSupplied)
#Displaying the number of defective kits from Uzumaki Safety Suppliers and Khairan Safety Company
print("The number of defective kits supplied by Uzumaki Safety Suppliers is: ", UzumakiFaultyKits,"\n",
      "The number of defective kits supplied by Khairan Safety Company is: ", KhairanFaultyKits)


#Calculating the probability of receiving a defective kit
ProbabilityFaultyKit = (UzumakiFaultyKits + KhairanFaultyKits)/(UzumakiKitsSupplied + KhairanKitsSupplied)
#Displaying the probability of receiving a defective kit
print("The probability of receiving a defective kit is: ", ProbabilityFaultyKit * 100, "%")


#Calculating the probability of a kit coming from Uzumaki Safety Suppliers given that its a defective kit using base theorem
ProbabilityUzumakiGivenDefective = (UzumakiFaultyPercentage * 0.75) / ProbabilityFaultyKit
#Displaying the probability of a kit coming from Uzumaki Safety Suppliers given that its a defective kit
print("The probability of a kit coming from Uzumaki Safety Suppliers given that its a defective kit is: ", ProbabilityUzumakiGivenDefective * 100, "%")


# Calculating the probability of a kit being defective given that it came from Uzumaki Safety Suppliers
ProbabilityDefectiveGivenUzumaki = (ProbabilityUzumakiGivenDefective * ProbabilityFaultyKit) / (UzumakiKitsSupplied / OverallKits)
#Displaying the probability of a kit being defective given that it came from Uzumaki Safety Supplierst
print("The probability of a kit being defective given that it came from Uzumaki Safety Suppliers is: ", ProbabilityDefectiveGivenUzumaki * 100, "%")
