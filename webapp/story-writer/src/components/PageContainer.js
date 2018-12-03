import React from "react";
import { EditorState, RichUtils } from "draft-js";
import Editor from "draft-js-plugins-editor";
import createHighlightPlugin from './plugins/highlightPlugin';

import createInlineToolbarPlugin from 'draft-js-inline-toolbar-plugin';





// Creates an Instance. At this step, a configuration object can be passed in
// as an argument.
const inlineToolbarPlugin = createInlineToolbarPlugin();

const highlightPlugin = createHighlightPlugin();

class PageContainer extends React.Component {




	constructor(props) {
		super(props);
		this.state = {
			editorState: EditorState.createEmpty()
		};


          this.plugins = [
           highlightPlugin,
           inlineToolbarPlugin
          ];
	}

	onChange = editorState => {
		this.setState({
			editorState
		});
	};

	handleKeyCommand = command => {
		const newState = RichUtils.handleKeyCommand(
			this.state.editorState,
			command
		);
		if (newState) {
			this.onChange(newState);
			return "handled";
		}
		return "not-handled";
	};

	onUnderlineClick = () => {
		this.onChange(
			RichUtils.toggleInlineStyle(this.state.editorState, "UNDERLINE")
		);
	};

	onBoldClick = () => {
		this.onChange(RichUtils.toggleInlineStyle(this.state.editorState, "BOLD"));
	};

	onItalicClick = () => {
		this.onChange(
			RichUtils.toggleInlineStyle(this.state.editorState, "ITALIC")
		);
	};

	onHighlight = () => {
   this.onChange(RichUtils.toggleInlineStyle(this.state.editorState, 'HIGHLIGHT'))
    };



	render() {
		return (
			<div className="editorContainer">
				<button onClick={this.onUnderlineClick}>U</button>
				<button onClick={this.onBoldClick}>
					<b>B</b>
				</button>
				<button onClick={this.onItalicClick}>
					<em>I</em>
				</button>
				<button className="highlight" onClick={this.onHighlight}>
                  <span style={{ background: "yellow" }}>H</span>
                </button>
				<div className="editors">
					<Editor
						editorState={this.state.editorState}
						handleKeyCommand={this.handleKeyCommand}
						onChange={this.onChange}
						plugins={this.plugins}
					/>
				</div>
			</div>
		);
	}
}

export default PageContainer;
