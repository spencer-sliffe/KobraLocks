import React from 'react';
import { render, screen, waitFor } from '@testing-library/react';
import App from './App';

// Test to check if the App component renders
test('renders App component', () => {
  render(<App />);
  expect(screen.getByText(/learn more/i)).toBeInTheDocument();
});

// Test to verify typewriter effect starts typing
test('starts typing the header', async () => {
  render(<App />);
  await waitFor(() => expect(screen.getByText(/Welcome to KobraLocks/i)).toBeInTheDocument(), {
    timeout: 3000 // Adjust timeout according to your averageSpeed
  });
});
