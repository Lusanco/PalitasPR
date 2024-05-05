<script>
  function scrollToTeam() {
    const teamSection = document.getElementById("team");
    teamSection.scrollIntoView({ behavior: "smooth" });
  }
</script>

<div class="scroll-smooth">
  <div class="relative bg-teal-700 h-[32rem]">
    <div class="absolute inset-x-0 bottom-0">
      <svg
        viewBox="0 0 224 12"
        fill="currentColor"
        class="w-full -mb-1 text-white"
        preserveAspectRatio="none"
      >
        <path
          d="M0,0 C48.8902582,6.27314026 86.2235915,9.40971039 112,9.40971039 C137.776408,9.40971039 175.109742,6.27314026 224,0 L224,12.0441132 L0,12.0441132 L0,0 Z"
        ></path>
      </svg>
    </div>
    <div
      class="px-4 py-16 mx-auto sm:max-w-xl md:max-w-full lg:max-w-screen-xl md:px-24 lg:px-8 lg:py-20"
    >
      <div
        class="relative max-w-2xl sm:mx-auto sm:max-w-xl md:max-w-2xl sm:text-center"
      >
        <h1
          class="mb-10 text-5xl font-bold tracking-tight text-center text-white sm:text-4xl sm:leading-none"
        >
          About Us
        </h1>
        <p class="mb-6 text-base text-center text-indigo-100 md:text-lg">
          Join our newsletter to keep up to date on features and releases. Also
          keep an eye out for discounts and promotions. No spam, we promise.
        </p>
        <form
          class="flex flex-col items-center w-full gap-2 mb-4 md:flex-row md:px-16"
        >
          <input
            placeholder="Email"
            type="text"
            class="w-full h-12 px-2 text-black border-2 border-transparent rounded shadow-lg placeholder:text-slate-300 md:mr-2 focus:border-none text-start sm:text-center placeholder:text-center md:placeholder:text-start"
          />
          <a
            href="/"
            class="inline-flex items-center justify-center w-full h-12 px-4 font-semibold tracking-wide text-black transition duration-200 rounded shadow-lg bg-slate-100 md:w-auto"
          >
            Subscribe
          </a>
        </form>
        <p
          class="max-w-md mb-10 text-xs tracking-wide text-center text-indigo-100 sm:text-sm sm:mx-auto md:mb-16"
        >
          We respect your privacy. <a href="/" class="hover:underline"
            >Unsubscribe</a
          > at any time.
        </p>
        <button
          on:click={scrollToTeam}
          aria-label="Scroll down"
          class="flex items-center justify-center w-10 h-10 mx-auto text-white duration-300 transform border rounded-full hover:shadow-sm hover:scale-110"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="12"
            height="12"
            viewBox="0 0 12 12"
            fill="currentColor"
          >
            <path
              d="M10.293,3.293,6,7.586,1.707,3.293A1,1,0,0,0,.293,4.707l5,5a1,1,0,0,0,1.414,0l5-5a1,1,0,1,0-1.414-1.414Z"
            ></path>
          </svg>
        </button>
      </div>
    </div>
  </div>
  <div
    id="team"
    class="px-4 py-16 mx-auto sm:max-w-xl md:max-w-full lg:max-w-screen-xl md:px-24 lg:px-8 lg:py-20"
  >
    <div class="mx-auto mb-10 lg:max-w-xl sm:text-center">
      <p
        class="inline-block px-3 py-px mb-4 text-xs font-semibold tracking-wider text-teal-900 uppercase rounded-full bg-teal-accent-400"
      >
        Our Team
      </p>
      <p class="text-base text-gray-700 md:text-lg">
        Meet the team that makes it all happen. We are a diverse group of people
        who love what we do. We are passionate about our work and we are always
        looking for ways to improve.
      </p>
    </div>
    <div
      class="grid items-center gap-6 lg:max-w-screen-xl sm:grid-cols-2 lg:grid-cols-2"
    >
      <div class="flex flex-col items-center justify-center">
        <img
          class="object-cover w-20 h-20 mb-2 rounded-full shadow"
          src="https://images.pexels.com/photos/220453/pexels-photo-220453.jpeg?auto=compress&amp;cs=tinysrgb&amp;dpr=3&amp;h=750&amp;w=1260"
          alt="Person"
        />
        <div class="flex flex-col items-center">
          <p class="text-lg font-bold">Luis Santiago</p>
          <p class="text-sm text-gray-800">Team Lead</p>
        </div>
      </div>
      <div class="flex flex-col items-center">
        <img
          class="object-cover w-20 h-20 mb-2 rounded-full shadow"
          src="https://images.pexels.com/photos/2381069/pexels-photo-2381069.jpeg?auto=compress&amp;cs=tinysrgb&amp;dpr=2&amp;h=750&amp;w=1260"
          alt="Person"
        />
        <div class="flex flex-col items-center">
          <p class="text-lg font-bold">Antonio De Jesus</p>
          <p class="text-sm text-gray-800">Database Manager</p>
        </div>
      </div>
      <div class="flex flex-col items-center col-span-2">
        <img
          class="object-cover w-20 h-20 mb-2 rounded-full shadow"
          src="https://images.pexels.com/photos/3785077/pexels-photo-3785077.jpeg?auto=compress&amp;cs=tinysrgb&amp;dpr=2&amp;w=500"
          alt="Person"
        />
        <div class="flex flex-col items-center">
          <p class="text-lg font-bold">Jonathan Perez</p>
          <p class="text-sm text-gray-800">UI/UX - Mobile Developer</p>
        </div>
      </div>
      <div class="flex flex-col items-center">
        <img
          class="object-cover w-20 h-20 mb-2 rounded-full shadow"
          src="https://images.pexels.com/photos/2379004/pexels-photo-2379004.jpeg?auto=compress&amp;cs=tinysrgb&amp;dpr=2&amp;h=750&amp;w=1260"
          alt="Person"
        />
        <div class="flex flex-col items-center">
          <p class="text-lg font-bold">Louis Toro</p>
          <p class="text-sm text-gray-800">Backend Manager</p>
        </div>
      </div>
      <div class="flex flex-col items-center">
        <img
          class="object-cover w-20 h-20 mb-2 rounded-full shadow"
          src="https://images.pexels.com/photos/3747435/pexels-photo-3747435.jpeg?auto=compress&amp;cs=tinysrgb&amp;dpr=2&amp;h=750&amp;w=1260"
          alt="Person"
        />
        <div class="flex flex-col items-center">
          <p class="text-lg font-bold">Livan Hernandez</p>
          <p class="text-sm text-gray-800">UI/UX - Web Developer</p>
        </div>
      </div>
    </div>
  </div>
</div>
