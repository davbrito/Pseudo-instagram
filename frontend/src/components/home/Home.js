import React,{Component} from 'react';
import {Container, Row, Col} from 'react-materialize'
import Styles from './Home.module.css'
import Navbar from '../navbar/Navbar'
import Post from '../post/Post'


const post ={love: true,
            description: "Es uno de los animales mas lindos del mundo",
            image: "https://cnnespanol.cnn.com/wp-content/uploads/2019/12/mejores-imagenes-del-ancc83o-noticias-2019-galeria10.jpg?quality=100&strip=info&w=320&h=240&crop=1"
        }

class Home extends Component{

    render(){
        return(
            <>
            <Navbar/>
            <Container>
                <Row>
                    <Col s="12" m="7" >
                        <Post description={post.description} image={post.image}/>
                        <Post description={post.description} image={post.image}/>
                        <Post description={post.description} image={post.image}/>
                        <Post description={post.description} image={post.image}/>
                        <Post description={post.description} image={post.image}/>
                        <Post description={post.description} image={post.image}/>
                    </Col>
                    <Col m="5" className="hide-on-small-only">
                    </Col>
                </Row>
            </Container>
            </>
        )
        
    }

}


export default Home;