jest.mock('next/navigation', () => ({
  useRouter: () => ({ push: jest.fn(), replace: jest.fn(), prefetch: jest.fn(), pathname: '/', query: {}, asPath: '/', events: { on: jest.fn(), off: jest.fn(), emit: jest.fn() }, isFallback: false }),
  usePathname: () => '/',
  useSearchParams: () => ({ get: jest.fn() }),
}));
import { renderHook, act } from '@testing-library/react-hooks';
import { useAuth } from './useAuth';

describe('useAuth', () => {
  it('returns initial token state', () => {
    const { result } = renderHook(() => useAuth());
    expect(result.current.token).toBeNull();
  });
  it('calls logout and sets token to null', () => {
    const { result } = renderHook(() => useAuth());
    act(() => {
      result.current.logout();
    });
    expect(result.current.token).toBeNull();
  });
});
