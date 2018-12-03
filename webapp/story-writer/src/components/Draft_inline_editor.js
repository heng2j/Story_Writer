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

let synonym = ""

class RandomSynonymPicker extends Component {

  async componentDidMount() {

    let query = selected_content.replace(" ", "+");

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

  async componentDidMount() {

    let query = selected_content.toLowerCase();;

    const url = "http://0.0.0.0:5000/api/rhymed/" + query;
    const response = await fetch(url);
    const data = await response.json();

    console.log("data: ", data)

    data.forEach(function(word) {

    rhymed_words.push(word.word)

    });


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

    };

    var rhymed_words_list = rhymed_words.map(function(word){
                        return <li>{word}</li>;
                      })


    return (

      <div style={divStyle}>

        <ul>{ rhymed_words_list }</ul>

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
      <div onMouseDown={this.onMouseDown} >
        <button onClick={this.onClick}>
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
    editorState: EditorState.createEmpty(),
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
      <div onClick={this.focus}>
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