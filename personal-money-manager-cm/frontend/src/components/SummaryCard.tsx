import React from 'react';

interface SummaryCardProps {
    totalIncome: number;
    totalExpenses: number;
    balance: number;
    savingsGoal: number;
}

const SummaryCard: React.FC<SummaryCardProps> = ({ totalIncome, totalExpenses, balance, savingsGoal }) => {
    return (
        <div className="summary-card">
            <h2>Summary</h2>
            <div className="summary-item">
                <span>Total Income:</span>
                <span>{totalIncome.toFixed(2)} XAF</span>
            </div>
            <div className="summary-item">
                <span>Total Expenses:</span>
                <span>{totalExpenses.toFixed(2)} XAF</span>
            </div>
            <div className="summary-item">
                <span>Balance:</span>
                <span>{balance.toFixed(2)} XAF</span>
            </div>
            <div className="summary-item">
                <span>Savings Goal:</span>
                <span>{savingsGoal.toFixed(2)} XAF</span>
            </div>
        </div>
    );
};

export default SummaryCard;