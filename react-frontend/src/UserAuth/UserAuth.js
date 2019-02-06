import React, {Component} from 'react';
import './UserAuth.css';
import {Button, Col, Form, FormGroup, Input, Label, Nav, NavItem, NavLink, Row, TabContent, TabPane} from "reactstrap";
import axios from 'axios';
import classnames from 'classnames';
import dog from '../img/dog.svg';

export default class UserAuth extends Component {

    constructor(props) {
        super(props);
        this.toggle = this.toggle.bind(this);
        this.state = {
            activeTab: '1',
            username: '',
            email: '',
            password: ''
        };
    }

    toggle(tab) {
        if (this.state.activeTab !== tab) {
            this.setState({
                activeTab: tab
            });
        }
    }

    handleUsernameChange = event => {
        this.setState({username: event.target.value});
    };

    handlePasswordChange = event => {
        this.setState({password: event.target.value});
    };

    handleEmailChange = event => {
        this.setState({email: event.target.value});
    };

    handleLoginSubmit = event => {
        event.preventDefault();

        // Creating form to be sent to API
        const data = new FormData();
        data.append('username', this.state.username);
        data.append('password', this.state.password);

        // Contacting API to validate user password
        axios.post(`http://localhost:5000/api/login`, data, {
            headers: {'Content-Type': 'application/json',}
        })
            .then(res => {
                if (res.data["is_authenticated"]) {
                    localStorage.setItem('user', JSON.stringify(res.data["user"]));
                    this.props.history.push("/chats")
                }
                // console.log(res);
                // console.log(res.data);
            })
    };

    handleSignUpSubmit = event => {
        event.preventDefault();

        // Creating form to be sent to API
        const data = new FormData();
        data.append('username', this.state.username);
        data.append('email', this.state.email);
        data.append('password', this.state.password);

        // Contacting api to add new user
        axios.post(`http://localhost:5000/api/register`, data, {
            headers: {'Content-Type': 'application/json',}
        })
            .then(res => {
                console.log(res);
                console.log(res.data);
            })
    };


    render() {
        return (
            <div className="UserAuth-logo">
                <img src={dog} className="UserAuth-logo" alt=""/>
                <div className="UserAuth-tabs">
                    <Nav tabs>
                        <NavItem>
                            <NavLink
                                className={classnames({active: this.state.activeTab === '1'})}
                                onClick={() => {
                                    this.toggle('1');
                                }}
                            >
                                Login
                            </NavLink>
                        </NavItem>
                        <NavItem>
                            <NavLink
                                className={classnames({active: this.state.activeTab === '2'})}
                                onClick={() => {
                                    this.toggle('2');
                                }}
                            >
                                Sign-Up
                            </NavLink>
                        </NavItem>
                    </Nav>
                    <TabContent activeTab={this.state.activeTab}>
                        <TabPane tabId="1">
                            <Row>
                                <Col sm="12">
                                    <div className="bork-logo">
                                        <div className="UserAuth">
                                            <Form onSubmit={this.handleLoginSubmit} className="login">
                                                <FormGroup>
                                                    <Label for="username">Username</Label>
                                                    <Input
                                                        type="username"
                                                        name="username"
                                                        id="UserAuth-username"
                                                        placeholder="Enter username"
                                                        onChange={this.handleUsernameChange}
                                                    />
                                                </FormGroup>
                                                <FormGroup>
                                                    <Label for="examplePassword">Password</Label>
                                                    <Input
                                                        type="password"
                                                        name="password"
                                                        id="UserAuth-password"
                                                        placeholder="Enter password"
                                                        onChange={this.handlePasswordChange}
                                                    />
                                                </FormGroup>
                                                <Button>Login</Button>
                                            </Form>
                                        </div>
                                    </div>
                                </Col>
                            </Row>
                        </TabPane>
                        <TabPane tabId="2">
                            <Row>
                                <Col sm="12">
                                    <div className="bork-logo">
                                        <div className="UserAuth">
                                            <Form onSubmit={this.handleSignUpSubmit} className="sign-up">
                                                <FormGroup>
                                                    <Label for="username">Username</Label>
                                                    <Input
                                                        type="username"
                                                        name="username"
                                                        id="UserAuth-username"
                                                        placeholder="Enter username"
                                                        onChange={this.handleUsernameChange}
                                                    />
                                                </FormGroup>
                                                <FormGroup>
                                                    <Label for="email">Email</Label>
                                                    <Input
                                                        type="email"
                                                        name="email"
                                                        id="UserAuth-email"
                                                        placeholder="Enter email"
                                                        onChange={this.handleEmailChange}
                                                    />
                                                </FormGroup>
                                                <FormGroup>
                                                    <Label for="examplePassword">Password</Label>
                                                    <Input
                                                        type="password"
                                                        name="password"
                                                        id="UserAuth-password"
                                                        placeholder="Enter password"
                                                        onChange={this.handlePasswordChange}
                                                    />
                                                </FormGroup>
                                                <Button>Sign-Up</Button>
                                            </Form>
                                        </div>
                                    </div>
                                </Col>
                            </Row>
                        </TabPane>
                    </TabContent>
                </div>
            </div>
        );
    }
}
