print("Hello Player, Welcome to the Mask Creator Program\n")

REG_NAME   = input("Please Enter your REGISTER Name: ")

Bit_0  = input("\nPlease Enter  0 Bit Name: ")
Bit_1  = input("\nPlease Enter  1 Bit Name: ")
Bit_2  = input("\nPlease Enter  2 Bit Name: ")
Bit_3  = input("\nPlease Enter  3 Bit Name: ")
Bit_4  = input("\nPlease Enter  4 Bit Name: ")
Bit_5  = input("\nPlease Enter  5 Bit Name: ")
Bit_6  = input("\nPlease Enter  6 Bit Name: ")
Bit_7  = input("\nPlease Enter  7 Bit Name: ")
Bit_8  = input("\nPlease Enter  8 Bit Name: ")
Bit_9  = input("\nPlease Enter  9 Bit Name: ")
Bit_10 = input("\nPlease Enter 10 Bit Name: ")
Bit_11 = input("\nPlease Enter 11 Bit Name: ")
Bit_12 = input("\nPlease Enter 12 Bit Name: ")
Bit_13 = input("\nPlease Enter 13 Bit Name: ")
Bit_14 = input("\nPlease Enter 14 Bit Name: ")
Bit_15 = input("\nPlease Enter 15 Bit Name: ")
Bit_16 = input("\nPlease Enter 16 Bit Name: ")
Bit_17 = input("\nPlease Enter 17 Bit Name: ")
Bit_18 = input("\nPlease Enter 18 Bit Name: ")
Bit_19 = input("\nPlease Enter 19 Bit Name: ")
Bit_20 = input("\nPlease Enter 20 Bit Name: ")
Bit_21 = input("\nPlease Enter 21 Bit Name: ")
Bit_22 = input("\nPlease Enter 22 Bit Name: ")
Bit_23 = input("\nPlease Enter 23 Bit Name: ")
Bit_24 = input("\nPlease Enter 24 Bit Name: ")
Bit_25 = input("\nPlease Enter 25 Bit Name: ")
Bit_26 = input("\nPlease Enter 26 Bit Name: ")
Bit_27 = input("\nPlease Enter 27 Bit Name: ")
Bit_28 = input("\nPlease Enter 28 Bit Name: ")
Bit_29 = input("\nPlease Enter 29 Bit Name: ")
Bit_30 = input("\nPlease Enter 30 Bit Name: ")
Bit_31 = input("\nPlease Enter 31 Bit Name: ")

#Creating File of the Masks
file = open( str(REG_NAME) + "_Defines.h",'w')

file.write("#define " + REG_NAME + "_" + Bit_0  + "_MASK"  + "\t\t (0x00000001) \n")
file.write("#define " + REG_NAME + "_" + Bit_0  + "_CLEAR" + "\t\t (0xFFFFFFFE) \n")
file.write("#define " + REG_NAME + "_" + Bit_1  + "_MASK"  + "\t\t (0x00000002) \n")
file.write("#define " + REG_NAME + "_" + Bit_1  + "_CLEAR" + "\t\t (0xFFFFFFFD) \n")
file.write("#define " + REG_NAME + "_" + Bit_2  + "_MASK"  + "\t\t (0x00000004) \n")
file.write("#define " + REG_NAME + "_" + Bit_2  + "_CLEAR" + "\t\t (0xFFFFFFFB) \n")
file.write("#define " + REG_NAME + "_" + Bit_3  + "_MASK"  + "\t\t (0x00000008) \n")
file.write("#define " + REG_NAME + "_" + Bit_3  + "_CLEAR" + "\t\t (0xFFFFFFF7) \n")
file.write("#define " + REG_NAME + "_" + Bit_4  + "_MASK"  + "\t\t (0x00000010) \n")
file.write("#define " + REG_NAME + "_" + Bit_4  + "_CLEAR" + "\t\t (0xFFFFFFEF) \n")
file.write("#define " + REG_NAME + "_" + Bit_5  + "_MASK"  + "\t\t (0x00000020) \n")
file.write("#define " + REG_NAME + "_" + Bit_5  + "_CLEAR" + "\t\t (0xFFFFFFDF) \n")
file.write("#define " + REG_NAME + "_" + Bit_6  + "_MASK"  + "\t\t (0x00000040) \n")
file.write("#define " + REG_NAME + "_" + Bit_6  + "_CLEAR" + "\t\t (0xFFFFFFBF) \n")
file.write("#define " + REG_NAME + "_" + Bit_7  + "_MASK"  + "\t\t (0x00000080) \n")
file.write("#define " + REG_NAME + "_" + Bit_7  + "_CLEAR" + "\t\t (0xFFFFFF7F) \n")
file.write("#define " + REG_NAME + "_" + Bit_8  + "_MASK"  + "\t\t (0x00000100) \n")
file.write("#define " + REG_NAME + "_" + Bit_8  + "_CLEAR" + "\t\t (0xFFFFFEFF) \n")
file.write("#define " + REG_NAME + "_" + Bit_9  + "_MASK"  + "\t\t (0x00000200) \n")
file.write("#define " + REG_NAME + "_" + Bit_9  + "_CLEAR" + "\t\t (0xFFFFFDFF) \n")
file.write("#define " + REG_NAME + "_" + Bit_10 + "_MASK"  + "\t\t (0x00000400) \n")
file.write("#define " + REG_NAME + "_" + Bit_10 + "_CLEAR" + "\t\t (0xFFFFFBFF) \n")
file.write("#define " + REG_NAME + "_" + Bit_11 + "_MASK"  + "\t\t (0x00000800) \n")
file.write("#define " + REG_NAME + "_" + Bit_11 + "_CLEAR" + "\t\t (0xFFFFF7FF) \n")
file.write("#define " + REG_NAME + "_" + Bit_12 + "_MASK"  + "\t\t (0x00001000) \n")
file.write("#define " + REG_NAME + "_" + Bit_12 + "_CLEAR" + "\t\t (0xFFFFEFFF) \n")
file.write("#define " + REG_NAME + "_" + Bit_13 + "_MASK"  + "\t\t (0x00002000) \n")
file.write("#define " + REG_NAME + "_" + Bit_13 + "_CLEAR" + "\t\t (0xFFFFDFFF) \n")
file.write("#define " + REG_NAME + "_" + Bit_14 + "_MASK"  + "\t\t (0x00004000) \n")
file.write("#define " + REG_NAME + "_" + Bit_14 + "_CLEAR" + "\t\t (0xFFFFBFFF) \n")
file.write("#define " + REG_NAME + "_" + Bit_15 + "_MASK"  + "\t\t (0x00008000) \n")
file.write("#define " + REG_NAME + "_" + Bit_15 + "_CLEAR" + "\t\t (0xFFFF7FFF) \n")
file.write("#define " + REG_NAME + "_" + Bit_16 + "_MASK"  + "\t\t (0x00010000) \n")
file.write("#define " + REG_NAME + "_" + Bit_16 + "_CLEAR" + "\t\t (0xFFFEFFFF) \n")
file.write("#define " + REG_NAME + "_" + Bit_17 + "_MASK"  + "\t\t (0x00020000) \n")
file.write("#define " + REG_NAME + "_" + Bit_17 + "_CLEAR" + "\t\t (0xFFFDFFFF) \n")
file.write("#define " + REG_NAME + "_" + Bit_18 + "_MASK"  + "\t\t (0x00040000) \n")
file.write("#define " + REG_NAME + "_" + Bit_18 + "_CLEAR" + "\t\t (0xFFFBFFFF) \n")
file.write("#define " + REG_NAME + "_" + Bit_19 + "_MASK"  + "\t\t (0x00080000) \n")
file.write("#define " + REG_NAME + "_" + Bit_19 + "_CLEAR" + "\t\t (0xFFF7FFFF) \n")
file.write("#define " + REG_NAME + "_" + Bit_20 + "_MASK"  + "\t\t (0x00100000) \n")
file.write("#define " + REG_NAME + "_" + Bit_20 + "_CLEAR" + "\t\t (0xFFEFFFFF) \n")
file.write("#define " + REG_NAME + "_" + Bit_21 + "_MASK"  + "\t\t (0x00200000) \n")
file.write("#define " + REG_NAME + "_" + Bit_21 + "_CLEAR" + "\t\t (0xFFDFFFFF) \n")
file.write("#define " + REG_NAME + "_" + Bit_22 + "_MASK"  + "\t\t (0x00400000) \n")
file.write("#define " + REG_NAME + "_" + Bit_22 + "_CLEAR" + "\t\t (0xFFBFFFFF) \n")
file.write("#define " + REG_NAME + "_" + Bit_23 + "_MASK"  + "\t\t (0x00800000) \n")
file.write("#define " + REG_NAME + "_" + Bit_23 + "_CLEAR" + "\t\t (0xFF7FFFFF) \n")
file.write("#define " + REG_NAME + "_" + Bit_24 + "_MASK"  + "\t\t (0x01000000) \n")
file.write("#define " + REG_NAME + "_" + Bit_24 + "_CLEAR" + "\t\t (0xFEFFFFFF) \n")
file.write("#define " + REG_NAME + "_" + Bit_25 + "_MASK"  + "\t\t (0x02000000) \n")
file.write("#define " + REG_NAME + "_" + Bit_25 + "_CLEAR" + "\t\t (0xFDFFFFFF) \n")
file.write("#define " + REG_NAME + "_" + Bit_26 + "_MASK"  + "\t\t (0x04000000) \n")
file.write("#define " + REG_NAME + "_" + Bit_26 + "_CLEAR" + "\t\t (0xFBFFFFFF) \n")
file.write("#define " + REG_NAME + "_" + Bit_27 + "_MASK"  + "\t\t (0x08000000) \n")
file.write("#define " + REG_NAME + "_" + Bit_27 + "_CLEAR" + "\t\t (0xF7FFFFFF) \n")
file.write("#define " + REG_NAME + "_" + Bit_28 + "_MASK"  + "\t\t (0x10000000) \n")
file.write("#define " + REG_NAME + "_" + Bit_28 + "_CLEAR" + "\t\t (0xEFFFFFFF) \n")
file.write("#define " + REG_NAME + "_" + Bit_29 + "_MASK"  + "\t\t (0x20000000) \n")
file.write("#define " + REG_NAME + "_" + Bit_29 + "_CLEAR" + "\t\t (0xDFFFFFFF) \n")
file.write("#define " + REG_NAME + "_" + Bit_30 + "_MASK"  + "\t\t (0x40000000) \n")
file.write("#define " + REG_NAME + "_" + Bit_30 + "_CLEAR" + "\t\t (0xBFFFFFFF) \n")
file.write("#define " + REG_NAME + "_" + Bit_31 + "_MASK"  + "\t\t (0x80000000) \n")
file.write("#define " + REG_NAME + "_" + Bit_31 + "_CLEAR" + "\t\t (0x7FFFFFFF) \n")

file.close()