import React, { useEffect, useState } from 'react';
import { Button, Card, Col, Row } from 'react-materialize';
import { useHistory } from 'react-router-dom';
import { login } from '../../auth';
import useQuery from '../../hooks/useQuery';
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

function LoginError({ error }) {
    const { non_field_errors } = error;
    return (
        <ul style={{ color: 'red' }}>
            {non_field_errors.map(err => (<li>* {err}</li>))}
        </ul>
    );
}

function LoginForm(props) {
    const history = useHistory();
    const query = useQuery();
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');
    const [isValid, setValid] = useState(false);

    useEffect(() => {
        setValid(username.length > 0 && password.length > 0);
    }, [username, password]
    );

    const submitHandler = (e) => {
        e.preventDefault();
        setLoading(true);
        login(username, password).then(() => {
            history.push({ pathname: query.get('next') || '/home' });
        }).catch(reason => {
            setLoading(false);
            setError(reason);
        });
    };

    return (
        <form onSubmit={submitHandler}>
            <Row className={styles.row}>
                <UsernameLoginField value={username} onChange={(e) => setUsername(e.target.value)} />
                <PasswordLoginField value={password} onChange={(e) => setPassword(e.target.value)} />
                <LoginButton disabled={!isValid} />
            </Row>
            {loading && <p>Loading...</p>}
            {error && <LoginError error={error} />}
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