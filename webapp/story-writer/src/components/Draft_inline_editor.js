/* eslint-disable react/no-multi-comp */
import React, { Component } from 'react';
import Editor, { createEditorStateWithText } from 'draft-js-plugins-editor';
import { EditorState, SelectionState, RichUtils } from "draft-js";
import createInlineToolbarPlugin, { Separator } from 'draft-js-inline-toolbar-plugin';
import ScrollMenu from 'react-horizontal-scrolling-menu';



import {
  ItalicButton,
  BoldButton,
  UnderlineButton,
  CodeButton,
  HeadlineOneButton,
  HeadlineTwoButton,
  HeadlineThreeButton,
  UnorderedListButton,
  OrderedListButton,
  BlockquoteButton,
  CodeBlockButton,
} from 'draft-js-buttons';


import '../../node_modules/draft-js-inline-toolbar-plugin/lib/plugin.css';
import './editorStyles.css';
import editorStyles from './editorStyles.css';








// list of items
const list = [
    {
        "word": "apiece"
    },
    {
        "word": "aris"
    },
    {
        "word": "audris"
    },
    {
        "word": "bbc's"
    },
    {
        "word": "bernice"
    },
    {
        "word": "breece"
    },
    {
        "word": "brocious"
    },
    {
        "word": "buice"
    }];


// One item component
// selected prop will be passed
const MenuItem = ({ text, selected }) => {
  return (
    <div
      className="menu-item"
    >
      {text}
    </div>
  );
};

// All items component
// Important! add unique key
export const Menu = (list) => list.map(el => {
  const { word } = el;

  return (
    <MenuItem
      text={word}
      key={word}
    />
  );
});


const Arrow = ({ text, className }) => {
  return (
    <div
      className={className}
    >{text}</div>
  );
};


const ArrowLeft = Arrow({ text: '<', className: 'arrow-prev' });
const ArrowRight = Arrow({ text: '>', className: 'arrow-next' });





let synonym = ""

class RandomSynonymPicker extends Component {

  async componentDidMount() {

    let query = selected_content.replace(" ", "+").toLowerCase();

    const url = "http://0.0.0.0:5000/api/synonym/" + query;
    const response = await fetch(url);
    const data = await response.json();
    console.log("synonym: ", data.synonym)

    synonym = data.synonym

    setTimeout(() => { window.addEventListener('click', this.onWindowClick); });
  }



  componentWillUnmount() {
    window.removeEventListener('click', this.onWindowClick);
  }

  onWindowClick = () =>
    // Call `onOverrideContent` again with `undefined`
    // so the toolbar can show its regular content again.
    this.props.onOverrideContent(undefined);

  render() {

    console.log("selected_content:", selected_content)

    var divStyle = {
      color: 'black',

    };

    return (


      <div>

        <p style={divStyle}>{synonym}</p>

      </div>
    );
  }
}

class RandomSynonymButton extends Component {
  // When using a click event inside overridden content, mouse down
  // events needs to be prevented so the focus stays in the editor
  // and the toolbar remains visible  onMouseDown = (event) => event.preventDefault()
  onMouseDown = (event) => event.preventDefault()

  onClick = () =>
    // A button can call `onOverrideContent` to replace the content
    // of the toolbar. This can be useful for displaying sub
    // menus or requesting additional information from the user.
    this.props.onOverrideContent(RandomSynonymPicker);

  render() {
    return (
      <div onMouseDown={this.onMouseDown} >
        <button onClick={this.onClick}>
          Random Synonym
        </button>
      </div>
    );
  }
}



let rhymed_words = []


class RhymedWordsPicker extends Component {

  state = {
    selected: 0
  };

  async componentDidMount() {

    let query = selected_content.toLowerCase();;

    const url = "http://0.0.0.0:5000/api/rhymed/" + query;
    const response = await fetch(url);
    rhymed_words = await response.json();

//    console.log("data: ", data)
//
//    data.forEach(function(word) {
//
//    rhymed_words.push(word.word)
//
//    });


    console.log("Rhymed Words: ", rhymed_words)

    setTimeout(() => { window.addEventListener('click', this.onWindowClick); });
  }



  componentWillUnmount() {
    window.removeEventListener('click', this.onWindowClick);
  }

  onWindowClick = () =>
    // Call `onOverrideContent` again with `undefined`
    // so the toolbar can show its regular content again.
    this.props.onOverrideContent(undefined);

  render() {

    console.log("selected_content:", selected_content)

    var divStyle = {
      color: 'black',
      width: '600px',

    };

    var rhymed_words_list = rhymed_words.map(function(word){
                        return <li>{word}</li>;
                      })



    const { selected } = this.state;
    // Create menu from items
    const menu = Menu(rhymed_words, selected);




    return (

         <div className="App" style={divStyle}>
          <ScrollMenu
          data={menu}
          selected={selected}
          onSelect={this.onSelect}
          wheel={true}
          transition={15}
        />
         </div>

    );
  }
}

class RhymedWordsButton extends Component {
  // When using a click event inside overridden content, mouse down
  // events needs to be prevented so the focus stays in the editor
  // and the toolbar remains visible  onMouseDown = (event) => event.preventDefault()
  onMouseDown = (event) => event.preventDefault()

  onClick = () =>
    // A button can call `onOverrideContent` to replace the content
    // of the toolbar. This can be useful for displaying sub
    // menus or requesting additional information from the user.
    this.props.onOverrideContent(RhymedWordsPicker);

  render() {
    return (
      <div onMouseDown={this.onMouseDown} className={editorStyles.headlineButtonWrapper} >
        <button onClick={this.onClick}  className={editorStyles.headlineButton}>
          Rhymed Words
        </button>
      </div>
    );
  }
}









const inlineToolbarPlugin = createInlineToolbarPlugin();
const { InlineToolbar } = inlineToolbarPlugin;
const plugins = [inlineToolbarPlugin];
const text = 'In this editor a toolbar shows up once you select part of the text …';


let selected_content = "";


export default class CustomInlineToolbarEditor extends Component {

  state = {
    editorState:  createEditorStateWithText(text),
    loading: true
  };


  onChange = (editorState) => {



        // The following block of code that extract selected text was by @robinmaben from this Github issue
    // https://github.com/facebook/draft-js/issues/442
    // Get block for current selection
    const selection= editorState.getSelection()
    const anchorKey = selection.getAnchorKey();
    const currentContent = editorState.getCurrentContent();
    const currentBlock = currentContent.getBlockForKey(anchorKey);

    //Then based on the docs for SelectionState -
    const start = selection.getStartOffset();
    const end = selection.getEndOffset();
    selected_content = currentBlock.getText().slice(start, end);






    this.setState({
      editorState,
    });
  };


  focus = () => {

    this.editor.focus();
  };




  render() {




    return (




      <div className={editorStyles.editor} onClick={this.focus}>


        <Editor
          editorState={this.state.editorState}
          onChange={this.onChange}
          plugins={plugins}
          ref={(element) => { this.editor = element; }}
        />
        <InlineToolbar>
          {
            // may be use React.Fragment instead of div to improve perfomance after React 16
            (externalProps) => (
              <div>
                <BoldButton {...externalProps} />
                <ItalicButton {...externalProps} />
                <UnderlineButton {...externalProps} />
                <CodeButton {...externalProps} />
                <Separator {...externalProps} />
                <RandomSynonymButton {...externalProps} />
//                <RhymedWordsButton {...externalProps} />

              </div>
            )
          }
        </InlineToolbar>
      </div>
    );
  }
}