import React from 'react';
import { Col, Container, Icon, Row } from 'react-materialize';
import Styles from './Navbar.module.css';

function Title() {
    return (
        <Col s="2">
            <div className={Styles.Logo}>Pseudo</div>
        </Col>
    );
}

class Search extends React.Component {
    constructor(props) {
        super(props);
        this.state = { value: '' };
        this.handleClose = this.handleClose.bind(this);
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleClose() {
        this.setState({ value: '' });
        document.getElementById('searcher').focus();
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
                <label htmlFor="searcher"><Icon className={Styles.searchIcon}>search</Icon></label>
                <Icon className={Styles.navIcon} className={Styles.searchClose} onClick={this.handleClose}>close</Icon>
            </Col>
        );
    }
}

function NavIconButton(props) {
    return (
        <Col s="2" m="1" align="center" className={Styles.navIcon}>
            <Icon>{props.name}</Icon>
        </Col>
    );
}

function NavButtons(props) {
    return props.names.map(name => (<NavIconButton key={name} name={name} />));
}

function Navbar(props) {
    return (
        <div className="navbar-fixed">
            <nav>
                <div className={Styles.fondo}>
                    <Container >
                        <Row >
                            <Title />
                            <Search />
                            <NavButtons names={[
                                'home', 'inbox', 'explore',
                                'favorite_border', 'person_outline'
                            ]} />
                        </Row>
                    </Container>
                </div>
            </nav>
        </div>
    );
}


export default Navbar;