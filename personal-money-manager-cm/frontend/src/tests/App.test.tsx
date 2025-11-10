import React from 'react';
import { render, screen } from '@testing-library/react';
import App from '../App';

test('renders the app and checks for essential elements', () => {
  render(<App />);
  
  const dashboardLink = screen.getByText(/dashboard/i);
  const transactionsLink = screen.getByText(/transactions/i);
  const savingsGoalsLink = screen.getByText(/savings goals/i);
  
  expect(dashboardLink).toBeInTheDocument();
  expect(transactionsLink).toBeInTheDocument();
  expect(savingsGoalsLink).toBeInTheDocument();
});