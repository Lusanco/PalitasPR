<script>
    function goBack() {
      window.history.back();
    }
  </script>
  
  <button
    type="button"
    class="inline-flex items-center justify-center w-16 h-16 p-2 text-sm text-teal-600 rounded-lg hover:bg-teal-700 hover:text-gray-200 focus:outline-none focus:ring-0"
    aria-label="Go back"
    on:click={goBack}
  >
    <span class="sr-only">Go back</span>
    <svg class="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
    </svg>
  </button>