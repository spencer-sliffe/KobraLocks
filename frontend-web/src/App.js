import React, { useState, useEffect } from 'react';
import './App.css';

function Typewriter({ text, averageSpeed, onTypingDone, showCursor }) {
  const [index, setIndex] = useState(0);
  const [currentText, setCurrentText] = useState('');
  const [mistakes, setMistakes] = useState(0);
  const [backspacing, setBackspacing] = useState(false);

  useEffect(() => {
    if (index === text.length && mistakes === 3) {
      onTypingDone && onTypingDone();  // Ensure typing is done only after 3 mistakes are made
      return;
    }

    const timeout = setTimeout(() => {
      if (backspacing) {
        if (currentText.length > index) {
          setCurrentText(currentText.slice(0, -1));  // Remove last character
        } else {
          setBackspacing(false);
          setMistakes(m => m + 1);
        }
      } else {
        if (index < text.length) {
          if (Math.random() < 0.1 && mistakes < 3 && !backspacing) {
            setCurrentText(currentText + '_');  // Simulate a mistake
            setBackspacing(true);
          } else {
            setCurrentText(currentText + text.charAt(index));  // Type next character
            setIndex(index + 1);
          }
        }
      }
    }, backspacing ? averageSpeed / 2 : averageSpeed);

    return () => clearTimeout(timeout);
  }, [currentText, index, backspacing, mistakes, text, averageSpeed, onTypingDone]);

  return (
    <span>
      {currentText}
      {showCursor && <span className="typewriter-cursor" style={{ opacity: 1 }}>|</span>}
    </span>
  );
}

function App() {
  const [headerCompleted, setHeaderCompleted] = useState(false);

  return (
    <div className="App">
      <a href="https://kobralocks.tech" className="static-link">kobralocks.tech</a>
      <header className="App-header">
        <h1>
          <Typewriter
            text="Welcome to KobraLocks"
            averageSpeed={120}
            onTypingDone={() => setHeaderCompleted(true)}
            showCursor={!headerCompleted}
          />
        </h1>
        {headerCompleted && (
          <div>
            <p>
              <Typewriter
                text="Your ultimate destination for sports betting insights."
                averageSpeed={100}
                showCursor={false}
                onTypingDone={() => console.log('Paragraph done')}
              />
            </p>
            <div>
              <button className="button-key" onClick={() => window.location.href = 'https://kobrastocks.tech'}>KobraStocks.tech</button>
              <button className="button-key" onClick={() => window.location.href = 'https://kobracoding.tech'}>KobraCoding.tech</button>
              <button className="button-key" onClick={() => window.location.href = '/about'}>About Kobra</button>
              <button className="button-key" onClick={() => window.location.href = '/signin'}>Sign in</button>
            </div>
          </div>
        )}
      </header>
    </div>
  );
}

export default App;
