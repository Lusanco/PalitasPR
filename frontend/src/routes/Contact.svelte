<script>
  let name, email, subject, message;
</script>

<div
  class="flex flex-col justify-center min-h-screen pt-2 md:my-20 bg-base-200"
>
  <div class="relative py-3 sm:max-w-xl sm:mx-auto">
    <div
      class="absolute inset-0 transform -skew-y-6 shadow-lg bg-gradient-to-r from-stone-500 to-stone-700 sm:skew-y-0 sm:-rotate-6 sm:rounded-3xl"
    ></div>
    <div
      class="relative px-4 py-10 shadow-lg text-stone-100 bg-stone-500 sm:rounded-3xl sm:p-20"
    >
      <div class="pb-6 text-center">
        <h1 class="text-3xl">Contact Us!</h1>
        <p class="text-stone-300">
          Fill up the form below to send us a message.
        </p>
      </div>
      <form>
        <input
          class="flex items-center w-full gap-2 px-3 py-2 mb-4 text-stone-800 input input-bordered"
          type="text"
          placeholder="Name"
          name="name"
          bind:value={name}
        />
        <input
          class="flex items-center w-full gap-2 px-3 py-2 mb-4 text-stone-800 input input-bordered"
          type="email"
          placeholder="Email"
          name="email"
          bind:value={email}
        />
        <input
          class="flex items-center w-full gap-2 px-3 py-2 mb-4 text-stone-800 input input-bordered"
          type="text"
          placeholder="Subject"
          name="_subject"
          bind:value={subject}
        />
        <textarea
          class="flex items-center w-full h-64 min-h-0 gap-2 px-3 py-2 mb-4 text-stone-800 input input-bordered"
          placeholder="Type your message here..."
          name="message"
          bind:value={message}
          style="height: 121px;"
        ></textarea>
        <div class="flex justify-between">
          <input
            class="px-4 py-2 font-bold rounded shadow text-stone-100 bg-stone-600 hover:bg-stone-700 focus:outline-none focus:shadow-outline"
            type="submit"
            value="Send ➤"
          />
          <input
            class="px-4 py-2 font-bold rounded shadow text-stone-100 bg-stone-600 hover:bg-stone-700 focus:outline-none focus:shadow-outline"
            type="reset"
          />
        </div>
      </form>
    </div>
  </div>
</div>
