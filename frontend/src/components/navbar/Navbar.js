import React,{Component} from 'react';
import {Container,Row,Col} from 'react-materialize'
import Styles from './Navbar.module.css'

class Navbar extends Component{


    render(){
        return(
            <nav>
            <div className={Styles.fondo}>
            <Container className={Styles.margen} >
                <Row className={Styles.margen}>
                    <Col s="2">
                        <div className={Styles.Logo}>Pseudo</div>
                    </Col>
                    <Col m="5" className="hide-on-small-only" style={{position: "relative"}}>
                        <input id="searcher" placeholder="Search" type="search" className={Styles.searcher} />
                        <label htmlFor="searcher"><i className={Styles.searchIcon}>search</i></label>
                        <i className={Styles.searchClose}>close</i>
                    </Col>
                    <Col s="2" m="1" ><i align="center" className="material-icons">home</i></Col>
                    <Col s="2" m="1" ><i align="center" className="material-icons">inbox</i></Col>
                    <Col s="2" m="1" ><i align="center" className="material-icons">explore</i></Col>
                    <Col s="2" m="1" ><i align="center" className="material-icons">favorite_border</i></Col>
                    <Col s="2" m="1" ><i align="center" className="material-icons">person_outline</i></Col>
                </Row>
            </Container>
            </div>
            </nav>
        )
    }

}


export default Navbar;