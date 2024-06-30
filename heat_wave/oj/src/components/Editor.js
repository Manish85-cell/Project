import React, { Component } from 'react'
import ReactDOM from "react-dom"


const handleSubmit = (e) => {
    e.preventDefault()
   
}


export default function Editor(props) {

      
    
    
    
    return (
        <>
            
            <div id="editor">
                <div class="editorbox">
                    <div class="editorbox2">
                        <form class="left_box">
                            <p id="heading">Two Sum</p>
                            <div class="field" id="prob_statement">
                                <p defaultValue={"Problem Statement"}>Problem Statement</p>
                                    
                                {/* <textarea type="text"  class="input-field" placeholder="Problem Statement" autocomplete="off"></textarea> */}
                            </div>
                            <div class="field" id="rest_of_part">
                                <p>Examples and constraints</p>
                            </div>
                
                        </form>
                    </div>

                </div>

                <div class="editorbox sec">
                    <div class="editorbox2">
                        <form class="left_box">
                            <p id="heading">Code Here</p>
                            <div class="field" id="prob_statement">
                                {/* code */}
                                <textarea type="text" name="code" class="input-field" placeholder="Code here" autocomplete="off" rows="20">
                               
                                </textarea>
                            </div>
                            <div class="field" id="rest_of_part">
                                <textarea class="input-field" placeholder="Test Cases">TestCases</textarea>
                            </div>
                            
                        </form>
                    </div>

                </div>
            </div>
        </>
    )
    
}