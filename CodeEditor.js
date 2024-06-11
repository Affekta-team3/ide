import React from 'react';
import MonacoEditor from 'react-monaco-editor';

const CodeEditor = ({ language, value, onChange }) => {
  const editorDidMount = (editor) => {
    editor.onDidChangeModelContent(() => {
      onChange(editor.getValue());
    });
  };

  return (
      <MonacoEditor
          width="100%"
          height="500px"
          language={language}
          theme="vs-dark"
          value={value}
          editorDidMount={editorDidMount}
          options={{ selectOnLineNumbers: true }}
      />
  );
};

export default CodeEditor;
