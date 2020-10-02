import React, { useRef, useState } from 'react';
import { Col, Container, Icon, Row } from 'react-materialize';
import { NavLink } from 'react-router-dom';
import { useAuthUser } from '../../auth';
import Styles from './Navbar.module.css';

function Title() {
    return (
        <Col s={2}>
            <NavLink to="/home" className={Styles.Logo}>
                Pseudo
            </NavLink>
        </Col>
    );
}

function Search(props) {
    const [query, setQuery] = useState('');
    const searcherEl = useRef(null);

    const handleResetClick = () => {
        setQuery('');
        searcherEl.current.focus();
    };

    const handleChange = (event) => {
        setQuery(event.target.value);
    };

    // const handleSubmit = (event) => {
    //     //
    //     event.preventDefault();
    // };

    return (
        <Col m={5} className="hide-on-small-only" style={{ position: "relative" }}>
            <input id="searcher"
                ref={searcherEl}
                className={Styles.searcher}
                type="search"
                placeholder="Search"
                value={query}
                onChange={handleChange} />
            <label htmlFor="searcher"><Icon className={Styles.searchIcon}>search</Icon></label>
            <button type="reset" onClick={handleResetClick} className={Styles.searchClose}>
                close
            </button>
        </Col>
    );

}

function NavIconButton({ name, to, children, title }) {
    return (
        <Col s={2} m={1} align="center">
            <NavLink to={to} className={Styles.navIcon} activeClassName={Styles.activeNav} title={title}>
                <Icon>{name}</Icon>
                {children}
            </NavLink>
        </Col>
    );
}

function NavButtons(props) {
    const user = useAuthUser();
    return (
        <>
            <NavIconButton name="home" to={"/home"} />
            <NavIconButton name="inbox" to="/inbox" />
            <NavIconButton name="explore" to="/explore" />
            {user &&
                <>
                    <NavIconButton title={user.username} name="person_outline" to={'/users/' + user.username} />
                    <NavIconButton title="Log out" name="logout" to="logout" />
                </>
            }
        </>
    );
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