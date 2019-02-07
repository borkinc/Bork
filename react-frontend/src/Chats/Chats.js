import React, {Component} from 'react';
import './Chats.css'
import {
    Badge,
    Button,
    Collapse,
    ListGroup,
    ListGroupItem,
    Modal,
    ModalBody,
    ModalFooter,
    ModalHeader,
    Nav,
    Navbar,
    NavbarBrand,
    NavbarToggler,
    NavItem
} from "reactstrap";
import axios from "axios";

export default class Chats extends Component {

    constructor(props) {
        super(props);

        this.toggleNavbar = this.toggleNavbar.bind(this);
        this.state = {
            collapsed: true,
            modal: false,
            chats: [],
            isLoading: true,
            errors: null
        };
        this.toggle = this.toggle.bind(this);
    }

    toggleNavbar() {
        this.setState({
            collapsed: !this.state.collapsed
        });
    }

    toggle() {
        this.setState(prevState => ({
            modal: !prevState.modal
        }));
    }

    componentDidMount() {
        axios
            .get("http://localhost:5000/api/chats")
            .then(response =>
                response.data.results.map(chat => ({
                    name: `${chat.chat_name}`,
                    id: `${chat.id}`,
                }))
            )
            .then(chats => {
                this.setState({
                    chats,
                    isLoading: false
                });
            })
            .catch(error => this.setState({error, isLoading: false}));
    }

    //
    //
    //
    // renderChats() {
    //     return this.state.chats.map((chat) => {
    //         return (
    //             <ListGroupItem className="justify-content-between" tag="button"
    //                            action key={chat}>{chat.chat_name}<Badge
    //                 pill>0</Badge></ListGroupItem>
    //         );
    //     })
    // }
    //
    render() {
        return (
            <div>
                <Navbar color="faded" light>
                    <NavbarBrand href="/" className="mr-auto">Bork</NavbarBrand>
                    <NavbarToggler onClick={this.toggleNavbar} className="mr-2"/>
                    <Collapse isOpen={!this.state.collapsed} navbar>
                        <Nav navbar>
                            <NavItem>
                                <Button color="link" onClick={this.toggle}>New group</Button>
                                <Modal isOpen={this.state.modal} toggle={this.toggle} className={this.props.className}>
                                    <ModalHeader toggle={this.toggle}>Modal title</ModalHeader>
                                    <ModalBody>
                                        Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor
                                        incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
                                        nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
                                        Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu
                                        fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
                                        culpa qui officia deserunt mollit anim id est laborum.
                                    </ModalBody>
                                    <ModalFooter>
                                        <Button color="primary" onClick={this.toggle}>Do Something</Button>{' '}
                                        <Button color="secondary" onClick={this.toggle}>Cancel</Button>
                                    </ModalFooter>
                                </Modal>
                            </NavItem>
                            <NavItem>
                                <Button color="link" onClick={this.toggle}>New contact</Button>
                                <Modal isOpen={this.state.modal} toggle={this.toggle} className={this.props.className}>
                                    <ModalHeader toggle={this.toggle}>Modal title</ModalHeader>
                                    <ModalBody>
                                        Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor
                                        incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
                                        nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
                                        Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu
                                        fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
                                        culpa qui officia deserunt mollit anim id est laborum.
                                    </ModalBody>
                                    <ModalFooter>
                                        <Button color="primary" onClick={this.toggle}>Do Something</Button>{' '}
                                        <Button color="secondary" onClick={this.toggle}>Cancel</Button>
                                    </ModalFooter>
                                </Modal>
                            </NavItem>
                        </Nav>
                    </Collapse>
                </Navbar>
                <ListGroup>
                    {!this.state.isLoading ? (
                        this.state.chats.map(chat => {
                            return (<ListGroupItem className="justify-content-between" tag="button"
                                                   action key={chat.id}>{chat.name}<Badge
                                pill>0</Badge></ListGroupItem>);
                        })
                    ) : (<p>Loading......</p>)}
                    {/*{this.renderChats()}*/}
                    {/*{this.state.chats.map((item) => (*/}
                    {/*<ListGroupItem className="justify-content-between" active tag="button"*/}
                    {/*action>{item.chat_name}<Badge*/}
                    {/*pill>0</Badge></ListGroupItem>))}*/}
                    {/*{this.state.chats.map((item) => ({*/}
                    {/*const {chat_name} = chat;*/}
                    {/*return (*/}

                    {/*)*/}
                    {/*}))}*/}
                    {/*<ListGroupItem className="justify-content-between" active tag="button" action>Cras justo odio <Badge*/}
                    {/*pill>14</Badge></ListGroupItem>*/}
                    {/*<ListGroupItem className="justify-content-between" tag="button" action>Dapibus ac facilisis*/}
                    {/*in <Badge*/}
                    {/*pill>2</Badge></ListGroupItem>*/}
                    {/*<ListGroupItem className="justify-content-between" tag="button" action>Morbi leo risus <Badge*/}
                    {/*pill>1</Badge></ListGroupItem>*/}
                </ListGroup>
            </div>
        );
    }

}
