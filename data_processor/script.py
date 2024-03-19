import pandas as pd
import numpy as np
import multiprocessing

# Define a function for type inference and conversion
def infer_and_convert_chunk(df):
    # Convert numeric columns to more memory-efficient types
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, downcast='float')

    # Convert categorical columns to category dtype
    cat_cols = df.select_dtypes(include=['object']).columns
    for col in cat_cols:
        if len(df[col].unique()) / len(df[col]) < 0.5:
            df[col] = pd.Categorical(df[col])

    # Convert datetime columns to datetime dtype
    date_cols = df.select_dtypes(include=['datetime64']).columns
    for col in date_cols:
        df[col] = pd.to_datetime(df[col], errors='coerce')

    return df

def infer_detailed_data_types(df):
    """
    Infer detailed data types for DataFrame columns based on content.

    Args:
        df (pandas.DataFrame): Input DataFrame.

    Returns:
        dict: Dictionary containing detailed data types for each column.
    """
    detailed_data_types = {}
    for col in df.columns:
        column_data_type = str(df[col].dtype)

        if column_data_type == 'object':
            # Check if the column contains datetime-like strings
            try:
                pd.to_datetime(df[col], format='%d/%m/%Y')
                detailed_data_types[col] = 'Datetime'
            except ValueError:
                # If not, check for numeric or categorical data
                if df[col].str.replace('.', '', 1).str.isdigit().all():
                    detailed_data_types[col] = 'Numeric'
                else:
                    unique_values = df[col].dropna().unique()
                    num_unique_values = len(unique_values)
                    if num_unique_values == 2:
                        detailed_data_types[col] = 'Boolean'
                    elif num_unique_values / len(df) < 0.5:
                        detailed_data_types[col] = 'Categorical'
                    else:
                        detailed_data_types[col] = 'Text'
        elif column_data_type.startswith('float') or column_data_type.startswith('int'):
            detailed_data_types[col] = 'Numeric'
        else:
            detailed_data_types[col] = 'Unknown'

    return detailed_data_types

def infer_and_convert_data_types(uploaded_file, chunk_size=None):
    # Read the data from the uploaded file into a DataFrame
    if uploaded_file.endswith('.csv'):
        try:
            if chunk_size:
                chunks = pd.read_csv(uploaded_file, chunksize=chunk_size, encoding='utf-8')
                pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
                results = pool.map(infer_and_convert_chunk, chunks)
                df = pd.concat(results)
            else:
                df = pd.read_csv(uploaded_file)

            data_types = infer_detailed_data_types(df)

        except pd.errors.EmptyDataError:
            raise ValueError("Uploaded CSV file is empty")
    elif uploaded_file.endswith(('.xls', '.xlsx')):
        try:
            if chunk_size:
                chunks = pd.read_excel(uploaded_file)
                pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
                results = pool.map(infer_and_convert_chunk, chunks)
                df = pd.concat(results)
            else:
                df = pd.read_excel(uploaded_file)

            data_types = infer_detailed_data_types(df)

        except pd.errors.EmptyDataError:
            raise ValueError("Uploaded Excel file is empty")
    else:
        raise ValueError("Unsupported file format. Only CSV and Excel files are supported.")

    return data_types