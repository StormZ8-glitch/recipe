import React from 'react';
import { useEffect, useState } from 'react';
import { getTransactions } from '../services/api';
import SummaryCard from '../components/SummaryCard';
import TransactionList from '../components/TransactionList';

const Dashboard: React.FC = () => {
    const [transactions, setTransactions] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const fetchTransactions = async () => {
            try {
                const data = await getTransactions();
                setTransactions(data);
            } catch (err) {
                setError('Failed to fetch transactions');
            } finally {
                setLoading(false);
            }
        };

        fetchTransactions();
    }, []);

    const totalIncome = transactions
        .filter((transaction) => transaction.type === 'income')
        .reduce((acc, transaction) => acc + transaction.amount, 0);

    const totalExpenses = transactions
        .filter((transaction) => transaction.type === 'expense')
        .reduce((acc, transaction) => acc + transaction.amount, 0);

    const balance = totalIncome - totalExpenses;

    if (loading) {
        return <div>Loading...</div>;
    }

    if (error) {
        return <div>{error}</div>;
    }

    return (
        <div>
            <h1>Dashboard</h1>
            <SummaryCard totalIncome={totalIncome} totalExpenses={totalExpenses} balance={balance} />
            <TransactionList transactions={transactions} />
        </div>
    );
};

export default Dashboard;