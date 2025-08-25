import React from 'react';
import { render, screen } from '@testing-library/react';
import { SeverityIndicator } from './severity-indicator';

describe('SeverityIndicator', () => {
  it('renders with low severity', () => {
    render(<SeverityIndicator severity="low" />);
  const lows = screen.getAllByText(/low/i);
  expect(lows.length).toBeGreaterThan(0);
  });
  it('renders with moderate severity', () => {
    render(<SeverityIndicator severity="moderate" />);
  const moderates = screen.getAllByText(/moderate/i);
  expect(moderates.length).toBeGreaterThan(0);
  });
  it('renders with high severity', () => {
    render(<SeverityIndicator severity="high" />);
  const highs = screen.getAllByText(/high/i);
  expect(highs.length).toBeGreaterThan(0);
  });
});
