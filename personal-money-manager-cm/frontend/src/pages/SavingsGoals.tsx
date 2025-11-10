import React, { useState, useEffect } from 'react';
import { fetchSavingsGoals, createSavingsGoal } from '../services/api';

const SavingsGoals = () => {
    const [goals, setGoals] = useState([]);
    const [goalName, setGoalName] = useState('');
    const [goalAmount, setGoalAmount] = useState(0);
    const [goalDeadline, setGoalDeadline] = useState('');

    useEffect(() => {
        const loadGoals = async () => {
            const fetchedGoals = await fetchSavingsGoals();
            setGoals(fetchedGoals);
        };
        loadGoals();
    }, []);

    const handleSubmit = async (e) => {
        e.preventDefault();
        const newGoal = { name: goalName, amount: goalAmount, deadline: goalDeadline };
        await createSavingsGoal(newGoal);
        setGoals([...goals, newGoal]);
        setGoalName('');
        setGoalAmount(0);
        setGoalDeadline('');
    };

    return (
        <div>
            <h1>Savings Goals</h1>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    placeholder="Goal Name"
                    value={goalName}
                    onChange={(e) => setGoalName(e.target.value)}
                    required
                />
                <input
                    type="number"
                    placeholder="Goal Amount"
                    value={goalAmount}
                    onChange={(e) => setGoalAmount(Number(e.target.value))}
                    required
                />
                <input
                    type="date"
                    value={goalDeadline}
                    onChange={(e) => setGoalDeadline(e.target.value)}
                    required
                />
                <button type="submit">Add Goal</button>
            </form>
            <h2>Your Goals</h2>
            <ul>
                {goals.map((goal, index) => (
                    <li key={index}>
                        {goal.name} - {goal.amount} by {goal.deadline}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default SavingsGoals;