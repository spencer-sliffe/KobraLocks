import React from 'react';
import { render, screen } from '@testing-library/react';
import App from './App';

// Test to check if the App component renders and dynamically added elements appear
test('renders App component and checks for dynamically visible elements', async () => {
  render(<App />);
  // Use findByText to wait for the "Learn More" link to appear after the typewriter effect
  const linkElement = await screen.findByText(/Learn More/i, { timeout: 10000 }); // Increase timeout if necessary
  expect(linkElement).toBeInTheDocument();
});
