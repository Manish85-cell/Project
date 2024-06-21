import React, { Component } from "react"                               
import ReactDOM from "react-dom"                                    
import HomePage from "./HomePage"                                                            
import Problem from "./Problem"
import Contest from "./Contest"
import Navbar from "./Navbar"
import '../../static/css/index';

export default class App extends Component {                          
    constructor(props){                                            
        super(props);  
                                      
    }                                                            
                                                                
    render(){                                                     
        return <>  
            <Navbar/>    
            <HomePage />
        </>;     
    }                                               
}                                                          
                                                                   
const appDiv = document.getElementById("app");
const root = ReactDOM.createRoot(appDiv)      
root.render (<App/>)                          