#!/usr/bin/env python
from fbpost import fbwallpost, grouppost
from config import perm_Acc_token_fb, PageName, usr_access_token
from firebasepy import FirebaseGet,FirebasePost

def main():
    """
    #GroupId = '1687433408198647'
    GroupIds = ['1066160280093643']
    """
    MasterJson = FirebaseGet()
    JSONKeys = MasterJson.keys()
    for JSONKey in JSONKeys:
        OneJSON = MasterJson[JSONKey]
        TextMessage = OneJSON['TextMessage']
        ImagePath = OneJSON['ImagePath']
        LinkPath = OneJSON['LinkPath']
        GroupIds = OneJSON['GroupIds']
        print TextMessage
        print ImagePath
        print LinkPath
        print GroupIds

        fbwallpost(perm_Acc_token_fb, PageName, TextMessage, ImagePath, LinkPath)
        grouppost(usr_access_token, GroupIds, TextMessage, ImagePath, LinkPath)

if __name__ == '__main__':
    main()