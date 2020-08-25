import React,{Component} from 'react'
import {Button} from 'react-materialize'


class Post extends Component{

    constructor(props){
        super(props)
        this.state = {love: this.props.love}

        this.handleLove = this.handleLove.bind(this);
    }

    handleLove(e){
       this.setState(state =>({love: !this.state.love}))
       e.preventDefault();
    }

    render(){
        return(
              <div className="card">
                <div className="card-image">
                  <img src={this.props.image} alt="" />
                </div>
                <div className="card-content">
                    <p>{this.props.description}</p>
                </div>
                <div className="card-action">
                  <Button className="red darken-1"style={{marginRight: "5px"}} onClick={this.handleLove} >
                    <i className="material-icons">{ this.state.love ? "favorite" : "favorite_border"}</i>
                  </Button>
                  <Button className="light-blue darken-3" style={{marginRight: "5px"}} >
                    <i className="material-icons">comment</i>
                  </Button>
                  <Button className="gren accent-3" >
                    <i className="material-icons">more_vert</i>
                  </Button>
                </div>
              </div>
        )
    }
}


export default Post