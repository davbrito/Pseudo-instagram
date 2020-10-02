import React from 'react';
import { Col, Row } from 'react-materialize';
import { timelineUrl } from '../../api/endpoints';
import { authFetch } from '../../auth';
import Post from '../post/Post';

const fakePost = {
    id: 15,
    love: true,
    description: "Es uno de los animales mas lindos del mundo",
    image: "https://cnnespanol.cnn.com/wp-content/uploads/2019/12/mejores-imagenes-del-ancc83o-noticias-2019-galeria10.jpg?quality=100&strip=info&w=320&h=240&crop=1"
};


function useTimelinePostList() {
    const [postList, setPostList] = React.useState([]);

    React.useEffect(() => {
        authFetch(timelineUrl)
            .then(response => {
                if (!response || !response.ok)
                    return [fakePost];
                return response.json().then(data => {
                    console.log(data);
                    return data.results;
                });
            })
            .then(postList => {
                setPostList(prevPostList => [...prevPostList, ...postList]);
            })
            .catch(() => [fakePost]);


    }, []);
    return postList;
}

function PostList(props) {
    const postList = useTimelinePostList();
    const loading = postList.length === 0;
    return (
        <>
            {postList.map((post) => (
                <Post
                    key={post.id}
                    description={post.description}
                    image={post.image}
                    love={post.love}
                />
            ))}
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
        <Content />
    );
}




export default Home;