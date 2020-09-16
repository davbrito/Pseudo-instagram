import React from 'react';
import { Col, Container, Row } from 'react-materialize';
import Navbar from '../navbar/Navbar';
import Post from '../post/Post';


const post = {
    love: true,
    description: "Es uno de los animales mas lindos del mundo",
    image: "https://cnnespanol.cnn.com/wp-content/uploads/2019/12/mejores-imagenes-del-ancc83o-noticias-2019-galeria10.jpg?quality=100&strip=info&w=320&h=240&crop=1"
};

const posts = [
    post, post, post, post, post, post
];

const renderPost = (post, i) => (
    <Post
        key={i}
        description={post.description}
        image={post.image}
        love={post.love}
    />
);

function PostList(props) {
    return (
        <Col s={12} m={7} >
            {posts.map(renderPost)}
        </Col>
    );
}

function ExtraContent(props) {
    return (
        <Col m={5} className="hide-on-small-only">
        </Col>
    );
}

function Content() {
    return (
        <Container>
            <Row>
                <PostList />
                <ExtraContent />
            </Row>
        </Container>
    );
}

function Home() {
    return (
        <>
            <Navbar />
            <Content />
        </>
    );
}




export default Home;