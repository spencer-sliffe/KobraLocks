import React from 'react';
import { render, screen } from '@testing-library/react';
import App from './App';

// Test to check if the App component renders
test('renders App component', () => {
  render(<App />);
  expect(screen.getByText(/Learn More/i)).toBeInTheDocument(); // Confirm that the "Learn More" link is rendered
});

// Test to verify the typewriter effect starts typing and checks for partial text
test('starts typing the header', async () => {
  render(<App />);
  // Wait for the text part to appear using findByText which includes its own waiting mechanism
  const textElement = await screen.findByText(/Welc/i, {timeout: 3000}); // Adjust timeout according to your averageSpeed
  expect(textElement).toBeInTheDocument();
});
