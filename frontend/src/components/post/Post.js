import React from 'react';
import { Button } from 'react-materialize';


function PostImage(props) {
    return (
        <div className="card-image">
            <img src={props.url} alt="" />
        </div>
    )
}

function PostDescription(props) {
    return (
        <div className="card-content">
            <p>{props.text}</p>
        </div>
    )
}

class LoveButton extends React.Component {
    constructor(props) {
        super(props)
        this.state = { love: this.props.love }
        this.handleLove = this.handleLove.bind(this)
    }

    handleLove(e) {
        this.setState(state => ({ love: !state.love }))
        e.preventDefault()
    }

    render() {
        return (
            <Button className="red darken-1" style={{ marginRight: "5px" }} onClick={this.handleLove} >
                <i className="material-icons">{this.state.love ? "favorite" : "favorite_border"}</i>
            </Button>
        )
    }
}

function CommentButton(props) {
    return (
        <Button className="light-blue darken-3" style={{ marginRight: "5px" }} >
            <i className="material-icons">comment</i>
        </Button>
    )
}

function MoreButton(props) {
    return (
        <Button className="gren accent-3" >
            <i className="material-icons">more_vert</i>
        </Button>
    )
}

function PostActions(props) {
    return (
        <div className="card-action">
            <LoveButton love={props.love} />
            <CommentButton />
            <MoreButton />
        </div>
    )
}

function Post(props) {
    return (
        <div className="card">
            <PostImage url={props.image} />
            <PostDescription text={props.description} />
            <PostActions love={props.love} />
        </div>
    )
}



export default Post