import React from 'react';
import { render } from '@testing-library/react';
import { Progress } from './progress';

describe('Progress', () => {
  it('renders with default props', () => {
    const { container } = render(<Progress />);
    expect(container.firstChild).toBeInTheDocument();
  });
    it('renders with value', () => {
      const { container } = render(<Progress value={50} />);
      // Find the progressbar element and check aria-valuenow
      const progressBar = container.querySelector('[role="progressbar"]');
      // Accept either string or number, fallback to checking not null
      expect(progressBar?.getAttribute('aria-valuenow')).not.toBeNull();
      expect(["50", 50]).toContain(progressBar?.getAttribute('aria-valuenow'));
    });
});
