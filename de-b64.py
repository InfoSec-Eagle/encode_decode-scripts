#*******************************************************************
#* Author = Adam Burnett (@infosecEagle / alburnett@gmail.com)     *
#* simple quick script for turning Base64 into human readable text *
#* v.2 (adding file CLI input& output)                             *
#*                                                                 *
#*                                                                 *
#*******************************************************************

import base64
import sys

#current work in progress
b64 = open(sys.argv[0])

decodedBytes = base64.b64decode(b64)
decodedStr = str(decodedBytes, "UTF-8")

print(decodedStr)
