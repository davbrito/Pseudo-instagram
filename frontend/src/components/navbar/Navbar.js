import React from 'react';
import { Col, Container, Row } from 'react-materialize';
import Styles from './Navbar.module.css';

function Title() {
    return (
        <Col s="2">
            <div className={Styles.Logo}>Pseudo</div>
        </Col>
    )
}

class Search extends React.Component {
    constructor(props) {
        super(props)
        this.state = { value: '' }
        this.handleClose = this.handleClose.bind(this)
        this.handleChange = this.handleChange.bind(this)
        this.handleSubmit = this.handleSubmit.bind(this)
    }

    handleClose() {
        this.setState({ value: '' });
        document.getElementById('searcher').focus()
    }

    handleChange(event) {
        this.setState({ value: event.target.value });
    }

    handleSubmit(event) {
        //
        event.preventDefault();
    }

    render(props) {
        return (
            <Col m="5" className="hide-on-small-only" style={{ position: "relative" }}>
                <input
                    id="searcher"
                    className={Styles.searcher}
                    type="search"
                    placeholder="Search"
                    value={this.state.value}
                    onChange={this.handleChange}
                />
                <label htmlFor="searcher"><i className={Styles.searchIcon}>search</i></label>
                <i className={Styles.searchClose} onClick={this.handleClose}>close</i>
            </Col>
        )
    }
}

function Navbar(props) {
    return (
        <nav>
            <div className={Styles.fondo}>
                <Container className={Styles.margen} >
                    <Row className={Styles.margen}>
                        <Title />
                        <Search />
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


export default Navbar;