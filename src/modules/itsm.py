
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
            #print (i['nomer']) #debug
    
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
    #return my_data # Возвращаем рузультаты

def get_queues_full():
    """ Получение всю информацию об очереде из ITSM """
    my_request = f"{SERVER_ADDRESS}services/rest/find/objectBase$Queues/?accessKey={ACCESS_KEY}"
    respons = requests.get(my_request)
    # исходный JSON-объект
    source_json = respons.json()
    #nomera = ""
    default_value = "Нет владельца"
    default_status = "Нет статуса"
    for i in source_json:  # Ищем в результатах
        if int(i['nomer']) > QUEUE_MIN and int(i['nomer']) < QUEUE_MAX or int(i['nomer']) == int("0001"):
            #print (i['nomer']) #debug
            num_title = i['DepOwner']['title'] if i['DepOwner'] is not None else default_value
            #print (num_title) #debug
            num_status = i['state'] if i['state'] is not None else default_status
            #print (num_status) #debug
            queues_dict[i['nomer']] = {
                    'queue' : i['nomer'],
                    'title' : num_title,
                    'pull_ext' : i['PullExt'],
                    'status' : num_status
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
    status =""
    for i in my_data:  # Ищем в результатах
        status = i['state']
    return status # Возвращаем рузультат