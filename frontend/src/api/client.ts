import { BACKEND_URL } from "@/constants/Values";

export class APIClient {
    baseURL: string;

    constructor(baseURL: string) {
      this.baseURL = baseURL;
    }
  
    async fetchData<T = object>(relativePath: string, options = {}): Promise<T> {
      const url = `${this.baseURL}${relativePath}`;
      try {
        const response = await fetch(url, options);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return await response.json() as T;
      } catch (error) {
        console.error('Fetch error:', error);
        throw error;
      }
    }
  }

export const api = new APIClient(BACKEND_URL);