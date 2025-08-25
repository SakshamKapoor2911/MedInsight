import React from 'react';
import { render, screen } from '@testing-library/react';
import { Alert } from './alert';

describe('Alert', () => {
  it('renders with children', () => {
    render(<Alert>Test Alert</Alert>);
    expect(screen.getByText('Test Alert')).toBeInTheDocument();
  });
  it('renders with custom className', () => {
    render(<Alert className="custom">Custom</Alert>);
    expect(screen.getByText('Custom')).toHaveClass('custom');
  });
});
