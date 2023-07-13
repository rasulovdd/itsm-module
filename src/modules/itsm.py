
import requests
import os
from mysql.connector import MySQLConnection, Error  # Добавляем функцию MySQLConnection
from dotenv import load_dotenv
import json
from json import JSONDecodeError

load_dotenv()
ACCESS_KEY = os.getenv('ACCESS_KEY')
SERVER_ADDRESS = os.getenv('SERVER_ADDRESS')
QUEUE_MIN = int(os.getenv('QUEUE_MIN'))
QUEUE_MAX = int(os.getenv('QUEUE_MAX'))

queues_dict = {}

def get_queues_nomer():
    """ Получение номера очередей из ITSM """
    # param = {
    #     "name" : ''
    # }
    my_request = f"{SERVER_ADDRESS}services/rest/find/objectBase$Queues/?accessKey={ACCESS_KEY}"
    respons = requests.get(my_request)
    #print (my_request) #debug
    my_data = respons.json()
    nomer = []
    for i in my_data:  # Ищем в результатах
        if int(i['nomer']) > QUEUE_MIN and int(i['nomer']) < QUEUE_MAX:
            nomer.append(i['nomer'])
    
    return nomer # Возвращаем рузультаты

def get_queues_title(nomer):
    """ Получение названия очередей из ITSM """
    param = {
        "nomer" : nomer
    }
    my_request = f"{SERVER_ADDRESS}services/rest/find/objectBase$Queues/{param}?accessKey={ACCESS_KEY}"
    respons = requests.get(my_request)
    print (my_request) #debug
    #respons = my_data.json()
    my_data = respons.json()
    title = []
    for i in my_data:  # Ищем в результатах
        #if int(i['nomer']) > i_min and int(i['nomer']) < i_max:
        #    nomer.append(i['nomer'])
        title.append(i['DepOwner']['title'])
    
    return title # Возвращаем рузультаты

def get_queues_full_debug():
    """ Получение всю информацию об очереде из ITSM """
    my_request = f"{SERVER_ADDRESS}services/rest/find/objectBase$Queues/?accessKey={ACCESS_KEY}"
    respons = requests.get(my_request)
    print (my_request) #debug
    #respons = my_data.json()
    my_data = respons.json()
    #print (my_data) 
    #return respons # Возвращаем рузультаты

def get_queues_full():
    """ Получение всю информацию об очереде из ITSM """
    my_request = f"{SERVER_ADDRESS}services/rest/find/objectBase$Queues/?accessKey={ACCESS_KEY}"
    respons = requests.get(my_request)
    # исходный JSON-объект
    source_json = respons.json()
    #nomera = ""
    for i in source_json:  # Ищем в результатах
        if int(i['nomer']) > QUEUE_MIN and int(i['nomer']) < QUEUE_MAX:
            queues_dict[i['nomer']] = {
                    'queue' : i['nomer'],
                    'title' : i['DepOwner']['title'],
                    'pull_ext' : i['PullExt'],
                    'status' : i['state']
            }
            #nomera = i['childBO']
            queues_dict[i['nomer']]['number_in_queue'] = i['childBO']
            #print (i) #debug
        
    return queues_dict # Возвращаем рузультаты


def get_number_info(number):
    """ Получение всю информацию о номере из ITSM """
    param = {
        'title' : number
    }
    my_request = f"{SERVER_ADDRESS}services/rest/find/objectBase$Citynumber/{param}?accessKey={ACCESS_KEY}"
    respons = requests.get(my_request)
    #print (my_request) #debug
    #respons = my_data.json()
    my_data = respons.json()
    #print (my_data) 
    for i in my_data:  # Ищем в результатах
        status = i['state']
    return status # Возвращаем рузультат