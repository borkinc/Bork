import React, {Component} from 'react';
import './HelloWorldList.css';

import HelloWorld from './HelloWorld';
import AddGreeter from './AddGreeter';

class HelloWorldList extends Component {

    render() {
        return (
            <div className="HelloWorldList">
                <AddGreeter addGreeting={this.addGreeting}/>
                {this.renderGreetings()}
            </div>
        );
    }

    addGreeting(newName) {
        this.setState({greetings: [...this.state.greetings, newName]});
    }

    renderGreetings() {
        return this.state.greetings.map(name => (
            <HelloWorld
                key={name}
                name={name}
                removeGreeting={this.removeGreeting}
            />
        ));
    }

    removeGreeting(removeName) {
        const filteredGreetings = this.state.greetings.filter(name => {
            return name !== removeName;
        });
        this.setState({greetings: filteredGreetings});
    }

    constructor(props) {
        super(props);
        this.state = {greetings: ['Jim', 'Sally', 'Bender']};
        this.addGreeting = this.addGreeting.bind(this);
        this.removeGreeting = this.removeGreeting.bind(this);
    }
}

export default HelloWorldList;