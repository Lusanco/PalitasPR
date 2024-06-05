import { writable } from "svelte/store";

// State store for UI/loading indicators
export const state = writable({
  hidden: true,
  loaded: false,
  reload: false,
  error: false,
});

// The data store now consistently holds a JavaScript object
export const data = writable({});
export const image = writable(null);
