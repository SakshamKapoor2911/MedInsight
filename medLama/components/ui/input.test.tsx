import { render, screen } from '@testing-library/react';
import { Input } from './input';

describe('Input', () => {
  it('renders input element', () => {
    render(<Input placeholder="Type here" />);
    expect(screen.getByPlaceholderText('Type here')).toBeInTheDocument();
  });
});
