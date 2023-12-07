import streamlit as st
import pandas as pd
import pymongo

def connect_with_mongodb():
    '''
    this function creates a connection with the MongoDB database
    '''
    myclient = pymongo.MongoClient("mongodb://localhost:27017/", username='root', password='example')
    mydb = myclient["docstreaming"]
    mycol = mydb["invoices"]
    return mycol

def customer_id_query(mycol):
    '''
    This function add an input field for the customer ID and get all values for that field
    '''
    # Below the first chart, add an input field for the customer ID
    cust_id = st.sidebar.text_input("CustomerID:")

    # if enter has been used on the input field
    if cust_id:
        myquery = {"CustomerID": cust_id}
        mydoc = mycol.find(myquery, {"_id": 0, "Description": 0})
        df = pd.DataFrame(mydoc)
        df.drop_duplicates(subset="InvoiceNo", keep='first', inplace=True)
        st.header("Customer Invoices")
        table2 = st.dataframe(data=df)
        return table2

def invoice_no_query(mycol):
    """
        This function queries a MongoDB collection using an InvoiceNo provided as input and displays the results as a DataFrame in a Streamlit app.

        :Param mycol: The MongoDB collection to query.

        Returns:
        - table2: A Streamlit DataFrame containing the results of the query.
    """
    inv_no = st.sidebar.text_input("InvoiceNo:")
    if inv_no:
        myquery = {"InvoiceNo": inv_no}
        mydoc = mycol.find(myquery, {"_id": 0, "Description": 0, "InvoiceDate": 0, "Country": 0, "CustomerID": 0, "InvoiceDate": 0})

        df = pd.DataFrame(mydoc)

        reindexed = df.reindex(sorted(df.columns), axis=1)

        # Add the table with a headline
        st.header("Invoice ID")
        table2 = st.dataframe(data=reindexed)

        return table2

if __name__ == '__main__':
    mycol = connect_with_mongodb()
    customer_id_query(mycol)
    invoice_no_query(mycol)
