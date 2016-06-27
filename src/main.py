#!/usr/bin/env python
from fbpost import fbwallpost, grouppost
from config import perm_Acc_token_fb, PageName, usr_access_token
from firebasepy import FirebaseGet,FirebasePost,FirebasePut

def main():

    MasterJson = FirebaseGet()
    JSONKeys = MasterJson.keys()
    for JSONKey in JSONKeys:
        OneJSON = MasterJson[JSONKey]
        TextMessage = OneJSON['TextMessage']
        ImagePath = OneJSON['ImageURL']
        LinkPath = OneJSON['Link']
        GroupIds = OneJSON['Groups']
        Days = OneJSON['Days']
        Name = OneJSON['Name']
        #print TextMessage
        #print ImagePath
        #print LinkPath
        #print GroupIds
        #print Days
        #print Name

        #fbwallpost(perm_Acc_token_fb, PageName, TextMessage, ImagePath, LinkPath)
        if Days>0:
            grouppost(usr_access_token, GroupIds, TextMessage, ImagePath, LinkPath, Days,Name)
            #decrement Days
            Days-=1
            OneJSON['Days'] = Days
            FirebasePut(OneJSON, JSONKey)

if __name__ == '__main__':
    main()