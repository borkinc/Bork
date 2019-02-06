import React, {Component} from 'react';
import './Chats.css'
import {
    Badge,
    Collapse,
    ListGroup,
    ListGroupItem,
    Nav,
    Navbar,
    NavbarBrand,
    NavbarToggler,
    NavItem,
    NavLink
} from "reactstrap";

export default class AddGroup extends Component {

    constructor(props) {
        super(props);

        this.toggleNavbar = this.toggleNavbar.bind(this);
        this.state = {
            collapsed: true
        };
    }

    toggleNavbar() {
        this.setState({
            collapsed: !this.state.collapsed
        });
    }

    render() {
        return (
            <div>
                <Navbar color="faded" light>
                    <NavbarBrand href="/" className="mr-auto">Bork</NavbarBrand>
                    <NavbarToggler onClick={this.toggleNavbar} className="mr-2"/>
                    <Collapse isOpen={!this.state.collapsed} navbar>
                        <Nav navbar>
                            <NavItem>
                                <NavLink href="/chats/add_group">New group</NavLink>
                            </NavItem>
                            <NavItem>
                                <NavLink href="">New contact</NavLink>
                            </NavItem>
                        </Nav>
                    </Collapse>
                </Navbar>
                <ListGroup>
                    <ListGroupItem className="justify-content-between" active tag="button" action>Cras justo odio <Badge
                        pill>14</Badge></ListGroupItem>
                    <ListGroupItem className="justify-content-between" tag="button" action>Dapibus ac facilisis
                        in <Badge
                            pill>2</Badge></ListGroupItem>
                    <ListGroupItem className="justify-content-between" tag="button" action>Morbi leo risus <Badge
                        pill>1</Badge></ListGroupItem>
                </ListGroup>
            </div>
        );
    }
}
