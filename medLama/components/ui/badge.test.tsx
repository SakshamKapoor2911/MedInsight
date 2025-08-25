import React from 'react';
import { render } from '@testing-library/react';
import { Badge } from './badge';

describe('Badge', () => {
  it('renders with children', () => {
    const { getByText } = render(<Badge>Badge Text</Badge>);
    expect(getByText('Badge Text')).toBeInTheDocument();
  });
});
