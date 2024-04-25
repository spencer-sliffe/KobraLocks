import { render, screen } from '@testing-library/react';
import App from './App';

test('renders welcome message', () => {
  render(<App />);
  const headerElement = screen.getByText(/Welcome to KobraLocks/i);
  expect(headerElement).toBeInTheDocument();
});

test('renders learn more link', () => {
  render(<App />);
  const linkElement = screen.getByText(/learn more/i);
  expect(linkElement).toBeInTheDocument();
});
