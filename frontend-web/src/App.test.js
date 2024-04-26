import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import Welcome from './Welcome'; // Adjust the import path according to your project structure

describe('Welcome Component', () => {
  test('renders the welcome message', () => {
    render(<Welcome />);
    const welcomeElement = screen.getByText(/welcome/i); // This regex assumes your message includes 'welcome'
    expect(welcomeElement).toBeInTheDocument();
  });
});
