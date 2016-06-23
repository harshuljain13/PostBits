from fbpost import fbwallpost, sharefb, grouppost
from config import perm_Acc_token_fb, PageName, usr_access_token

def main():
    TextMessage = 'You can never be too old to have balloons at your birthday party!' \
                  'Hire the best balloon decorators in Delhi-Ncr and have the craziest birthday party.'

    ImagePath = 'https://fbcdn-photos-c-a.akamaihd.net/hphotos-ak-xla1/v/t1.0-0/p480x480/13233083_928046943971926_2544' \
                '900988046449714_n.jpg?oh=12d928cb49ef28b1efdfde8559ba9d4b&oe=57C1244C&__gda__=1472611472_281d37b8ac' \
                '37a32fb70f7b6771a24cbc'

    LinkPath = 'https://www.quotemykaam.com/#!service/balloon-decorators'

    GroupId = '1687433408198647'

    x = fbwallpost(perm_Acc_token_fb, PageName, TextMessage, ImagePath, LinkPath)
    print x

    return_code = grouppost(usr_access_token,GroupId , TextMessage, ImagePath, LinkPath)
    print return_code

if __name__ == '__main__':
    main()