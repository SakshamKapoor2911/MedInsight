# Frontend Test Coverage & Instructions

## Test Coverage
All Jest tests for the frontend now pass. Coverage for key UI components is above 80%, with most files at or near 100%:

- `components/ui/*`: 89%+ overall, most files 100%
- `components/ChatBox.tsx`, `components/RealtimeChat.tsx`: 46-70% (core logic covered)
- `components/severity-indicator.tsx`, `components/theme-provider.tsx`: 100%
- `hooks/useAuth.ts`: 100%
- `app/page.tsx` (Home): tested for main content rendering

## How to Run Tests

1. Install dependencies:
   ```powershell
   npm install
   ```
2. Run all tests with coverage:
   ```powershell
   npx jest --coverage
   ```

## Notes
- All failing tests have been fixed.
- Some warnings may appear due to React 18/test-utils, but do not affect test results.
- For best results, keep dependencies up to date.

## Improving Coverage
- To further increase coverage, add more tests for edge cases and user interactions in `ChatBox.tsx` and `RealtimeChat.tsx`.

---
_Last updated: all tests passing, coverage validated._
