import json

from TimeanddateScrapper.worldweather import Weather
from json import dumps, loads
from kafka import KafkaProducer, KafkaConsumer
from pymongo import MongoClient


class Stream:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.mongotable = self.client.mydb.scrapstream
        self.topic_name = 'scrapstream'
        self.producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                                      value_serializer=lambda x: dumps(x).encode('utf-8'))
        self.consumer = KafkaConsumer(
            self.topic_name,
            bootstrap_servers=['localhost:9092'],
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='group',
            value_deserializer=lambda x: loads(x.decode('utf-8')))

    def data_stream(self):
        weather = Weather()
        report = weather.worldWideReport()
        size = len(report)
        timestamp = report[0][3]
        for data in report:
            self.producer.send(self.topic_name, data)
        itr = 0
        listofvalues = []
        for data in self.consumer:
            if itr == size:
                break
            itr+=1
            print(data.value)

            document = {
                "Country": data.value[0],
                "City": data.value[1],
                "Temparature": data.value[2],
                "TimeStamp": data.value[3]
            }
            listofvalues.append(document)
        rec = self.mongotable.insert_many(listofvalues)
        return {"Result":"Data Pushed Successfully"}


    def show_data(self):
        listofvalues = []
        for data in self.mongotable.find({},{'_id': 0, 'Country': 1,
                 'City': 1, 'Temparature': 1,'TimeStamp':1}):
            listofvalues.append(data)
            #print(data)
        return json.dumps(listofvalues)


