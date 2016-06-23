__author__ = 'h_hack'


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import facebook
import requests

def fbwallpost(PageAccessToken, PageName, TextMessage, ImagePath, LinkPath):
    perm_access_token= PageAccessToken
    page_name = PageName

    graph = facebook.GraphAPI(access_token=perm_access_token, version='2.2')

    attachment = {
        'name': 'Quotemykaam',
        'link': LinkPath,
        'picture': ImagePath
    }
    x = graph.put_wall_post( message=TextMessage, attachment= attachment)
    return x

def grouppost(UserAccessToken, GroupId, TextMessage, ImagePath, LinkPath):

    x = requests.post('https://graph.facebook.com/v2.6/'+GroupId+'/feed',
                      params= {'access_token': UserAccessToken, 'message': TextMessage,
                                'picture': ImagePath,
                                'link': LinkPath})

    #x = requests.post('https://graph.facebook.com/v2.6/1687433408198647/feed', params= {'access_token': UserAccessToken,
    #                                                                              'message': msg})

    return x



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






