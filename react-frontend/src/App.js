import React from 'react';
import './App.css';
import UserAuth from './UserAuth/UserAuth';
import {Route} from "react-router";
import Chats from "./Chats/Chats";
import AddGroup from "./Chats/AddGroup";

const App = () => {

    return (
        <div className="App">
            <Route exact path="/" component={UserAuth}/>
            <Route exact path="/chats" component={Chats}/>
            <Route exact path="/chats/add_group" component={AddGroup}/>
        </div>
    );
};


export default App;
