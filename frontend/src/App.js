import React, { useState } from 'react';
import FileUpload from './components/FileUpload';
import DataTypesPage from './components/DataTypesPage';
import { uploadFile } from './api/api';

function App() {
    const [message, setMessage] = useState('');
    const [dataTypes, setDataTypes] = useState({});
    const [fileUploaded, setFileUploaded] = useState(false); // State to track if a file has been uploaded

    const handleFileUpload = async (file) => {
        try {
            const response = await uploadFile(file);
            setMessage(response.message); // Set the message from the response
            setDataTypes(response.data_types); // Set the data types from the response
            setFileUploaded(true); // Set fileUploaded to true after successful upload
        } catch (error) {
            console.error('Error uploading file:', error);
        }
    };

    return (
        <div className="App">
            <h1>Data Inference App</h1>
            {fileUploaded ? (
                <DataTypesPage message={message} dataTypes={dataTypes} />
            ) : (
                <FileUpload onFileUpload={handleFileUpload} />
            )}
        </div>
    );
}

export default App;
