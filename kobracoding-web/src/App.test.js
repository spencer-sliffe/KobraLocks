import React from 'react';
import { render, screen } from '@testing-library/react';
import App from './App';

// Test to check if the App component renders and immediately available elements are present
test('renders App component and checks for immediately visible elements', () => {
  render(<App />);
  // Assuming there's a static footer or logo with text "Kobra Locks" that's always visible
  const staticElement = screen.getByText(/kobracoding.tech/i);
  expect(staticElement).toBeInTheDocument();
});
