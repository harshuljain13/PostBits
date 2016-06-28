#!/usr/bin/python
from fbpost import fbwallpost, grouppost
from config import perm_Acc_token_fb, PageName, usr_access_token
from firebasepy import FirebaseGet,FirebasePost,FirebasePut,FirebaseDelete

def main():

    MasterJson = FirebaseGet()
    """
    Check if Master json is present. This means whether there is any data to bbe processed or not.
    """
    if MasterJson:
        #assigning keys list to JSONKeys
        JSONKeys = MasterJson.keys()

        for JSONKey in JSONKeys:

            #get JSON for every key
            OneJSON = MasterJson[JSONKey]

            #get values in this JSON
            TextMessage = OneJSON['TextMessage']
            ImagePath = OneJSON['ImageURL']
            LinkPath = OneJSON['Link']
            Days = OneJSON['Days']
            Name = OneJSON['Name']

            #if any groups in selected then process else delete the JSON
            if 'Groups' in  OneJSON:
                GroupIds = OneJSON['Groups']
                #print TextMessage
                #print ImagePath
                #print LinkPath
                #print GroupIds
                #print Days
                #print Name

                #fbwallpost(perm_Acc_token_fb, PageName, TextMessage, ImagePath, LinkPath)

                """checking the Days. if 0 then delete the JSON else publish it."""
                if Days > 0:
                    grouppost(usr_access_token, GroupIds, TextMessage, ImagePath, LinkPath, Days,Name)
                    #decrement Days

                    #Days-=1
                    #OneJSON['Days'] = Days
                    #FirebasePut(OneJSON, JSONKey)
                if Days == 0:
                    FirebaseDelete(JSONKey)
            else:
                FirebaseDelete(JSONKey)

if __name__ == '__main__':
    main()