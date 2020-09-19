import React from 'react';
import {Row} from 'react-materialize'
import styles from './Main.module.css'
import Login from '../login/Login'

function Main(){
    return(
        <div className={styles.background}>
            <div className={styles.container}>
                <Row>
                    <div className={styles.rowContainer}>
                        <Login/>
                    </div>
                </Row>
            </div>
        </div>
    )
}

export default Main