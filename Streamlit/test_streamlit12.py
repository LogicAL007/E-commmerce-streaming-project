from streamlit12 import invoice_no_query
from streamlit12 import connect_with_mongodb
import pandas as pd
from pytest_mock import mocker
import streamlit as st
from streamlit12 import customer_id_query

mycol= connect_with_mongodb()
def test_valid_invoice_no( mocker):
    '''
    This Function returns a Streamlit DataFrame containing the results of the query when a valid InvoiceNo is provided.
    '''
    # Mocking the st.sidebar.text_input method to return a valid InvoiceNo
    mocker.patch('streamlit.sidebar.text_input', return_value='12345')
    
    # Mocking the mycol.find method to return a MongoDB query result
    mocker.patch.object(mycol, 'find', return_value=[{"_id": 1, "InvoiceNo": "12345", "Description": "Product A", "Quantity": 2}])

    # Mocking the st.dataframe method to return a Streamlit DataFrame
    mocker.patch('streamlit.dataframe', return_value='table')
    
    # Call the function under test
    result = invoice_no_query(mycol)
    
     # Assert that the function returns a Streamlit DataFrame
    assert result == 'table'


def test_invalid_invoice_no(mocker):
    '''
    This Function returns an empty DataFrame when an invalid InvoiceNo is provided.
    '''
    # Mocking the st.sidebar.text_input method to return an invalid InvoiceNo
    mocker.patch('streamlit.sidebar.text_input', return_value='')

    # Call the function under test
    result = invoice_no_query(mycol)

    # Assert that the function returns None
    assert result is None

def test_invalid_customer_id(mocker):
    '''
    This Function returns an empty DataFrame when an invalid InvoiceNo is provided.
    '''
    # Mocking the st.sidebar.text_input method to return an invalid InvoiceNo
    mocker.patch('streamlit.sidebar.text_input', return_value='')

    # Call the function under test
    result = customer_id_query(mycol)

    # Assert that the function returns None
    assert result is None

    # 
def test_valid_customer_id(self, mocker):
    '''
    This Function returns a dataframe when a valid customer ID is entered
    '''
    # Mocking the streamlit sidebar text_input method
    mocker.patch.object(st.sidebar, 'text_input', return_value='12345')
    
    # Mocking the mycol.find method
    mocker.patch.object(mycol, 'find', return_value=[{"InvoiceNo": "1", "CustomerID": "12345", "Description": "Product 1"},
                                                        {"InvoiceNo": "2", "CustomerID": "12345", "Description": "Product 2"}])
    
    # Mocking the st.dataframe method
    mocker.patch.object(st, 'dataframe')
    
    # Calling the function under test
    result = customer_id_query(mycol)
    
    # Asserting that the st.dataframe method was called with the correct data
    st.dataframe.assert_called_once_with(data=pd.DataFrame([{"InvoiceNo": "1", "CustomerID": "12345", "Description": "Product 1"},
                                                                {"InvoiceNo": "2", "CustomerID": "12345", "Description": "Product 2"}]))
    
    # Asserting that the result is equal to the mocked st.dataframe method
    assert result == st.dataframe.return_value