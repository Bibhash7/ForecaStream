# ForecaStream
ForecaStream is a powerful weather data pipeline application based on Flask-based REST API that leverages the TimeanddateScrapper Python package(Developed by me) to extract real-time weather information from timeanddate.com. This application employs Apache Kafka for efficient data streaming and MongoDB for robust data storage.

## About the scrapper (Created by me):

It is live on: https://pypi.org/project/TimeanddateScrapper/
      pip install TimeanddateScrapper

## Key Features:

1. TimeanddateScrapper Integration: Utilize the TimeanddateScrapper Python package to efficiently extract weather data from timeanddate.com.

2. Apache Kafka Integration: Implement a high-throughput, low-latency data streaming pipeline using Apache Kafka, ensuring reliable and real-time data transfer.

3. MongoDB Database: Store and manage the scraped weather data in a MongoDB database, offering scalability and flexibility for data storage needs.

4. Easy Configuration: Customize data scraping frequency, Kafka settings, and MongoDB connection parameters through simple configuration options.
Robust Error Handling: Implement error handling mechanisms to ensure smooth data extraction, transformation, and loading processes even in the presence of unexpected issues.

## Output
#### MongoDB:
[![Scrap-1.png](https://i.postimg.cc/8PTyHqgW/Scrap-1.png)](https://postimg.cc/14YcR7t5)

#### Response from MongoDB
[![Scrap-2.png](https://i.postimg.cc/SxJf14TX/Scrap-2.png)](https://postimg.cc/xXVmqwSY)
