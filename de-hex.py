#*******************************************************************
#* Author = Adam Burnett (@infosecEagle / alburnett@gmail.com)     *
#* simple quick script for turning hex into human readable text    *
#*                                                                 *
#*                                                                 *
#* use python3 ./de-hex.py                                         *
#*******************************************************************

hex_Input = input("drop Hex here ")
print(bytes.fromhex(hex_Input).decode('utf-8'))

#*******************************************************************
# To-Do:                                                           *
# 1) Chose decoding; ie: ASCII, UTF,... Maybe both?                *
#                                                                  *
#*******************************************************************
