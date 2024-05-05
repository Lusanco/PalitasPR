<script>
  function handleFileUpload(event) {
    const files = event.target.files;
    // Handle the selected files here
    console.log("Selected files:", files);
  }
</script>

<div class="flex flex-col items-center justify-center h-screen">
  <div class="max-w-xs p-5 mx-auto rounded-xl bg-slate-100">
    <label
      for="file-upload"
      class="block mb-2 text-sm font-medium text-center text-gray-700"
      >Upload file</label
    >
    <label
      for="file-upload"
      class="flex items-center justify-center w-full p-6 transition-all border-2 rounded-md cursor-pointer"
    >
      <div class="space-y-2 text-center">
        <div
          class="inline-flex items-center justify-center w-10 h-10 mx-auto rounded-full bg-slate-100"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="1.5"
            stroke="currentColor"
            class="w-6 h-6 text-gray-500"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M12 16.5V9.75m0 0l3 3m-3-3l-3 3M6.75 19.5a4.5 4.5 0 01-1.41-8.775 5.25 5.25 0 0110.233-2.33 3 3 0 013.758 3.848A3.752 3.752 0 0118 19.5H6.75z"
            />
          </svg>
        </div>
        <div class="text-gray-600">
          <p
            class="font-medium text-primary-500 hover:text-primary-700 text-balance"
          >
            Click to uploador drag and drop
          </p>
        </div>
        <p class="text-sm text-gray-500 text-balance">
          SVG, PNG, JPG or GIF (max. 1080x720px)
        </p>
      </div>
      <input
        id="file-upload"
        type="file"
        accept=".svg,.png,.jpg,.gif"
        class="sr-only"
        on:change={handleFileUpload}
      />
    </label>
  </div>
</div>
