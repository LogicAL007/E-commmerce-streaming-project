from kafka import KafkaConsumer
import logging

consumer = KafkaConsumer()

def kafka_python_consumer():
    consumer = KafkaConsumer('ingestion-topic', group_id='mypythonconsumer',bootstrap_servers='localhost:9092',)
    for msg in consumer:
      logging.info(msg)

if __name__ =='__main__':
   print("start consuming")
   kafka_python_consumer()
   print("done")