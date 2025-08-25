import { formatDate, capitalize } from './utils';
describe('utils', () => {
  it('formats date correctly', () => {
    expect(formatDate('2025-08-25')).toMatch(/2025/);
  });
  it('capitalizes string', () => {
    expect(capitalize('test')).toBe('Test');
  });
});
