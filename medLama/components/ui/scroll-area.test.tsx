import React from 'react';
import { render } from '@testing-library/react';
import { ScrollArea } from './scroll-area';

describe('ScrollArea', () => {
  it('renders children', () => {
    const { getByText } = render(<ScrollArea><div>Scroll Content</div></ScrollArea>);
    expect(getByText('Scroll Content')).toBeInTheDocument();
  });
});
