import React, { useState } from 'react';
import { Button, Card, Col, Row } from 'react-materialize';
import Logo from '../../styles/Logo.module.css';
import styles from './Login.module.css';

function UsernameLoginField(props) {
    const [username, setUsername] = useState('');
    return (
        <Col s={12} className="input-field">
            <input id="User" name="username"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                type="text" className="validate" />
            <label for="User">User name</label>
        </Col>);
}

function PasswordLoginField(props) {
    const [password, setPassword] = useState('');
    return (
        <Col s={12} className="input-field">
            <input id="password" name="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                type="password" className="validate" />
            <label for="password">Password</label>
        </Col>);
}

function LoginButton(props) {
    return (
        <Col s={6} offset="s3" className="input-field">
            <Button className={styles.button}>log in</Button>
        </Col>);
}

function LoginForm(props) {
    return (
        <form action="" method="post">
            <Row className={styles.row}>
                <UsernameLoginField />
                <PasswordLoginField />
                <LoginButton />
            </Row>
        </form>
    );
}


function Login() {
    return (
        <Card className={styles.card}>
            <div className="card-content">
                <h1 className={Logo.socialgramLogo}>Pseudo-Instagram</h1>
                <LoginForm />
            </div>
        </Card>
    );
}


export default Login;