import React from 'react';
import { Col, Container, Row } from 'react-materialize';
import Post from '../post/Post';


const fakePost = {
    id: 15,
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
                if (!response || !response.ok)
                    return [fakePost];
                return response.json().results;
            })
            .catch(() => [fakePost])
            .then(postList => {
                setPostList(prevPostList => [...prevPostList, ...postList]);
            });


    }, []);
    return postList;
}

function PostList(props) {
    const postList = usePostList();
    const loading = postList.length === 0;
    return (
        <>
            {postList.map(renderPost)}
            {loading && <p>Loading posts...</p>}
        </>
    );
}

function ExtraContent(props) {
    return (null);
}

function Content() {
    return (
        <Row>
            <Col s={12} m={7} >
                <PostList />
            </Col>
            <Col m={5} className="hide-on-small-only">
                <ExtraContent />
            </Col>
        </Row>
    );
}

function Home() {
    return (
        <Container>
            <Content />
        </Container>
    );
}




export default Home;