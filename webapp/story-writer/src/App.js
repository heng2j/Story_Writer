import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

import CustomInlineToolbarEditor from './components/Draft_inline_editor'
import PageContainer from './components/PageContainer'

class App extends Component {
  render() {
    return (
      <div className="App">

        <div className="pageComponents">

            	<CustomInlineToolbarEditor />


        </div>
      </div>
    );
  }
}

export default App;
