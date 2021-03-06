import React, { Component } from 'react';  
import ReactDOM from 'react-dom';
import axios from 'axios';
import UsersList from './component/UsersList';
import AddUser from './component/AddUser';
 

class App extends Component {
    constructor() {
        super();
       // nuevo
       this.state = {
         users: [],
         username: '', // nuevo
         email: '', // nuevo
       };
       this.addUser = this.addUser.bind(this);
       this.handleChange = this.handleChange.bind(this);
    };
    addUser(event) {
      event.preventDefault();
      const data = {
        username: this.state.username,
        email: this.state.email
      };
      axios.post(`${process.env.REACT_APP_USERS_SERVICE_URL}/users`, data)
      .then((res) => { 
        this.getUsers();
        this.setState({username: '', email: ''}); 
      })
      .catch((err) => { console.log(err); });
    };
    handleChange(event) {
      const obj = {};
      obj[event.target.name] = event.target.value;
      this.setState(obj);
    };
    componentDidMount() {
      this.getUsers();
    };
    getUsers() {
        axios.get(`${process.env.REACT_APP_USERS_SERVICE_URL}/users`) 
        .then((res) =>{ this.setState({ users: res.data.data.users }); })
        .catch((err) =>{ console.log(err); });
    };         
    render() {
      return (
        <section className="section">
          <div className="container">
            <div className="columns">
              <div className="column is-half">
                <br/>
                <h1 className="title is-1">Todos los Usuarios</h1>
                <hr/><br/>
                <AddUser
                  username={this.state.username}
                  email={this.state.email}
                  addUser={this.addUser}
                  handleChange={this.handleChange}
                  /> {/* nuevo */}
                <br></br> {/* nuevo */}
                <UsersList users={this.state.users}/>
              </div>
            </div>
          </div>
        </section>
      )
    }        
};
  
ReactDOM.render(
  <App />,
  document.getElementById('root')
);


