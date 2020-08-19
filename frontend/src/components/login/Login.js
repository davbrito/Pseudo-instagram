import React, { Component} from 'react'
import {Card, Row, Button, Col} from 'react-materialize'
import styles from './Login.module.css'
import Logo from '../../styles/Logo.module.css'

class Login extends Component {
    render() {
        return (
            <Card className={styles.card}>
                <div className="card-content">
                    <h1 className={Logo.socialgramLogo}>Pseudo-Instagram</h1>
                    <form action="" method="post">
                        <Row className={styles.row}>
                            <Col s="12" className="input-field">
                                <input id="User" type="text" className="validate"/>
                                <label for="User">User name</label>
                            </Col>
                            <Col s="12" className="input-field">
                                <input id="password" type="password" className="validate"/>
                                <label for="password">Password</label>
                            </Col>
                            <Col s="6" offset="s3" className="input-field">
                                <Button className={styles.button}>log in</Button>
                            </Col>
                        </Row>
                    </form>
                </div>
            </Card>
        )
    }
}

export default Login