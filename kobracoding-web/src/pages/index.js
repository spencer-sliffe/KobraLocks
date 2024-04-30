import React, { useState, useEffect } from 'react';

function Typewriter({ text, averageSpeed, onTypingDone, startDelay = 0 }) {
  const [index, setIndex] = useState(0);
  const [currentText, setCurrentText] = useState('');
  const [isTyping, setIsTyping] = useState(false);

  useEffect(() => {
    let typingTimeout;
    if (isTyping) {
      if (index < text.length) {
        typingTimeout = setTimeout(() => {
          setCurrentText(current => current + text[index]);
          setIndex(i => i + 1);
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

  return <span>{currentText}</span>;
}

const Home = () => {
  const [startParagraph, setStartParagraph] = useState(false);

  useEffect(() => {
    const paragraphDelay = setTimeout(() => {
      setStartParagraph(true);
    }, 2000); // Wait for 2 seconds before starting the paragraph

    return () => clearTimeout(paragraphDelay);
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        
        <h1>
          <Typewriter
            text="Welcome to KobraLocks"
            averageSpeed={120}
            onTypingDone={() => console.log('Header completed.')}
          />
        </h1>
        
        {startParagraph && (
          <p>
            <Typewriter
              text="Your ultimate destination for sports betting insights."
              averageSpeed={100}
              onTypingDone={() => console.log('Paragraph completed.')}
            />
          </p>
        )}

        <div>
          <button className="button-key" onClick={() => window.location.href = 'https://kobrastocks.tech'}>KobraStocks.tech</button>
          <button className="button-key" onClick={() => window.location.href = 'https://kobralocks.tech'}>KobraLocks.tech</button>
        </div>
      </header>
    </div>
  );
};

export default Home;
