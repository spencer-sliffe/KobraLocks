import React from 'react';
import { render, screen } from '@testing-library/react';
import App from './App';

// Test to check if the App component renders
test('renders App component', async () => {
  render(<App />);
  // Use findByText to handle asynchronous loading of text due to the typewriter effect.
  // We wait for "Learn More" which is part of a link that should appear after the typewriter effect completes.
  // This might need a longer timeout depending on how your typewriter effect is implemented.
  const linkElement = await screen.findByText(/Learn More/i, { timeout: 10000 });
  expect(linkElement).toBeInTheDocument();
});

// Test to verify the typewriter effect starts typing and checks for initial text
test('starts typing the header', async () => {
  render(<App />);
  // Here we look for the initial part of the typewriter text to verify that typing starts.
  // We use "Welc" because it's part of "Welcome to KobraLocks" that should appear first.
  const partialTextElement = await screen.findByText(/Welc/i, { timeout: 3000 }); // Adjust timeout according to your averageSpeed
  expect(partialTextElement).toBeInTheDocument();
});
