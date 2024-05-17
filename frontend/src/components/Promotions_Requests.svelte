<script>
  let activeTab = "Posts";

  function selectTab(tab) {
    activeTab = tab;
  }

  let posts = [
    { id: 1, title: "Post 1", content: "Content for post 1." },
    { id: 2, title: "Post 2", content: "Content for post 2." },
    { id: 3, title: "Post 3", content: "Content for post 3." },
    { id: 4, title: "Post 4", content: "Content for post 4." },
    { id: 5, title: "Post 5", content: "Content for post 5." },
    { id: 6, title: "Post 6", content: "Content for post 6." },
    { id: 7, title: "Post 7", content: "Content for post 7." },
    { id: 8, title: "Post 8", content: "Content for post 8." },
    { id: 9, title: "Post 9", content: "Content for post 9." },
    { id: 10, title: "Post 10", content: "Content for post 10." },
    { id: 11, title: "Post 11", content: "Content for post 11." },
    { id: 12, title: "Post 12", content: "Content for post 12." },
    { id: 13, title: "Post 13", content: "Content for post 13." },
    { id: 14, title: "Post 14", content: "Content for post 14." },
    { id: 15, title: "Post 15", content: "Content for post 15." },
    { id: 16, title: "Post 16", content: "Content for post 16." },
    { id: 17, title: "Post 17", content: "Content for post 17." },
    { id: 18, title: "Post 18", content: "Content for post 18." },
    { id: 19, title: "Post 19", content: "Content for post 19." },
    { id: 20, title: "Post 20", content: "Content for post 20." },
  ];

  let requests = [
    { id: 1, title: "Request 1", content: "Content for request 1." },
    { id: 2, title: "Request 2", content: "Content for request 2." },
    { id: 3, title: "Request 3", content: "Content for request 3." },
    { id: 4, title: "Request 4", content: "Content for request 4." },
    { id: 5, title: "Request 5", content: "Content for request 5." },
    { id: 6, title: "Request 6", content: "Content for request 6." },
    { id: 7, title: "Request 7", content: "Content for request 7." },
    { id: 8, title: "Request 8", content: "Content for request 8." },
    { id: 9, title: "Request 9", content: "Content for request 9." },
    { id: 10, title: "Request 10", content: "Content for request 10." },
    { id: 11, title: "Request 11", content: "Content for request 11." },
    { id: 12, title: "Request 12", content: "Content for request 12." },
    { id: 13, title: "Request 13", content: "Content for request 13." },
    { id: 14, title: "Request 14", content: "Content for request 14." },
    { id: 15, title: "Request 15", content: "Content for request 15." },
    { id: 16, title: "Request 16", content: "Content for request 16." },
    { id: 17, title: "Request 17", content: "Content for request 17." },
    { id: 18, title: "Request 18", content: "Content for request 18." },
    { id: 19, title: "Request 19", content: "Content for request 19." },
    { id: 20, title: "Request 20", content: "Content for request 20." },
  ];
</script>

<div class="flex flex-col">
  <div class="m-5 mb-0">
    <div class="flex gap-2">
      <input
        id="searchBar"
        type="text"
        placeholder="Search..."
        class="flex-grow w-full mb-4 text-gray-700 border-none rounded-lg outline-none placeholder:opacity-85 hover:cursor-pointer focus:ring-0"
      />
      <button
        class="w-10 h-10 transition-colors duration-300 bg-teal-400 rounded-md shadow-sm hover:bg-teal-500"
        ><i class="text-white fa-solid fa-magnifying-glass"></i></button
      >
      <button
        class="w-10 h-10 transition-colors duration-300 bg-white rounded-md shadow-sm hover:bg-opacity-70"
        ><i class="fa-solid fa-bars"></i></button
      >
    </div>
    <ul class="flex text-sm font-medium text-center">
      <li class="w-full focus-within:z-10">
        <button
          class={`inline-block w-full p-4 shadow-md rounded-lg text-slate-100 transition-colors duration-300 ${
            activeTab === "Posts" ? "bg-teal-500" : "bg-teal-400"
          }`}
          on:click={() => selectTab("Posts")}
          aria-current={activeTab === "Posts" ? "page" : undefined}
        >
          Posts
        </button>
      </li>
      <li class="w-2 bg-slate-200"></li>
      <li class="w-full focus-within:z-10">
        <button
          class={`inline-block w-full p-4 shadow-md rounded-lg text-slate-100 transition-colors duration-300 ${
            activeTab === "Requests" ? "bg-teal-500" : "bg-teal-400"
          }`}
          on:click={() => selectTab("Requests")}
        >
          Requests
        </button>
      </li>
    </ul>
  </div>
  <div
    class="flex md:hidden justify-center h-[2px] mx-5 mt-4 -mb-1 bg-slate-300"
  ></div>
  <div class="h-screen m-5 overflow-y-scroll element">
    {#if activeTab === "Posts"}
      <div>
        {#each posts as post}
          <div
            class="flex justify-between p-4 mb-4 bg-white rounded-lg shadow-md"
          >
            <div>
              <h2 class="text-xl font-bold">{post.title}</h2>
              <p>{post.content}</p>
            </div>
            <div class="mt-4">
              <a href="/" class=""><i class="fas fa-angle-right"></i></a>
            </div>
          </div>
        {/each}
      </div>
    {:else if activeTab === "Requests"}
      <div>
        {#each requests as request}
          <div
            class="flex justify-between p-4 mb-4 bg-white rounded-lg shadow-md"
          >
            <div>
              <h2 class="text-xl font-bold">{request.title}</h2>
              <p>{request.content}</p>
            </div>
            <div class="mt-4">
              <a href="/" class=""><i class="fas fa-angle-right"></i></a>
            </div>
          </div>
        {/each}
      </div>
    {/if}
  </div>
</div>

<style>
</style>
