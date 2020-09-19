import React from 'react';
import { Col, Container, Row } from 'react-materialize';
import Navbar from '../navbar/Navbar';
import Post from '../post/Post';


const post = {
    love: true,
    description: "Es uno de los animales mas lindos del mundo",
    image: "https://cnnespanol.cnn.com/wp-content/uploads/2019/12/mejores-imagenes-del-ancc83o-noticias-2019-galeria10.jpg?quality=100&strip=info&w=320&h=240&crop=1"
};
const base_api_url = 'http://localhost:8000';
const posts_url = `${base_api_url}/posts/?format=json`;



const renderPost = (post) => (
    <Post
        key={post.id}
        description={post.description}
        image={post.image}
        love={post.love}
    />
);

function usePostList() {
    const [postList, setPostList] = React.useState([]);
    React.useEffect(() => {
        fetch(posts_url)
            .then(response => {
                console.log(response);
                return response.json();
            })
            .then(data => {
                console.log('data: ', data);
                console.log(typeof data.results);
                setPostList(prevPostList => [prevPostList, ...data.results]);
                console.log(data);
            })
            .catch(err => setPostList([post]));
    }, []);
    return postList;
}

function PostList(props) {
    const postList = usePostList();
    return (
        <Col s={12} m={7} >
            {postList.map(renderPost)}
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