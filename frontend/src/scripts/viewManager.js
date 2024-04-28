// viewManager.js
import { writable } from 'svelte/store';

export const currentView = writable("LandingPage");

export function changeView(view) {
    currentView.set(view);
    console.log("View changed to: " + view);
}
