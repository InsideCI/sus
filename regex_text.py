# import re
# text = "portal.jsf?id=1626785&amp;lc=pt_BR"
 
# match = re.search("portal.jsf?id=(.+?)&amp;lc=pt_BR", text,flags=re.IGNORECASE)
 
# try:
#     result = match.group(1)
# except:
#     result = "no match found"
 
# print(result)

import re
text = "id=1626785&amp"
 
match = re.search("id=(.+?)&amp", text,flags=re.IGNORECASE)
 
try:
    result = match.group(1)
except:
    result = "no match found"
 
print(result)