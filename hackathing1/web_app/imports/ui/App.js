import React, { Component } from 'react';
  
// App component - represents the whole app
export default class App extends Component {

  constructor(props) {
    super(props);
    this.state = {value: '', sentiment: ''};

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({value: event.target.value});
  }

  handleSubmit(event) {
    event.preventDefault()
    console.log('A name was submitted: ' + this.state.value);
  }
 
  render() {
    return (
      <form onSubmit={this.handleSubmit} className="container">
        <header>
          <h1>Enter your phrase below!</h1>
        </header>
        <ul>
          <div>
            <input id="search" placeholder="Your phrase" value={this.state.value} onChange={this.handleChange}/>
          </div>
          <div>
            <button id="submit" placeholder="Submit" onSubmit={this.handleSubmit}> Search </button>
          </div>
          <div id="result">
            {this.state.sentiment}
          </div>
        </ul>
      </form>
    );
  }
}





