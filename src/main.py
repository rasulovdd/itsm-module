
import datetime
import json
import modules.itsm as itsm
import os
from dotenv import load_dotenv
from json import JSONDecodeError

load_dotenv()
QUEUE_MIN = os.getenv('QUEUE_MIN')
QUEUE_MAX = os.getenv('QUEUE_MAX')

def FileWrite(text):
    try:
        #Filetxt = open('text.txt', 'a') #добавляет в текст новый текст 
        Filetxt = open('text.txt', 'w') #записывает новый поверх старой
        #Filetxt.write(str(datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S")) + text)
        Filetxt.write(text)
        Filetxt.close()

    except BaseException as error:
        print('Ошибка Записи в файл :', error)

#получаем данные из ITSM

def main():
    try:
        my_queue_info = itsm.get_queues_full() #получаем инфо об очередях
        #my_queue_info = itsm.get_queues_full_debug() #debug
        #получаем городской номер из списка
        for key in my_queue_info:
            for item  in my_queue_info[key]["number_in_queue"]:
                #получаем статус городского номера
                num_status = itsm.get_number_info(item['title']) 
                item["status"] = num_status
        
        FileWrite(str(my_queue_info)) #записываем в файл
    except Exception as E:
        print(f"Ошибка: {E}")  # debug

#запускаем приложение 
main()