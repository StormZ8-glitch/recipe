import React, { useEffect, useState } from 'react';
import { fetchTransactions } from '../services/api';
import TransactionList from '../components/TransactionList';

const Transactions = () => {
    const [transactions, setTransactions] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const getTransactions = async () => {
            try {
                const data = await fetchTransactions();
                setTransactions(data);
            } catch (err) {
                setError(err.message);
            } finally {
                setLoading(false);
            }
        };

        getTransactions();
    }, []);

    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error}</div>;

    return (
        <div>
            <h1>Transactions</h1>
            <TransactionList transactions={transactions} />
        </div>
    );
};

export default Transactions;