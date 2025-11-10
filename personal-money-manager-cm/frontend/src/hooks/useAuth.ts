import { useState, useEffect } from 'react';
import { api } from '../services/api';

const useAuth = () => {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    const login = async (username, password) => {
        try {
            const response = await api.post('/api/v1/users/login', { username, password });
            setUser(response.data);
        } catch (err) {
            setError(err.response.data.message);
        } finally {
            setLoading(false);
        }
    };

    const logout = async () => {
        try {
            await api.post('/api/v1/users/logout');
            setUser(null);
        } catch (err) {
            setError(err.response.data.message);
        }
    };

    const checkAuth = async () => {
        try {
            const response = await api.get('/api/v1/users/me');
            setUser(response.data);
        } catch (err) {
            setUser(null);
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        checkAuth();
    }, []);

    return { user, loading, error, login, logout };
};

export default useAuth;