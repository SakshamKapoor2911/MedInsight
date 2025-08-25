jest.mock('@/hooks/useAuth', () => ({ useAuth: () => ({ token: 'test-token' }) }));
import { render, screen, fireEvent } from "@testing-library/react";
import "@testing-library/jest-dom";
import ChatBox from "./ChatBox";

describe('ChatBox', () => {
  it('renders input and send button', () => {
    render(<ChatBox />);
    expect(screen.getByRole('textbox')).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /send/i })).toBeInTheDocument();
  });
  it('allows typing in input', () => {
    render(<ChatBox />);
    const input = screen.getByRole('textbox');
    fireEvent.change(input, { target: { value: 'Hello' } });
    expect(input).toHaveValue('Hello');
  });
});
