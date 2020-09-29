import React, { useContext, useState } from 'react';
import { Redirect, Route, Switch, useLocation } from 'react-router-dom';
import Home from './components/home/Home';
import Login from './components/login/Login';
import Navbar from './components/navbar/Navbar';

const baseUrl = 'http://localhost:8000/';
const loginUrl = `${baseUrl}/auth/login/`;

var authContext = React.createContext(
    {
        user: null,
        apiToken: '',
        isAuthenticated: false,
        authenticate: null,
        signout: null
    }
);

function useAuthentication() {
    const [user, setUser] = useState(null);
    const [apiToken, setApiToken] = useState('');
    const [isAuthenticated, setIsAuthenticated] = useState(false);

    const authenticate = (username, password, onAuth) => {
        setTimeout(() => {
            setIsAuthenticated(true);
            if (onAuth) {
                onAuth();
            }
        }, 3000); // esto solo para probar
    };

    const signout = (onSignout) => {
        setTimeout(() => {
            setIsAuthenticated(false);
            if (onSignout) {
                onSignout();
            }
        }, 3000);
    };
    return { user, setUser, isAuthenticated, authenticate, signout };
};

const useAuthContext = () => {
    return useContext(authContext);
};

function App() {
    const { pathname } = useLocation();
    const auth = useAuthentication();

    return (
        <authContext.Provider value={auth}>
            <Switch>
                <Route path="/login">
                    <Login />
                </Route>
                {auth.isAuthenticated ?
                    (
                        <Route>
                            {/* El navbar aparece en todas las rutas menos en login */}
                            <Navbar />
                            <Switch>
                                <Route path="/home">
                                    <Home />
                                </Route>
                                <Redirect to="/home" />
                            </Switch>
                        </Route>
                    ) : (
                        <Redirect
                            to={{
                                pathname: "/login",
                                search: new URLSearchParams({
                                    next: pathname
                                }).toString()
                            }} />
                    )
                }
            </Switch >
        </authContext.Provider>
    );
}

export default App;

export { useAuthContext };

