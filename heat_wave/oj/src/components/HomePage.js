import React , { Component } from 'react'
import Problem from "./Problem"
import Contest from "./Contest"
// import Login from "./Login"
// import Signup from "./Signup"
import {BrowserRouter as Router,  Routes,Route, Link, Redirect} from "react-router-dom"
// import Navbar from "./Navbar"
import '../../static/css/index';

 export default class HomePage extends Component {
    constructor(props){
        super(props);
    }

    render(){
        return (<div className='main_content'>
        <Router>
            <Routes>
                <Route path='/oj/' element={<h1>This is the home page</h1>} />
                <Route path='/oj/contests' element={<Contest />}/>
                <Route path='/oj/problems' element={<Problem/>}/>
                {/* <Route path='/oj/login' element={<Login/>}/> */}
                {/* <Route path='/oj/signup' element={<Signup/>}/> */}
                
                {/* <Route path='/oj/*' element={<Navbar/>}/> */}
            </Routes>
        </Router>
        </div>
        );
    }
 }
