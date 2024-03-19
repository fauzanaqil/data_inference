const API_BASE_URL = 'http://localhost:8000/api/';

export const uploadFile = async (file) => {
  const response = await fetch(`${API_BASE_URL}upload/`, {
    method: 'POST',
    body: file
  });
  return await response.json();
};