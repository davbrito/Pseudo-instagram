import React, { useEffect } from 'react';
import { Container } from 'react-materialize';
import { Redirect, Route, Switch, useHistory, useLocation } from 'react-router-dom';
import { logout, useAuthentication } from './auth';
import Home from './components/home/Home';
import Login from './components/login/Login';
import Navbar from './components/navbar/Navbar';
import User from './components/user/User';
import useNext from './hooks/useNext';

function Logout() {
    const next = useNext();
    const history = useHistory();
    useEffect(() => {
        logout().then(() => { history.push(next || '/login'); });
    }, [next, history]);
    return <p>Logging out.</p>;
}

function App() {
    const { pathname } = useLocation();
    const [isAuthenticated] = useAuthentication();

    return (
        <Switch>
            <Route path="/login">
                <Login />
            </Route>
            <Route path="/logout">
                {isAuthenticated ? <Logout /> : <Redirect to="/login" />}
            </Route>
            {isAuthenticated ?
                (
                    <Switch>
                        <Route>
                            {/* El navbar aparece en todas las rutas menos en login */}
                            <Navbar />
                            <Container>

                            <Switch>
                                <Route path="/home">
                                    <Home />
                                </Route>
                                    <Route path="/users/:username">
                                        <User />
                                    </Route>
                                <Redirect to="/home" />
                            </Switch>
                            </Container>
                        </Route>
                    </Switch>
                ) : (
                    <Redirect
                        to={{
                            pathname: "/login",
                            search: pathname === '/logout'
                                ? ''
                                : new URLSearchParams({
                                    next: pathname
                                }).toString()
                        }} />
                )
            }
        </Switch >
    );
}

export default App;