import React,{Component} from 'react';
import Styles from './Searcher.module.css'

class Searcher extends Component{

    render(){
        return(
            <form className={Styles.form}>
                <input id="search-id" type="search" className={Styles.inputText} />
               
            </form>

            
        )
    }

}


export default Searcher;