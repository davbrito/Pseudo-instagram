import React from 'react';
import { Button, Icon } from 'react-materialize';


function PostImage(props) {
    return (
        <div className="card-image">
            <img src={props.url} alt="" />
        </div>
    );
}

function PostDescription(props) {
    return (
        <div className="card-content">
            <p>{props.text}</p>
        </div>
    );
}

function LoveButton(props) {
    const [love, setLove] = React.useState(props.love);

    const handleLove = (e) => {
        setLove(!love);
        // aquí va el código para crear el 'love' mediante la API
        e.preventDefault();
    };

    return (
        <Button className="red darken-1" style={{ marginRight: "5px" }} onClick={handleLove} >
            <Icon>{love ? "favorite" : "favorite_border"}</Icon>
        </Button>
    );
}

function CommentButton(props) {
    return (
        <Button className="light-blue darken-3" style={{ marginRight: "5px" }} >
            <Icon>comment</Icon>
        </Button>
    );
}

function MoreButton(props) {
    return (
        <Button className="gren accent-3" >
            <Icon>more_vert</Icon>
        </Button>
    );
}

function PostActions(props) {
    return (
        <div className="card-action">
            <LoveButton love={props.love} />
            <CommentButton />
            <MoreButton />
        </div>
    );
}

function Post(props) {
    return (
        <div className="card">
            <PostImage url={props.image} />
            <PostDescription text={props.description} />
            <PostActions love={props.love} />
        </div>
    );
}



export default Post;