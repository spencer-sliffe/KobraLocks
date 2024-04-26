import React, { useState, useEffect } from 'react';
import './App.css';

const Typewriter = ({ text, averageSpeed, onTypingDone, showCursor }) => {
  const [mistakeCount, setMistakeCount] = useState(0);
  const [totalMistakesMade, setTotalMistakesMade] = useState(0);
  const [isTyping, setIsTyping] = useState(true);
  const [blink, setBlink] = useState(true);
  const textArray = text.split('');
  const [currentArray, setCurrentArray] = useState([]);

  useEffect(() => {
    let timer;

    const typeCharacter = () => {
      if (currentArray.length < textArray.length && isTyping) {
        if (Math.random() < 0.1 && totalMistakesMade < 3) {
          // Simulate a mistake
          setCurrentArray((prev) => prev.concat('_'));
          setIsTyping(false);
        } else {
          setCurrentArray((prev) => prev.concat(textArray[currentArray.length]));
        }
      }
    };

    const backspaceCharacter = () => {
      if (!isTyping) {
        if (mistakeCount < 3) {
          setCurrentArray((prev) => prev.slice(0, prev.length - 1));
          setMistakeCount((prev) => prev + 1);
        } else {
          // End mistake sequence
          setIsTyping(true);
          setMistakeCount(0);
          setTotalMistakesMade((prev) => prev + 1);
        }
      }
    };

    timer = setTimeout(() => {
      if (currentArray.length === textArray.length && totalMistakesMade === 3) {
        onTypingDone(); // Typing complete
      } else {
        if (isTyping) {
          typeCharacter();
        } else {
          backspaceCharacter();
        }
      }
    }, averageSpeed);

    return () => clearTimeout(timer);
  }, [currentArray, isTyping, mistakeCount, totalMistakesMade, onTypingDone]);

  useEffect(() => {
    const blinkInterval = setInterval(() => {
      setBlink((prev) => !prev);
    }, 500);

    return () => clearInterval(blinkInterval);
  }, []);

  return (
    <span>
      {currentArray.join('')}
      {showCursor && <span className="typewriter-cursor" style={{ opacity: blink ? 1 : 0 }}>|</span>}
    </span>
  );
};

function App() {
  const [headerCompleted, setHeaderCompleted] = useState(false);

  return (
    <div className="App">
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
          <p>
            <Typewriter
              text="Your ultimate destination for sports betting insights."
              averageSpeed={100}
              showCursor={false}
              onTypingDone={() => {}}
            />
          </p>
        )}
        <a
          className="App-link"
          href="https://kobralocks.tech"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn More
        </a>
      </header>
    </div>
  );
}

export default App;
