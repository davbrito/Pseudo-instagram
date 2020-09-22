import React, { useState } from 'react';
import { Redirect, Route, Switch, useLocation } from 'react-router-dom';
import Home from './components/home/Home';
import Login from './components/login/Login';
import Navbar from './components/navbar/Navbar';

const baseUrl = 'http://localhost:8000/';
const loginUrl = `${baseUrl}/auth/login/`;

var authContext = React.createContext({ user: null, apiToken: null, isAuthenticated: false });

const useAuthentication = () => {
    const [isAuthenticated, setIsAuthenticated] = useState(false);

    const authenticate = async (username, password) => {
        await new Promise(resolve => setTimeout(() => {
            setIsAuthenticated(true);
            resolve();
        }, 3000)); // esto solo para probar
        console.log(isAuthenticated);
        // const response = await fetch(loginUrl, { method: 'POST', body: { username, password } });
        // if (response.ok) {
        //     setIsAuthenticated(true);
        // }
        // return response.json();
    };
    return [isAuthenticated, authenticate];
};

function App() {
    const { pathname } = useLocation();
    const [isAuthenticated, authenticate] = useAuthentication();

    return (
        <Switch>
            <Route path="/login">
                <Login authenticate={authenticate} />
            </Route>
            <Route>
                {isAuthenticated ?
                    <>
                        {/* El navbar aparece en todas las rutas menos en login */}
                        < Navbar />
                        <Route path="/home">
                            <Home />
                        </Route>
                        <Route path="/">
                            <Redirect to="/home" />
                        </Route>
                    </>
                    : <Redirect from="/"
                        to={{
                            pathname: "/login",
                            search: new URLSearchParams({ next: pathname }).toString()
                        }} />
                }
            </Route>
        </Switch>
    );
}

export default App;

export { useAuthentication };

