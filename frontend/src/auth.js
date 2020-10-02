import { useEffect, useState } from "react";
import { authUserUrl, loginUrl, logoutUrl } from './api/endpoints';

function createTokenProvider() {
    let _token =
        JSON.parse(localStorage.getItem('PSEUDOIG_TOKEN_AUTH') || 'null');

    const setToken = (token) => {
        if (token) {
            localStorage.setItem('PSEUDOIG_TOKEN_AUTH', JSON.stringify(token));
        } else {
            localStorage.removeItem('PSEUDOIG_TOKEN_AUTH');
        }
        _token = token;
        notify();
    };

    const getToken = () => {
        if (!_token)
            return null;
        return _token;
    };

    const isLoggedIn = () => {
        return !!_token;
    };

    let observers = [];

    const subscribe = (observer) => {
        observers.push(observer);
    };

    const unsubscribe = (observer) => {
        observers = observers.filter(_observer => _observer !== observer);
    };

    const notify = () => {
        const isLogged = isLoggedIn();
        observers.forEach(observer => observer(isLogged));
    };

    const fetchToken = async (username, password) => {
        const init = {
            method: 'POST',
            body: JSON.stringify({ username, password }),
            headers: {
                'Content-Type': 'application/json'
            }
        };
        const token = await fetch(loginUrl, init).then(async (response) => {
            if (response.ok) {
                const token = await response.json().then(data => data.key);
                setToken(token);
                return token;
            }
            setToken(null);
            const data = await response.json().then(data => data);
            throw data;
        });
        return token;
    };
    return { setToken, getToken, fetchToken, isLoggedIn, subscribe, unsubscribe };
};

const createAuthProvider = () => {
    let _authUser =
        JSON.parse(localStorage.getItem('PSEUDOIG_AUTH_USER') || 'null');

    const authFetch = async (input, init) => {
        const token = tokenProvider.getToken();

        init = init || {};
        init.headers = {
            ...init.headers,
            Authorization: `token ${token}`,
            'Content-Type': 'application/json',
        };

        return fetch(input, init);
    };

    const useAuthentication = () => {
        // const [user, setUser] = useState(null);
        const [isAuthenticated, setIsAuthenticated] = useState(tokenProvider.isLoggedIn);

        useEffect(() => {
            const listener = (isLoggedIn) => {
                setIsAuthenticated(isLoggedIn);
            };
            tokenProvider.subscribe(listener);
            return () => { tokenProvider.unsubscribe(listener); };
        }, []);
        return [isAuthenticated];
    };

    const login = async (username, password, onLogin) => {
        await tokenProvider.fetchToken(username, password);
        if (onLogin) {
            onLogin();
        }
        updateAuthUser();
    };
    const updateAuthUser = async () => {
        const user = await authFetch(authUserUrl)
            .then((response) => {
                if (response.ok) {
                    return response.json();
                } else {
                    return null;
                }
            });
        if (user) {
            localStorage.setItem('PSEUDOIG_AUTH_USER', JSON.stringify(user));
        } else {
            localStorage.removeItem('PSEUDOIG_AUTH_USER');
        }
        _authUser = user;
    };

    const logout = async (onLogout) => {
        const init = { method: 'POST' };
        await authFetch(logoutUrl, init).then(() => {
            tokenProvider.setToken(null);
        }).then(() => {
            localStorage.removeItem('PSEUDOIG_AUTH_USER');
            if (onLogout) {
                onLogout();
            }
        });
    };

    const useAuthUser = () => {
        const [user] = useState(_authUser || null);
        return user;
    };
    return { authFetch, useAuthentication, login, logout, useAuthUser };
};

const tokenProvider = createTokenProvider();
export const { authFetch, useAuthentication, login, logout, useAuthUser } = createAuthProvider();
