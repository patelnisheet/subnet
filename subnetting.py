from math import ceil, log
#1 ip address
ipAddress = input("Enter ip Address: ")


#2 separated in 4 parts => string and binary
firstPart, secondPart, thirdPart, fourthPart = ipAddress.split(".")
ipAddressFourParts = [int(firstPart), int(secondPart), int(thirdPart), int(fourthPart)]
binaryipAddressFourParts = list(map(lambda x: format(int(x),"08b") , ipAddressFourParts))

#3 Class of IP address
if int(firstPart) <= 127:
    addressRange = "A"
    subnetMaskInitialPart = format(255,"b") 
elif 128 <= int(firstPart) <= 191:
    addressRange = "B"
    subnetMaskInitialPart = format(255,"b") + format(255,"b")
elif 192 <= int(firstPart) <= 239:
    addressRange = "C"
    subnetMaskInitialPart = format(255,"b") + format(255,"b") + format(255,"b")
print("Address class: ",addressRange)

#4 Default subnet Mask
formation = str("0"+str(32-len(subnetMaskInitialPart))+"b")
tailingZeros = format(0,formation)
defaultSubnetMaskBinary = subnetMaskInitialPart + tailingZeros
defaultSubnetMaskWithDotsBinary = ''.join('.' * (n%8 == 0) + l for n, l in enumerate(defaultSubnetMaskBinary))
defaultSubnetMaskWithDotsBinary = defaultSubnetMaskWithDotsBinary[1:] #to remove . at start
defaultSubnetMaskWithDotsDecFourParts = list(map(lambda x: int(x,2) , defaultSubnetMaskWithDotsBinary.split(".")))
defaultSubnetMaskWithDotsDec = ".".join(str(x) for x in defaultSubnetMaskWithDotsDecFourParts)
print("Default subnet mask in Binary: ", defaultSubnetMaskWithDotsBinary)
print("Default subnet mask in  Decimal: ", defaultSubnetMaskWithDotsDec)


#5 Network Address
networkAddressFourParts = list(map(lambda x: x[0] & x[1] , list(zip(ipAddressFourParts, defaultSubnetMaskWithDotsDecFourParts))))
networkAddressDotDec = ".".join(str(x) for x in networkAddressFourParts)
print("Network Address in Decimal: ", networkAddressDotDec)
binarynetworkAddressFourParts = list(map(lambda x: format(int(x),"08b") , networkAddressFourParts))
networkAddressBin = "".join(str(x) for x in binarynetworkAddressFourParts)
networkAddressDotBin = ''.join('.' * (n%8 == 0) + l for n, l in enumerate(networkAddressBin))
networkAddressDotBin = networkAddressDotBin[1:]
print("Network Address in Binary: ", networkAddressDotBin)
networkAddressInitialPart = networkAddressBin[0:len(subnetMaskInitialPart)]


#6 custom subnet mask & host
choice = input("Which information do You have?\n1. CIDR\n2. No of subnets\n3. No of total subnets\n4. No of total hosts\n5. No of usable hosts\nYour choice should be 1, 2, 3, 4 or 5: ")
if choice == '1':
    CIDR = input("Enter CIDR value: ")
    CIDR = int(CIDR)
    subnetBitsCount = CIDR - len(subnetMaskInitialPart)
    hostsBitsCount =  32 - CIDR
elif choice == '2':
    subnetBitsCount = input("Enter subnet *Bits* you want: ")
    subnetBitsCount = int(subnetBitsCount)
    hostsBitsCount = 32 - subnetBitsCount - len(subnetMaskInitialPart)
elif choice == '3':
    totalSubnets = input("Enter total number of Subnets: ")
    totalSubnets = int(totalSubnets)
    subnetBitsCount = ceil(log(totalSubnets)/(log(2)))
    hostsBitsCount = 32 - subnetBitsCount - len(subnetMaskInitialPart)
elif choice == '4':
    totalHosts = input("Enter total number of Hosts: ")
    totalHosts = int(totalHosts)
    hostsBitsCount = ceil(log(totalHosts)/(log(2)))
    subnetBitsCount = 32 - hostsBitsCount - len(subnetMaskInitialPart)
elif choice == '5':
    usableHosts = input("Enter usableHosts value: ")
    usableHosts = int(usableHosts)
    usableHosts = usableHosts + 2
    hostsBitsCount = ceil(log(usableHosts)/(log(2)))
    subnetBitsCount = 32 - hostsBitsCount - len(subnetMaskInitialPart)
else:
    print("Please input correct choice from 1 to 4 only...")

numberOfSubnets = (2**subnetBitsCount) 
numberOfHosts = (2**hostsBitsCount) 

print("Number of Subnet bits: ", subnetBitsCount)
print("Total Number of subnets: ", numberOfSubnets)
print("Number of host bits: ", hostsBitsCount)
print("Total Number of Hosts: ", numberOfHosts)


#7 CUSTOM subnet
formation = str("0"+str(subnetBitsCount+len(subnetMaskInitialPart))+"b")
customSubnet = format(2**(int(subnetBitsCount+len(subnetMaskInitialPart)))-1, formation)
formation = str("0"+str(hostsBitsCount)+"b")
customSubnetTrailingZero = format(0,formation)
customSubnetMaskBinary = customSubnet + customSubnetTrailingZero
customSubnetMaskWithDotsBinary = ''.join('.' * (n%8 == 0) + l for n, l in enumerate(customSubnetMaskBinary))
customSubnetMaskWithDotsBinary = customSubnetMaskWithDotsBinary[1:] #to remove . at start
customSubnetMaskWithDotsDecFourParts = list(map(lambda x: int(x,2) , customSubnetMaskWithDotsBinary.split(".")))
customSubnetMaskWithDotsDec = ".".join(str(x) for x in customSubnetMaskWithDotsDecFourParts)
print("Custom subnet Mask in Binary: ", customSubnetMaskWithDotsBinary)
print("Custom subnet Mask in Decimal: ", customSubnetMaskWithDotsDec)

def my_function(initialPart):
    formation = str("0"+str(subnetBitsCount)+"b")
    subnetAddressBits = format(subnetNumber-1, formation)
    if len(subnetAddressBits) > subnetBitsCount:
        print("You cannot borrow more bits than available")

    formation = str("0"+str(hostsBitsCount)+"b")
    networkAddressHostBits = format(0, formation)


    networkAddressHostSubnet = subnetAddressBits + networkAddressHostBits
    networkAddress = initialPart + networkAddressHostSubnet
    networkAddressWithDotsBinary = ''.join('.' * (n%8 == 0) + l for n, l in enumerate(networkAddress))
    networkAddressWithDotsBinary = networkAddressWithDotsBinary[1:] #to remove . at start
    networkAddressWithDotsDecFourParts = list(map(lambda x: int(x,2) , networkAddressWithDotsBinary.split(".")))
    networkAddressWithDotsDec = ".".join(str(x) for x in networkAddressWithDotsDecFourParts)

    broadcastAddressHostBits = format(2**(int(hostsBitsCount))-1, formation)
    broadcastAddressHostSubnet = subnetAddressBits + broadcastAddressHostBits
    broadcastAddress = initialPart + broadcastAddressHostSubnet
    broadcastAddressWithDotsBinary = ''.join('.' * (n%8 == 0) + l for n, l in enumerate(broadcastAddress))
    broadcastAddressWithDotsBinary = broadcastAddressWithDotsBinary[1:] #to remove . at start
    broadcastAddressWithDotsDecFourParts = list(map(lambda x: int(x,2) , broadcastAddressWithDotsBinary.split(".")))
    broadcastAddressWithDotsDec = ".".join(str(x) for x in broadcastAddressWithDotsDecFourParts)
    print(networkAddressWithDotsDec ," to ", broadcastAddressWithDotsDec)
    print("In binary: ", networkAddressWithDotsBinary," to ", broadcastAddressWithDotsBinary)


#8 Need information specific subnet
while(True):
    subnetNumber = int(input("Enter subnet's number you want: "))
    formation = str("0"+str(subnetBitsCount)+"b")
    subnetAddressBits = format(subnetNumber-1, formation)
    if len(subnetAddressBits) > subnetBitsCount:
        print("You cannot borrow more bits than available")
        continue
    print("You required of: ",subnetNumber)
    
    print("-"*80)
    print("Network Range: ", end="")
    my_function(networkAddressInitialPart)
    print("-"*80)
    print("Subnet Range: ", end="")
    my_function(subnetMaskInitialPart)


