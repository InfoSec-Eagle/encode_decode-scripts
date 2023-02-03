#*******************************************************************
#* Author = Adam Burnett (@infosecEagle / alburnett@gmail.com)     *
#* simple quick script for turning human readable text into Base64 *
#*                                                                 *
#*                                                                 *
#*                                                                 *
#*******************************************************************

import base64

plain = input("drop plain text here ")
plain_string = plain.encode("ascii")

base64_bytes = base64.b64encode(plain_string)
base64_string = base64_bytes.decode("ascii")

print(base64_string)
