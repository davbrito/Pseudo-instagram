import React from 'react';
import { Col, Container, Icon, NavItem, Row } from 'react-materialize';
import Styles from './Navbar.module.css';

function Title() {
    return (
        <Col s={2}>
            <div className={Styles.Logo}>Pseudo</div>
        </Col>
    );
}

function Search(props) {
    const [value, setValue] = React.useState('');

    const handleClose = () => {
        setValue('');
        document.getElementById('searcher').focus();
    };

    const handleChange = (event) => {
        setValue(event.target.value);
    };

    const handleSubmit = (event) => {
        //
        event.preventDefault();
    };

    return (
        <Col m={5} className="hide-on-small-only" style={{ position: "relative" }}>
            <spam>
                <input
                    id="searcher"
                    className={Styles.searcher}
                    type="search"
                    placeholder="Search"
                    value={value}
                    onChange={handleChange}
                />
                <label htmlFor="searcher"><Icon className={Styles.searchIcon}>search</Icon></label>
                <button onClick={handleClose} className={Styles.searchClose}>
                    close
                </button>
            </spam>
        </Col>
    );

}

function NavIconButton(props) {
    return (
        <Col s={2} m={1} align="center">
            <NavItem className={Styles.navIcon}>
                <Icon>{props.name}</Icon>
            </NavItem>
        </Col>
    );
}

function NavButtons(props) {
    const names = [
        'home', 'inbox', 'explore',
        'favorite_border', 'person_outline'
    ];
    return names.map(name => (<NavIconButton key={name} name={name} />));
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
                            <NavButtons />
                        </Row>
                    </Container>
                </div>
            </nav>
        </div>
    );
}


export default Navbar;