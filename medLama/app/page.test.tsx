
// Mock Next.js router
jest.mock('next/navigation', () => ({
  useRouter: () => ({ push: jest.fn(), replace: jest.fn(), prefetch: jest.fn(), pathname: '/', query: {}, asPath: '/', events: { on: jest.fn(), off: jest.fn(), emit: jest.fn() }, isFallback: false }),
  usePathname: () => '/',
  useSearchParams: () => ({ get: jest.fn() }),
}));
import { render, screen } from '@testing-library/react';
// Mock useAuth before importing Home
jest.mock('@/hooks/useAuth', () => ({ useAuth: () => ({ token: 'test-token', logout: jest.fn() }) }));
import Home from './page';

describe('Home', () => {
  beforeAll(() => {
    // Mock scrollIntoView for jsdom
    window.HTMLElement.prototype.scrollIntoView = jest.fn();
  });
  it('renders main content', () => {
    render(<Home />);
    expect(screen.getByText(/AI health assistant/i)).toBeInTheDocument();
  });
});
// ...existing code...
