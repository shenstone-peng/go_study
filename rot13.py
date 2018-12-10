import string
from codecs import encode as _dont_use_this_

def rot13(message):
    ans = []
    print message
    #if i.isalpha() == True:
    for i in message:
        if i.isalpha() == True:
            num = ord(i)
            print num
            ss = num +13
            if( num >= 65 and  num <=90):
                if ss > 90:
                    ss = ss- 90 +64
                    print 'ss>90'
                    i = chr(ss)
                    ans.append(i)
                else:
                
                     i = chr(ss)
                     ans.append(i)
            else:
                if ss > 122:
                    ss = ss -122 +96
                
                    ans.append(chr(ss))
                else:
                    ans.append(chr(ss))
        else:
            ans.append(i)
    ans = ''.join(ans)
    return ans
