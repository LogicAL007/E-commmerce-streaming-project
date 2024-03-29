# E-commerce Document streaming Data Pipeline
 This project aims to create a data pipeline that processes CSV files, converts them into JSON format, performs data transformation using Apache Spark, stores the transformed data in MongoDB, and provides visualization through a Streamlit dashboard

## Data Sources
[E-commmerce data](https://www.kaggle.com/datasets/carrie1/ecommerce-data)  from Kaggle

## Tech stack
- **Kafka**
  >>Kafka is an open-source stream-processing platform developed by the Apache Software Foundation. It is designed to handle high-throughput, fault-tolerant, and real-time data streaming. Kafka allows organizations to publish, subscribe, store, and process streams of records, which can include data from various sources such as databases, sensors, logs, and more. It provides a distributed architecture that enables data to be efficiently and reliably transferred between producers and consumers, making it a popular choice for building data pipelines, event-driven architectures, and real-time analytics systems.
- **Pyspark**
  >>PySpark is the Python API for Apache Spark. It allows you to write Spark applications using Python, a language that is widely known and used by data scientists and engineers. PySpark provides the ability to leverage Spark's distributed computing capabilities for data processing tasks, machine learning, graph processing, and more, all while working within the Python programming environment.
- **MongoDB**
  >> MongoDB is an open-source NoSQL database system that stores and manages data in flexible, JSON-like documents. It offers schema flexibility, scalability, and supports features like replication, high availability, and flexible querying. MongoDB is widely used for various applications, providing an efficient and adaptable solution for handling structured, semi-structured, and unstructured data.
- **Streamlit**
  >>Streamlit is an open-source Python library that empowers data professionals to transform data scripts into interactive web applications effortlessly. With minimal code, you can craft web-based interfaces featuring data visualizations, charts, and dynamic widgets for user interaction. Streamlit's real-time updates ensure that changes to your code are immediately reflected in the application, allowing for seamless development. By integrating with popular data libraries, Streamlit facilitates the creation of engaging and user-friendly data-driven apps, making it a valuable asset for sharing insights and analyses with a broader audience.
- Postman
  >>**Postman** is a widely used API (Application Programming Interface) testing and development tool that simplifies the process of building, testing, and documenting APIs. It provides an intuitive interface for developers and testers to interact with APIs and perform tasks such as sending HTTP requests, viewing responses, and validating API behavior. Postman offers a user-friendly environment for creating and organizing requests, setting up authentication, handling different request types, and visualizing data

## Data Pipeline 

![docstreamingor](https://github.com/LogicAL007/E-commmerce-streaming-project/assets/122959675/3ee32cf2-1f8e-4a96-b6bf-d588de405e83)

# Data Pipeline Overview

This repository outlines a robust data pipeline, designed to ingest, process, transform, store, and visualize data. The pipeline is built upon several state-of-the-art technologies, ensuring efficient data handling and presentation.

## 1. CSV to JSON Conversion

- **Description**: 
  - The pipeline starts by ingesting CSV files as input.
  - It reads the files, extracts the data, and converts it into JSON format.
  
- **Purpose**: 
  - This step ensures that the data is ready for further processing.

## 2. Testing the Ingest API with Postman

- **Description**: 
  - After conversion, the integrity and correctness of the data ingestion API are tested using Postman, ensuring a seamless data transfer process.

## 3. Streaming with Kafka

- **Description**: 
  - Once the data is converted into JSON, it is streamed using Apache Kafka.
  - Kafka acts as a distributed messaging system.
  
- **Features**: 
  - Kafka provides fault-tolerant and scalable data streaming capabilities.
  - It allows for efficient handling of large volumes of data.

## 4. Data Transformation with Apache Spark

- **Description**: 
  - The streaming data from Kafka is consumed by Apache Spark.
  - Spark is a powerful distributed data processing engine.
  
- **Capabilities**: 
  - Spark enables data transformation tasks, such as filtering, aggregating, and applying complex computations or machine learning algorithms.
  - The transformed data is then prepared for storage.

## 5. Storing Data in MongoDB

- **Description**: 
  - The transformed data is stored in a MongoDB database.
  
- **Features**: 
  - MongoDB is a popular NoSQL database.
  - It provides flexibility and scalability for handling diverse data types.
  - MongoDB stores the transformed data in a structured manner, which allows for efficient retrieval and analysis.

## 6. Visualization with Streamlit Dashboard

- **Description**: 
  - To provide a user-friendly interface for data exploration and visualization, a Streamlit dashboard is developed.
  
- **Features**: 
  - Streamlit is a Python library for creating interactive web applications.
  - It makes it easy to build data-driven dashboards.
  - The dashboard enables users to visualize and analyze the data stored in MongoDB in a dynamic and intuitive manner.
