#!/usr/bin/env python
# coding: utf-8

# In[1]:


import string
w=list(string.ascii_lowercase)
dic={}
for i in range (len(w)):
    dic[w[i]]=i
class vignere:
    """This is for the vignere cipher, can be used to encode, decode and find key if you know the probable answer"""
    def Encode(Decoded,Key):
        Decoded=Decoded.lower()
        Key=Key.lower()
        l=[]
        ans=""
        i=j=0
        while len(Decoded)>len(Key):
            Key+=Key
        Key=Key[0:len(Decoded)]
        while i<len(Decoded) and j<len(Decoded):
            if Decoded[i]==" ":
                ans+=" "
                j=j-1

            else:
                Dnumber=dic[str(Decoded[i])]
                Knumber=dic[str(Key[j])]
                Enumber=Dnumber+Knumber
                if Enumber>25:
                    Enumber-=26
                ans+=list(dic.keys())[list(dic.values()).index(Enumber)]
            j+=1
            i+=1
        return ans
    def keyfinder(Decoded,Encoded):
        i=j=0
        Decoded=Decoded.lower()
        Encoded=Encoded.lower()
        ans=""
        for i in range (len(Decoded)):
            if Decoded[i]==" ":
                pass
            else:
                Dnumber=dic[str(Decoded[i])]
                Enumber=dic[str(Encoded[i])]
                Knumber=-Dnumber+Enumber
                if Knumber>25:
                    Knumber-=26
                elif Knumber<0:
                    Knumber+=26
                ans+=list(dic.keys())[list(dic.values()).index(Knumber)]
        return ans
    def decode(Encoded,Key):
        Encoded=Encoded.lower()
        Key=Key.lower()
        l=[]
        ans=""
        i=j=0
        while len(Encoded)>len(Key):
            Key+=Key
        Key=Key[0:len(Encoded)]
        while i<len(Encoded) and j<len(Encoded):
            if Encoded[i]==" ":
                ans+=" "
                j=j-1

            else:
                Enumber=dic[str(Encoded[i])]
                Knumber=dic[str(Key[j])]
                Dnumber=Enumber-Knumber
                if Dnumber>25:
                    Dnumber-=26
                elif Dnumber<0:
                    Dnumber+=26
                ans+=list(dic.keys())[list(dic.values()).index(Dnumber)]
            j+=1
            i+=1
        return ans

