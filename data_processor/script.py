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

def infer_and_convert_data_types(uploaded_file, chunk_size=None):
    # Read the data from the uploaded file into a DataFrame
    if uploaded_file.name.endswith('.csv'):
        if chunk_size:
            chunks = pd.read_csv(uploaded_file, chunksize=chunk_size)
            pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
            results = pool.map(infer_and_convert_chunk, chunks)
            df = pd.concat(results)
        else:
            df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith(('.xls', '.xlsx')):
        if chunk_size:
            chunks = pd.read_excel(uploaded_file, chunksize=chunk_size)
            pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
            results = pool.map(infer_and_convert_chunk, chunks)
            df = pd.concat(results)
        else:
            df = pd.read_excel(uploaded_file)
    else:
        raise ValueError("Unsupported file format. Only CSV and Excel files are supported.")

    return df