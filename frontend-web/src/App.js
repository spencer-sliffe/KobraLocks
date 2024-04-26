import React, { useState, useEffect } from 'react';
import './App.css';

const Typewriter = ({ text, averageSpeed = 100, onTypingDone, showCursor }) => {
  const [content, setContent] = useState('');
  const [mistakeCount, setMistakeCount] = useState(0);
  const [totalMistakesMade, setTotalMistakesMade] = useState(0);
  const [isTyping, setIsTyping] = useState(true);
  const [blink, setBlink] = useState(true);
  const textArray = text.split('');
  const [currentArray, setCurrentArray] = useState([]);

  useEffect(() => {
    let timer;

    // Decide whether to type next character, make a mistake, or backspace
    const typeCharacter = () => {
      if (currentArray.length < textArray.length && isTyping) {
        // Randomly decide to make a mistake if no mistake is currently happening
        if (totalMistakesMade < 3 && Math.random() < 0.1) {
          setCurrentArray((prev) => prev.concat('_')); // Append a placeholder to represent a mistake
          setIsTyping(false); // Start backspacing in the next intervals
        } else {
          setCurrentArray((prev) => prev.concat(textArray[currentArray.length]));
        }
      }
    };

    // Correct the mistake by backspacing
    const backspaceCharacter = () => {
      if (!isTyping) {
        if (mistakeCount < 3) {
          setCurrentArray((prev) => prev.slice(0, prev.length - 1));
          setMistakeCount((prev) => prev + 1);
        } else {
          setIsTyping(true); // Done backspacing, resume typing
          setMistakeCount(0); // Reset mistake characters count
          setTotalMistakesMade((prev) => prev + 1); // Increment the total number of mistakes made
        }
      }
    };

    if (currentArray.length === textArray.length && totalMistakesMade === 3) {
      onTypingDone(); // Notify when typing is done
    } else {
      timer = setTimeout(() => {
        if (isTyping) {
          typeCharacter();
        } else {
          backspaceCharacter();
        }
      }, averageSpeed);
    }

    return () => clearTimeout(timer);
  }, [currentArray, textArray, isTyping, mistakeCount, totalMistakesMade, onTypingDone]);

  useEffect(() => {
    const blinkInterval = setInterval(() => {
      setBlink(prev => !prev);
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
