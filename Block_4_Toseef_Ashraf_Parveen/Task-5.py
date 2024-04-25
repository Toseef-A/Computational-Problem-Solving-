#overall number of kits supplied
OverallKits = 2000
#Number of kits supplied by Uzumaki Safety Suppliers
UzumakiKitsSupplied = OverallKits * 0.5
#Number of kits supplied by Khairan Safety Company
KhairanKitsSupplied = OverallKits * 0.2
#Number of kits supplied by Leaf Firt-Aid Kits Ltd
LeafKitsSupplied = OverallKits * 0.3


#Percentage given of defective kits supplied by Uzumaki Safety Suppliers (20% = 0.2)
UzumakiFaultyPercentage = 0.2
#Percentage given of defective kits supplied by Khairan Safety Company (10% = 0.1)
KhairanFaultyPercentage = 0.1
#Assuming Percentage given of defective kits supplied by Leaf Firt-Aid Kits Ltd (10% = 0.1)
LeafFaultyPercentage = 0.1


#Calculating the number of defective kits supplied by Uzumaki Safety Suppliers
UzumakiFaultyKits = (UzumakiFaultyPercentage * UzumakiKitsSupplied)
#Calculating the number of defective kits supplied by Khairan Safety Company
KhairanFaultyKits = (KhairanFaultyPercentage * KhairanKitsSupplied)
#Calculating the number of defective kits supplied by Leaf Firt-Aid Kits Ltd
LeafFaultyKits = (LeafFaultyPercentage * LeafKitsSupplied)
#Displaying the number of defective kits from Uzumaki Safety Suppliers, Khairan Safety Company and Leaf Firt-Aid Kits Ltd
print("The number of defective kits from Uzumaki Safety Suppliers is", UzumakiFaultyKits, "\n",
      "The number of defective kits from Khairan Safety Company is", KhairanFaultyKits, "\n",
      "The number of defective kits from Leaf Fisrt-Aid Kits Ltd is", LeafFaultyKits)


#Calculating the probability of receiving a defective kit
ProbabilityFaultyKit = (UzumakiFaultyKits + KhairanFaultyKits + LeafFaultyKits)/(UzumakiKitsSupplied + KhairanKitsSupplied + LeafKitsSupplied)
#Displaying the probability of receiving a defective kit
print("The probability of receiving a defective kit is", ProbabilityFaultyKit * 100, "%")


#Calculating the probability of a kit coming from Uzumaki Safety Suppliers given that its a defective kit using base theorem
ProbabilityUzumakiGivenDefective = UzumakiFaultyPercentage * 0.5 / ProbabilityFaultyKit
#Displaying the probability of a kit coming from Uzumaki Safety Suppliers given that its a defective kit
print("The probability of a kit coming from Uzumaki Safety Suppliers given that its a defective kit is", ProbabilityUzumakiGivenDefective * 100, "%")