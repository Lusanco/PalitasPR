<!-- Fix: link, layout for all bridge components -->
<script>
  function redirectToHome() {
    window.location.href = "/";
  }
</script>

<head>
  <title>PalitasPR | Create Request Success</title>
</head>

<div
  class="flex flex-col items-center justify-center h-full max-w-md min-h-screen p-6 m-auto text-teal-800 rounded-md sm:p-10"
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
      class="w-full px-8 py-3 font-semibold bg-teal-600 rounded-md text-teal-50"
    >
      Back to Dashboard
    </button>
  </div>
</div>
