beforeAll(() => {
  Object.defineProperty(window, 'matchMedia', {
    writable: true,
    value: jest.fn().mockImplementation(query => ({
      matches: false,
      media: query,
      onchange: null,
      addListener: jest.fn(),
      removeListener: jest.fn(),
      addEventListener: jest.fn(),
      removeEventListener: jest.fn(),
      dispatchEvent: jest.fn(),
    })),
  });
});
import React from 'react';
import { render } from '@testing-library/react';
import { ThemeProvider } from './theme-provider';

describe('ThemeProvider', () => {
  it('renders children', () => {
    const { getByText } = render(
      <ThemeProvider>
        <div>Theme Content</div>
      </ThemeProvider>
    );
    expect(getByText('Theme Content')).toBeInTheDocument();
  });
});
