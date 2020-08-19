import React,{Component} from 'react';
import {Container} from 'react-materialize'
import Styles from './Navbar.module.css'
//mport Searcher from '../searcher/Searcher'

class Navbar extends Component{


    render(){
        return(
            <nav>
            <div className={Styles.fondo}>
            <Container className={Styles.margen}>
                <a href="#!" className={Styles.Logo}>Pseudo-Ig</a>
                <ul id="nav-mobile" className="right">
                    <li><a href="sass.html"><i className="material-icons">search</i></a></li>
                    <li><a href="sass.html"><i className="material-icons">home</i></a></li>
                    <li><a href="badges.html"><i className="material-icons">inbox</i></a></li>
                    <li><a href="sass.html"><i className="material-icons">explore</i></a></li>
                    <li><a href="collapsible.html"><i className="material-icons">favorite_border</i></a></li>
                    <li><a href="mobile.html"><i className="material-icons">person_outline</i></a></li>
                </ul>
            </Container>
            </div>
            </nav>
        )
    }

}


export default Navbar;