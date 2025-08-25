import { analyzeData, findAvailableDoctors, findNearbyHospitals } from './analysis';

describe('analyzeData', () => {
  it('returns expected result for valid input', () => {
    const result = analyzeData({ value: 10 });
    expect(result).toEqual({ result: 20 });
  });
  it('handles edge cases', () => {
    expect(() => analyzeData(null)).toThrow('Invalid input');
    expect(() => analyzeData({})).toThrow('Invalid input');
    expect(() => analyzeData({ value: 'not-a-number' })).toThrow('Invalid input');
  });
});

describe('findAvailableDoctors', () => {
  beforeEach(() => {
    global.fetch = jest.fn(() => Promise.resolve({
      ok: true,
      status: 200,
      json: () => Promise.resolve([{ name: 'Dr. Smith', specialty: 'cardiology' }]),
      headers: new Headers(),
      redirected: false,
      statusText: '',
      type: 'basic',
      url: '',
      clone: function() { return this; },
      body: null,
      bodyUsed: false,
      arrayBuffer: () => Promise.resolve(new ArrayBuffer(0)),
      blob: () => Promise.resolve(new Blob()),
      formData: () => Promise.resolve(new FormData()),
      text: () => Promise.resolve(''),
    } as Response));
  });
  afterEach(() => {
    jest.resetAllMocks();
  });
  it('returns a list of doctors for valid specialty', async () => {
    const doctors = await findAvailableDoctors('cardiology');
    expect(Array.isArray(doctors)).toBe(true);
    expect(doctors.length).toBeGreaterThan(0);
    expect(doctors[0]).toHaveProperty('name');
  });
});

describe('findNearbyHospitals', () => {
  beforeEach(() => {
    global.fetch = jest.fn(() => Promise.resolve({
      ok: true,
      status: 200,
      json: () => Promise.resolve([{ name: 'General Hospital', latitude: 38.02931, longitude: -78.47668 }]),
      headers: new Headers(),
      redirected: false,
      statusText: '',
      type: 'basic',
      url: '',
      clone: function() { return this; },
      body: null,
      bodyUsed: false,
      arrayBuffer: () => Promise.resolve(new ArrayBuffer(0)),
      blob: () => Promise.resolve(new Blob()),
      formData: () => Promise.resolve(new FormData()),
      text: () => Promise.resolve(''),
    } as Response));
  });
  afterEach(() => {
    jest.resetAllMocks();
  });
  it('returns a list of hospitals for valid coordinates', async () => {
    const hospitals = await findNearbyHospitals(38.02931, -78.47668);
    expect(Array.isArray(hospitals)).toBe(true);
    expect(hospitals.length).toBeGreaterThan(0);
    expect(hospitals[0]).toHaveProperty('name');
  });
});
// Removed duplicate test blocks and imports
