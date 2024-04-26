import React from 'react';
import { render, screen } from '@testing-library/react';
import App from './App';

// Test to check if the App component renders
test('renders App component', async () => {
  render(<App />);
  const linkElement = await screen.findByText(/Learn More/i);  // Using findByText to wait for the element to appear
  expect(linkElement).toBeInTheDocument();
});

// Test to verify the typewriter effect starts typing and checks for partial text
test('starts typing the header', async () => {
  render(<App />);
  const partialTextElement = await screen.findByText(/Welc/i, {timeout: 3000}); // Wait for the text part to appear
  expect(partialTextElement).toBeInTheDocument();
});
