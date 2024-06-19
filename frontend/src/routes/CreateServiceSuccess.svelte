<script>
  import { link } from "svelte-routing";
</script>

<head>
  <title>PalitasPR | Create Service Success</title>
</head>

<div
  class="flex flex-col items-center justify-center h-full max-w-md min-h-screen p-6 m-auto text-[#1f1f1f] rounded-md sm:p-10"
>
  <div class="mb-8 text-center">
    <h1 class="my-3 text-4xl font-bold">Service Created Successfully</h1>
    <p class="text-sm text-[#1f1f1f]">
      Your service has been successfully submitted.
    </p>
  </div>
  <div class="space-y-2">
    <a
      use:link
      href="/dashboard"
      type="button"
      class="w-full px-8 py-3 font-semibold bg-[#cc2936] rounded-md text-[#f1f1f1]"
    >
      Back to Dashboard
    </a>
  </div>
</div>
