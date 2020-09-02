import React, { Component } from 'react'
import { Button, Card, Col, Row } from 'react-materialize'
import Logo from '../../styles/Logo.module.css'
import styles from './Login.module.css'

class LoginForm extends Component {
    constructor(props) {
        super(props)
        this.state = { username: '', password: '' }
        this.handleInputChange = this.handleInputChange.bind(this);
    }

    handleInputChange(event) {
        const target = event.target;
        const value = target.value;
        const name = target.name;
        this.setState({ [name]: value });
    }

    render() {
        return (
            <form action="" method="post">
                <Row className={styles.row}>
                    <Col s="12" className="input-field">
                        <input id="User" name="username"
                            value={this.state.username}
                            onChange={this.handleInputChange}
                            type="text" className="validate" />
                        <label for="User">User name</label>
                    </Col>
                    <Col s="12" className="input-field">
                        <input id="password" name="password"
                            value={this.state.password}
                            onChange={this.handleInputChange}
                            type="password" className="validate" />
                        <label for="password">Password</label>
                    </Col>
                    <Col s="6" offset="s3" className="input-field">
                        <Button className={styles.button}>log in</Button>
                    </Col>
                </Row>
            </form>
        )
    }
}

function Login() {
    return (
        <Card className={styles.card}>
            <div className="card-content">
                <h1 className={Logo.socialgramLogo}>Pseudo-Instagram</h1>
                <LoginForm />
            </div>
        </Card>
    )
}


export default Login