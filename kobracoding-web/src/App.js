import React, { useState, useEffect } from 'react';
import './App.css';

function Typewriter({ text, averageSpeed, onTypingDone, startDelay = 0 }) {
  const [index, setIndex] = useState(0);
  const [currentText, setCurrentText] = useState('');
  const [isTyping, setIsTyping] = useState(false);

  useEffect(() => {
    let typingTimeout;
    if (isTyping) {
      if (index < text.length) {
        typingTimeout = setTimeout(() => {
          setCurrentText((current) => current + text[index]);
          setIndex((i) => i + 1);
          if (index === text.length - 1) {
            onTypingDone && onTypingDone();
          }
        }, averageSpeed);
      }
    } else {
      const startTypingTimeout = setTimeout(() => {
        setIsTyping(true);
      }, startDelay);

      return () => clearTimeout(startTypingTimeout);
    }

    return () => clearTimeout(typingTimeout);
  }, [index, text, averageSpeed, onTypingDone, isTyping, startDelay]);

  return (
    <span>{currentText}</span>
  );
}

function App() {
  const [startParagraph, setStartParagraph] = useState(false);

  // Start typing the paragraph after a delay
  useEffect(() => {
    const paragraphDelay = setTimeout(() => {
      setStartParagraph(true);
    }, 2000); // Wait for 2 seconds before starting the paragraph

    return () => clearTimeout(paragraphDelay);
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        {/* Static link at the top left corner */}
        <a href="https://kobracoding.tech" className="static-link">kobracoding.tech</a>
        
        <h1>
          {/* Typewriter for the header */}
          <Typewriter
            text="Welcome to Kobra"
            averageSpeed={120}
            onTypingDone={() => console.log('Header completed.')}
          />
        </h1>
        
        {startParagraph && (
          <p>
            {/* Typewriter for the paragraph */}
            <Typewriter
              text="Your ultimate destination for machine-learning aided financial gain."
              averageSpeed={100}
              onTypingDone={() => console.log('Paragraph completed.')}
            />
          </p>
        )}
              <div>
              <button className="button-key" onClick={() => window.location.href = 'https://kobrastocks.tech'}>KobraStocks.tech</button>
              <button className="button-key" onClick={() => window.location.href = 'https://kobralocks.tech'}>KobraLocks.tech</button>
              <button className="button-key" onClick={() => window.location.href = '/about'}>About Kobra</button>
              <button className="button-key" onClick={() => window.location.href = '/signin'}>Sign in</button>
            </div>
      </header>

    </div>
  );
}

export default App;
