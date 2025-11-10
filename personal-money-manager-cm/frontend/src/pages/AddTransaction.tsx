import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';
import TransactionForm from '../components/TransactionForm';
import { createTransaction } from '../services/api';

const AddTransaction = () => {
    const [error, setError] = useState(null);
    const history = useHistory();

    const handleSubmit = async (transactionData) => {
        try {
            await createTransaction(transactionData);
            history.push('/transactions');
        } catch (err) {
            setError('Failed to add transaction. Please try again.');
        }
    };

    return (
        <div>
            <h1>Add Transaction</h1>
            {error && <p className="error">{error}</p>}
            <TransactionForm onSubmit={handleSubmit} />
        </div>
    );
};

export default AddTransaction;