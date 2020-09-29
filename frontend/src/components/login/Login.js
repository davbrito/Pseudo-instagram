import React, { useState } from 'react';
import { Button, Card, Col, Row } from 'react-materialize';
import { useHistory, useLocation } from 'react-router-dom';
import { useAuthContext } from '../../App';
import { Logo as LogoStyle } from '../navbar/Navbar.module.css';
import styles from './Login.module.css';


function UsernameLoginField(props) {
    return (
        <Col s={12} className="input-field">
            <input id="User" name="username"
                autoFocus
                value={props.value}
                onChange={props.onChange}
                type="text" className="validate" />
            <label htmlFor="User">User name</label>
        </Col>);
}

function PasswordLoginField(props) {
    return (
        <Col s={12} className="input-field">
            <input id="password" name="password"
                value={props.value}
                onChange={props.onChange}
                type="password" className="validate" />
            <label htmlFor="password">Password</label>
        </Col>);
}

function LoginButton(props) {
    return (
        <Col s={6} offset="s3" className="input-field">
            <Button className={styles.button} type="submit" disabled={props.disabled}>log in</Button>
        </Col>
    );
}

function useQuery() {
    return new URLSearchParams(useLocation().search);
}

function LoginForm(props) {
    const { authenticate } = useAuthContext();
    const history = useHistory();
    const query = useQuery();
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [loading, setLoading] = useState(false);

    const submitHandler = (e) => {
        e.preventDefault();
        setLoading(true);
        authenticate(username, password,
            () => {
                history.push({ pathname: query.get('next') || '/home' });
            });
    };

    const validate = () => {
        return username.length > 0 && password.length > 0;
    }

    return (
        <form onSubmit={submitHandler}>
            <Row className={styles.row}>
                <UsernameLoginField value={username} onChange={(e) => setUsername(e.target.value)} />
                <PasswordLoginField value={password} onChange={(e) => setPassword(e.target.value)} />
                <LoginButton disabled={!validate()} />
            </Row>
            {loading && <p>Loading...</p>}
        </form>
    );
}


function Login(props) {
    return (
        <Card className={styles.card}>
            <h1 className={LogoStyle}>Pseudo-Instagram</h1>
            <LoginForm />
        </Card>
    );
}


export default Login;