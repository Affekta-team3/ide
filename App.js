import React, { useState } from 'react';
import CodeEditor from './CodeEditor';

const App = () => {
    const [code, setCode] = useState('// write your code here');
    const [output, setOutput] = useState('');

    const handleCodeChange = (newCode) => {
        setCode(newCode);
    };

    const executeCode = async () => {
        const response = await fetch('http://localhost:5000/execute', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ code }),
        });

        const result = await response.json();
        setOutput(JSON.stringify(result, null, 2));
    };

    return (
        <div className="App">
            <CodeEditor language="javascript" value={code} onChange={handleCodeChange} />
            <button onClick={executeCode}>Execute</button>
            <pre>{output}</pre>
        </div>
    );
};

export default App;



