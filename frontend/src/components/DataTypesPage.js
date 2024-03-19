import React from 'react';

const DataTypesPage = ({ message, dataTypes }) => {
    return (
        <div>
            <p>{message}</p>
            <ul>
                {Object.entries(dataTypes).map(([column, type]) => (
                    <li key={column}>{`${column}: ${type}`}</li>
                ))}
            </ul>
        </div>
    );
};

export default DataTypesPage;
