jest.mock('@/hooks/useAuth', () => ({ useAuth: () => ({ token: 'test-token' }) }));

import { render, screen, fireEvent } from "@testing-library/react";
import "@testing-library/jest-dom";
import RealtimeChat from "./RealtimeChat";

describe('RealtimeChat', () => {
  it('renders input and send button', () => {
    render(<RealtimeChat />);
    expect(screen.getByRole('textbox')).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /send/i })).toBeInTheDocument();
  });
  it('allows typing in input', () => {
    render(<RealtimeChat />);
    const input = screen.getByRole('textbox');
    fireEvent.change(input, { target: { value: 'Hello' } });
    expect(input).toHaveValue('Hello');
  });
});

