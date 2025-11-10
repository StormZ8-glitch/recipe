import React, { useState } from 'react';

const TransactionForm = ({ onSubmit, initialData }) => {
    const [amount, setAmount] = useState(initialData ? initialData.amount : '');
    const [category, setCategory] = useState(initialData ? initialData.category : '');
    const [date, setDate] = useState(initialData ? initialData.date : '');
    const [description, setDescription] = useState(initialData ? initialData.description : '');

    const handleSubmit = (e) => {
        e.preventDefault();
        const transactionData = { amount, category, date, description };
        onSubmit(transactionData);
        resetForm();
    };

    const resetForm = () => {
        setAmount('');
        setCategory('');
        setDate('');
        setDescription('');
    };

    return (
        <form onSubmit={handleSubmit}>
            <div>
                <label>Amount:</label>
                <input
                    type="number"
                    value={amount}
                    onChange={(e) => setAmount(e.target.value)}
                    required
                />
            </div>
            <div>
                <label>Category:</label>
                <input
                    type="text"
                    value={category}
                    onChange={(e) => setCategory(e.target.value)}
                    required
                />
            </div>
            <div>
                <label>Date:</label>
                <input
                    type="date"
                    value={date}
                    onChange={(e) => setDate(e.target.value)}
                    required
                />
            </div>
            <div>
                <label>Description:</label>
                <textarea
                    value={description}
                    onChange={(e) => setDescription(e.target.value)}
                />
            </div>
            <button type="submit">Save Transaction</button>
        </form>
    );
};

export default TransactionForm;