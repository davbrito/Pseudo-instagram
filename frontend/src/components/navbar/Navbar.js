import React from 'react';
import { Col, Container, Icon, Row } from 'react-materialize';
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
            <input
                id="searcher"
                className={Styles.searcher}
                type="search"
                placeholder="Search"
                value={value}
                onChange={handleChange}
            />
            <label htmlFor="searcher"><Icon className={Styles.searchIcon}>search</Icon></label>
            <div onClick={handleClose}>
                <Icon className={Styles.navIcon + ' ' + Styles.searchClose}>close</Icon>
            </div>
        </Col>
    );

}

function NavIconButton(props) {
    return (
        <Col s={2} m={1} align="center" className={Styles.navIcon}>
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