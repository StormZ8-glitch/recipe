import axios from 'axios';

const API_URL = 'http://localhost:8000/api/v1'; // Adjust the URL as needed

// Function to get all transactions
export const getTransactions = async () => {
    const response = await axios.get(`${API_URL}/transactions`);
    return response.data;
};

// Function to add a new transaction
export const addTransaction = async (transaction) => {
    const response = await axios.post(`${API_URL}/transactions`, transaction);
    return response.data;
};

// Function to update an existing transaction
export const updateTransaction = async (id, transaction) => {
    const response = await axios.put(`${API_URL}/transactions/${id}`, transaction);
    return response.data;
};

// Function to delete a transaction
export const deleteTransaction = async (id) => {
    const response = await axios.delete(`${API_URL}/transactions/${id}`);
    return response.data;
};

// Function to get user savings goals
export const getSavingsGoals = async () => {
    const response = await axios.get(`${API_URL}/goals`);
    return response.data;
};

// Function to add a new savings goal
export const addSavingsGoal = async (goal) => {
    const response = await axios.post(`${API_URL}/goals`, goal);
    return response.data;
};

// Function to update an existing savings goal
export const updateSavingsGoal = async (id, goal) => {
    const response = await axios.put(`${API_URL}/goals/${id}`, goal);
    return response.data;
};

// Function to delete a savings goal
export const deleteSavingsGoal = async (id) => {
    const response = await axios.delete(`${API_URL}/goals/${id}`);
    return response.data;
};