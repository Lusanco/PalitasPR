<!-- Fix: link, layout for all bridge components -->
<script>
    function redirectToHome() {
      window.location.href = "/";
    }
  </script>
  
  <div
    class="flex flex-col items-center justify-center h-full max-w-md min-h-screen p-6 m-auto rounded-md text-primary-content sm:p-10"
  >
    <div class="mb-8 text-center">
      <h1 class="my-3 text-4xl font-bold">Request Created Successfully</h1>
      <p class="text-sm text-teal-600">
        Your request has been successfully submitted.
      </p>
    </div>
    <div class="space-y-2">
      <button
        on:click={redirectToHome}
        type="button"
        class="w-full btn btn-primary"
      >
        Back to Dashboard
      </button>
    </div>
  </div>
  