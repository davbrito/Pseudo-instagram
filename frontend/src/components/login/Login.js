import React, { Component} from 'react'
import {Card, Row, Button} from 'react-materialize'
import styles from './Login.module.css'

class Login extends Component {
    render() {
        return (
            <Card className={styles.card}>
                <div className="card-content">
                        <h1 className={styles.socialgramLogo}>Pseudo-Instagram</h1>
                    <form action="" method="post">
                        <Row className={styles.row}>
                            <div className="input-field col s12">
                                <input id="User" type="text" className="validate"/>
                                <label for="User">User name</label>
                            </div>
                            <div className="input-field col s12">
                                <input id="password" type="password" class="validate"/>
                                <label for="password">Password</label>
                            </div>
                            <div className="col s6 offset-s3">
                                <Button className={styles.button}>log in</Button>
                            </div>
                        </Row>
                    </form>
                </div>
            </Card>
        )
    }
}

export default Login