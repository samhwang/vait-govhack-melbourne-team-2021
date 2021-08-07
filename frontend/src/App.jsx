import { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [text, setText] = useState('');

  useEffect(() => {
    fetch('http://localhost:5000/graphql', {
      method: 'POST',
      mode: 'cors',
      cache: 'no-cache',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        query: `
        query Hello {
          hello {
            success
            message
            errors
          }
        }
        `,
      }),
    })
      .then((result) => result.json())
      .then((resultData) => {
        console.log(resultData);
        setText(resultData.data.hello.message);
      })
      .catch((error) => console.error(error));
  }, []);

  return <div>{text}</div>;
}

export default App;
