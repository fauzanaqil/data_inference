import React, { useState } from 'react';

const FileUpload = ({ onFileUpload }) => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [fileUploaded, setFileUploaded] = useState(false);

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    const formData = new FormData();
    formData.append('file', selectedFile);
    try {
      await onFileUpload(formData);
      setFileUploaded(true);
      // Redirect to the root URL upon successful upload
    } catch (error) {
      console.error('Error uploading file:', error);
      // Handle error
    }
  };

  return (
    <div>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleSubmit}>Upload</button>
      {fileUploaded && <p>File uploaded successfully!</p>}
    </div>
  );
};

export default FileUpload;
