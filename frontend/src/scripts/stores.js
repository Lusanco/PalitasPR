import { writable } from "svelte/store";

export const data = writable();
export const response = writable(null);
export const responseData = writable(null);
export const responseStatus = writable(null);
export const paginationPage = writable(null);
export const paginationTotal = writable(null);
export const paginationNext = writable(null);
export const paginationPrev = writable(null);
export const state = writable({
  hidden: true,
  loaded: false,
  reload: false,
  error: false,
});

export const userSession = writable(false);
