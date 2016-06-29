__author__ = 'h_hack'

import facebook
import requests

def fbwallpost(PageAccessToken, PageName, TextMessage, ImagePath, LinkPath):
    perm_access_token= PageAccessToken
    page_name = PageName

    graph = facebook.GraphAPI(access_token=perm_access_token, version='2.2')

    attachment = {
        'link': LinkPath,
        'picture': ImagePath
    }
    PostId = graph.put_wall_post( message=TextMessage, attachment= attachment)
    print PostId


def grouppost(UserAccessToken, GroupIds, TextMessage, ImagePath, LinkPath,Days, Name):

    for GroupId in GroupIds:
        x = requests.post('https://graph.facebook.com/v2.6/'+GroupId+'/feed',
                      params= {'access_token': UserAccessToken, 'message': TextMessage,
                                'picture': ImagePath,
                                'link': LinkPath,
                               'name': Name})
        print Name + ' ' + GroupId + ' ' + str(x) + ' will run ' + str(Days) + ' more days'


"""
def sharefb(myusername, mypassword, PostId, FilePath):
    driver = webdriver.Firefox()
    driver.get('https://www.facebook.com/')
    EmailId = driver.find_element_by_id('email')
    EmailId.clear()
    EmailId.send_keys(myusername)
    PassWord = driver.find_element_by_id('pass')
    PassWord.clear()
    PassWord.send_keys(mypassword)
    LoginButton = driver.find_element_by_id('loginbutton')
    LoginButton.send_keys(Keys.RETURN)

    driver.find_element_by_class_name('_1mf').send_keys('hello')


    input_file = driver.find_element_by_xpath("//input[@type='file']")
    input_file.send_keys('/home/h_hack/work/PostBits/src/222.jpg/')
    """






