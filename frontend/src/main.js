import "./app.css";
import App from "./App.svelte";

// Script to handle the current page
import { currentPage } from './scripts/currentPage';

const app = new App({
  target: document.getElementById("app"),
});

// Function to set the title of the page
function updateTitle() {
  const title = `PalitasPR | ${currentPage()}`;
  document.title = title;
  console.log("Title set to:", title); // Debug: Log the title being set
}

// Set the title on initial load and listen for history changes
window.addEventListener('DOMContentLoaded', updateTitle);
window.addEventListener('popstate', updateTitle);

// Override pushState and replaceState to update the title on navigation
const originalPushState = history.pushState;
history.pushState = function() {
  originalPushState.apply(this, arguments);
  updateTitle();
};

const originalReplaceState = history.replaceState;
history.replaceState = function() {
  originalReplaceState.apply(this, arguments);
  updateTitle();
};

// Register the service worker
if ("serviceWorker" in navigator) {
  window.addEventListener("load", () => {
    navigator.serviceWorker
      .register("/service-worker.js")
      .then((registration) => {
        console.log(
          "ServiceWorker registration successful with scope: ",
          registration.scope
        );
      })
      .catch((error) => {
        console.log("ServiceWorker registration failed: ", error);
      });
  });
}

export default app;
