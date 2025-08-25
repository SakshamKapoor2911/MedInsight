import { render, screen } from '@testing-library/react';
import { Card } from './card';

describe('Card', () => {
  it('renders children content', () => {
    render(<Card>Card Content</Card>);
    expect(screen.getByText('Card Content')).toBeInTheDocument();
  });
});
