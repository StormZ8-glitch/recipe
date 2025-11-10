import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Dashboard from './pages/Dashboard';
import Transactions from './pages/Transactions';
import AddTransaction from './pages/AddTransaction';
import SavingsGoals from './pages/SavingsGoals';
import NavBar from './components/NavBar';
import './styles/globals.css';

const App: React.FC = () => {
  return (
    <Router>
      <NavBar />
      <Switch>
        <Route path="/" exact component={Dashboard} />
        <Route path="/transactions" component={Transactions} />
        <Route path="/add-transaction" component={AddTransaction} />
        <Route path="/savings-goals" component={SavingsGoals} />
      </Switch>
    </Router>
  );
};

export default App;