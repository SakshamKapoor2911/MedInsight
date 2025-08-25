import React from 'react';
import { render } from '@testing-library/react';
import { AspectRatio } from './aspect-ratio';

describe('AspectRatio', () => {
  it('renders children', () => {
    const { getByText } = render(<AspectRatio><div>Aspect Content</div></AspectRatio>);
    expect(getByText('Aspect Content')).toBeInTheDocument();
  });
});
