import React from 'react'
import Button from 'react-bootstrap/Button';
import {Navbar, Nav} from 'react-bootstrap/'
import {Container, Row, Col} from 'react-bootstrap/';

export default class TimelineHome extends React.Component {
    render() {
        return(
            <div className="App">
            <Navbar bg="dark" className="ml-auto">
                <Navbar.Collapse className="justify-content-end">
                    <Button variant="outline-light" href="/home" size="sm">
                      Login
                    </Button>
                    <Button variant="dark" size="sm">
                      Sign Up
                    </Button>
                </Navbar.Collapse>
            </Navbar>
              <header className="App-header">
                <h1 className = "logo-home">
                  revibe
                </h1>
              </header>
          </div>
        );
    }
}