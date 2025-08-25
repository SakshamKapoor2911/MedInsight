import React from 'react';
import { render } from '@testing-library/react';
import { Avatar } from './avatar';

describe('Avatar', () => {
  it('renders with default props', () => {
    const { container } = render(<Avatar />);
    expect(container.firstChild).toBeInTheDocument();
  });
});
