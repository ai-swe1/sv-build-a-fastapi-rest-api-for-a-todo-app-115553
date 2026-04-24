js
// src/apiClient.js
const BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api/v1';

export const request = async (path, {method = 'GET', body = null, headers = {}} = {}) => {
  const cfg = {
    method,
    headers: {
      'Content-Type': 'application/json',
      ...headers,
    },
    ...(body && {body: JSON.stringify(body)}),
  };
  const resp = await fetch(`${BASE_URL}${path}`, cfg);
  if (!resp.ok) {
    const err = await resp.json();
    throw new Error(err.detail || resp.statusText);
  }
  return resp.json();
}