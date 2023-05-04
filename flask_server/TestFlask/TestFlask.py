from pickle import FALSE
import flask
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service 



app = flask.Flask(__name__)

#to display the connection status
@app.route('/', methods=['GET'])
def handle_call():
    return "Successfully Connected"

#the get method. when we call this, it just return the text "Hey!! I'm the fact you got!!!"
@app.route('/getfact', methods=['GET'])
def get_fact():
    return "Poti introduce alta cautare"

#the post method. when we call this with a string containing a name, it will return the name with the text "I got your name"
@app.route('/getname/<name>', methods=['POST'])
def extract_name(name):
    driver = webdriver.Chrome(executable_path="C:\\Users\\Laptop\\Desktop\\concurs\\chromedriver.exe")
    driver.implicitly_wait(5)
    search_terms = name.split(" ")
    links = []
    for term in search_terms:
        # Open YouTube page for search 
        driver.get('https://www.youtube.com/search?q={}'.format(term))
        # Find a first webelement with video thumbnail on the page
        link_webelement = driver.find_element(By.CSS_SELECTOR, 'div#contents ytd-item-section-renderer>div#contents a#thumbnail')
        # grab first href element
        links += [link_webelement.get_attribute('href')]
    return links

#this commands the script to run in the given port
if __name__ == '__main__':
    app.run(host="192.168.149.90", port=8000, debug=FALSE)