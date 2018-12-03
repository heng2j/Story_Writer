import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

import MyEditor from './components/Draft_inline_editor'
import PageContainer from './components/PageContainer'

class App extends Component {
  render() {
    return (
      <div className="App">
        <div className="headline">
          <h1>Draft.js Demo</h1>
        </div>

        <div className="pageComponents">





            	<PageContainer />


        </div>
      </div>
    );
  }
}

export default App;
