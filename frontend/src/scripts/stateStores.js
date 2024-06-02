import { writable } from "svelte/store";

export const state = writable({
  hidden: true,
  loaded: false,
  reload: false,
  error: false,
});
