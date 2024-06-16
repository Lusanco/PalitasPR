<script>
  let name, email, subject, message;
</script>

<head>
  <title>PalitasPR | Contact</title>
</head>

<div
  class="flex flex-col justify-center min-h-screen pt-2 md:my-20 bg-base-200"
>
  <div class="relative py-3 sm:max-w-xl sm:mx-auto">
    <div
      class="absolute inset-0 transform -skew-y-6 shadow-lg bg-gradient-to-r from-[#cc2936] to-[#1f1f1f] sm:skew-y-0 sm:-rotate-6 sm:rounded-3xl"
    ></div>
    <div
      class="relative px-4 py-10 shadow-lg bg-gradient-to-tr from-white to-white via-[#f1f1f1] border-l-2 border-b-2 border-[#cc2936] text-[#cc2936] sm:rounded-3xl sm:p-20"
    >
      <div class="pb-6 text-center">
        <h1 class="text-3xl">Contact Us!</h1>
        <p class="text-[#1f1f1f]">
          Fill up the form below to send us a message.
        </p>
      </div>
      <form>
        <input
          class="flex items-center w-full gap-2 px-3 py-2 mb-4 text-[#cc2936] input bg-white input-bordered"
          type="text"
          placeholder="Name"
          name="name"
          bind:value={name}
        />
        <input
          class="flex items-center w-full gap-2 px-3 py-2 mb-4 text-[#cc2936] input bg-white input-bordered"
          type="email"
          placeholder="Email"
          name="email"
          bind:value={email}
        />
        <input
          class="flex items-center w-full gap-2 px-3 py-2 mb-4 text-[#cc2936] input bg-white input-bordered"
          type="text"
          placeholder="Subject"
          name="_subject"
          bind:value={subject}
        />
        <textarea
          class="flex items-center w-full h-64 min-h-0 gap-2 px-3 py-2 mb-4 text-[#cc2936] input bg-white input-bordered"
          placeholder="Type your message here..."
          name="message"
          bind:value={message}
          style="height: 121px;"
        ></textarea>
        <div class="flex justify-between">
          <input
            class="px-4 py-2 font-bold rounded text-[#f1f1f1] bg-[#cc2936] hover:bg-white shadow-xl hover:text-[#cc2936] focus:outline-none focus:shadow-outline"
            type="submit"
            value="Send ➤"
          />
          <input
            class="px-4 py-2 font-bold rounded text-[#f1f1f1] bg-[#cc2936] hover:bg-white shadow-xl hover:text-[#cc2936] focus:outline-none focus:shadow-outline"
            type="reset"
          />
        </div>
      </form>
    </div>
  </div>
</div>
