# E-commerce Document streaming Data Pipeline
 This project aims to create a data pipeline that processes CSV files, converts them into JSON format, performs data transformation using Apache Spark, stores the transformed data in MongoDB, and provides visualization through a Streamlit dashboar


**this is a bold**

## Tech stack
->Kafka	
->Pyspark/sparkSL
->MongoDB
->Streamlit
->Postman


The data pipeline follows the following steps:

CSV to JSON Conversion: The pipeline starts by ingesting CSV files as input. It reads the files, extracts the data, and converts it into JSON format. This step ensures that the data is ready for further processing.

Streaming with Kafka: Once the data is converted into JSON, it is streamed using Apache Kafka, which acts as a distributed messaging system. Kafka provides fault-tolerant and scalable data streaming capabilities, allowing for efficient handling of large volumes of data.

Data Transformation with Apache Spark: The streaming data from Kafka is consumed by Apache Spark, a powerful distributed data processing engine. Spark enables data transformation tasks, such as filtering, aggregating, and applying complex computations or machine learning algorithms. The transformed data is then prepared for storage.

Storing Data in MongoDB: The transformed data is stored in a MongoDB database, a popular NoSQL database that provides flexibility and scalability for handling diverse data types. MongoDB stores the transformed data in a structured manner, allowing for efficient retrieval and analysis.

Visualization with Streamlit Dashboard: To provide a user-friendly interface for data exploration and visualization, a Streamlit dashboard is developed. Streamlit is a Python library for creating interactive web applications, making it easy to build data-driven dashboards. The dashboard enables users to visualize and analyze the data stored in MongoDB in a dynamic and intuitive manner.


## Usage/Examples

```javascript
import Component from 'my-project'

function App() {
  return <Component />
}
```
