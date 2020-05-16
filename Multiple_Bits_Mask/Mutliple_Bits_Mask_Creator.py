print("Hello Player, Welcome to the Multiple Bits Mask Creator Program\n")

REG_NAME                = input("\nPlease Enter your REGISTER Name: ")
MASK_NAME               = input("\nPlease Enter your MASK Name: ")
NO_OF_BITS_str          = input("\nPlease Enter your number of Bits: ")

print("\n")

NO_OF_BITS          = int(NO_OF_BITS_str)

Mask = 0

for i in range(1,NO_OF_BITS+1):
  Bits_Pos     = input("Please Enter your " + str(i) + " Bit position: ")
  Bits_Pos_int = int(Bits_Pos)
  Mask         = Mask | (1 << Bits_Pos_int)

#Creating File of the Masks
file = open( str(REG_NAME) + "_Defines.h",'w')


file.write("#define " + REG_NAME + "_" + MASK_NAME  + "_MASK"  + "\t\t (0x"+  format( (Mask) , '08X' )                     +") \n")
file.write("#define " + REG_NAME + "_" + MASK_NAME  + "_CLEAR" + "\t\t (0x"+  format( (~(Mask) + 1 + 0xFFFFFFFF) , '08X' ) +") \n")


file.close()