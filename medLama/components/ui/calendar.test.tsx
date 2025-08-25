import React from 'react';
import { render } from '@testing-library/react';
import { Calendar } from './calendar';

describe('Calendar', () => {
  it('renders without crashing', () => {
    const { container } = render(<Calendar />);
    expect(container.firstChild).toBeInTheDocument();
  });
});
