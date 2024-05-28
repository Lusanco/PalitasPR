<!-- ? Promotion/Request after Search View -->
<!-- 
  TODO:

    * Implement data from backend
    * Implement functions with real logic to handle the buttons
    * Implement Card(Component) close logic
-->

<script>
  import ReviewCards from "./ReviewCards.svelte";

  /**
   * ! Test data
   */

  let reviews = [
    {
      name: "Jane Doe",
      id: Math.floor(Math.random() * 1000000),
      rating: Math.floor(Math.random() * 5) + 1,
    },
    {
      name: "John Doe",
      id: Math.floor(Math.random() * 1000000),
      rating: Math.floor(Math.random() * 5) + 1,
    },
    {
      name: "John Smith",
      id: Math.floor(Math.random() * 1000000),
      rating: Math.floor(Math.random() * 5) + 1,
    },
    {
      name: "Jane Smith",
      id: Math.floor(Math.random() * 1000000),
      rating: Math.floor(Math.random() * 5) + 1,
    },
    {
      name: "John Doe",
      id: Math.floor(Math.random() * 1000000),
      rating: Math.floor(Math.random() * 5) + 1,
    },
    {
      name: "John Smith",
      id: Math.floor(Math.random() * 1000000),
      rating: Math.floor(Math.random() * 5) + 1,
    },
    {
      name: "Jane Smith",
      id: Math.floor(Math.random() * 1000000),
      rating: Math.floor(Math.random() * 5) + 1,
    },
  ];

  /**
   * ? User data
   */

  let image = {
    img: "https://images.pexels.com/photos/1453499/pexels-photo-1453499.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    alt: "Lawn Mowing",
  };

  let description = `Lorem ipsum dolor, sit amet consectetur adipisicing elit. Laudantium,
          magni nisi? Repellendus sequi perspiciatis delectus esse excepturi
          laborum, labore debitis quos sunt doloribus nesciunt quia quibusdam
          sed. Culpa, corrupti nisi.`;

  /**
   * ! Test functions
   */

  function handleAccept() {
    alert("Accept button is working!");
  }

  function handleReject() {
    alert("Reject button is working!");
  }

  function handleCard() {
    alert("Close button is working!");
  }

  function viewReview() {
    alert("View Review button is working!");
  }
</script>

<!-- 
  ? Container
-->
<div
  class="flex flex-col items-center justify-center min-h-screen p-5 bg-slate-100"
>
  <!-- 
    * Card 
  -->
  <div
    class="relative w-full max-w-6xl p-5 py-4 mx-2 rounded-md shadow-md bg-slate-100"
  >
    <!-- 
      * Exit button 
    -->
    <button
      on:click={handleCard}
      class="absolute justify-end w-8 top-4 right-2"
    >
      <i class="fa-solid fa-xmark"></i>
    </button>
    <div class="grid grid-cols-1 gap-4 sm:grid-cols-2">
      <!-- 
        * Left Side Section 
      -->
      <div class="col-span-1 p-2 m-1">
        <h1 class="text-3xl text-center">Promotion</h1>
        <figure class="mb-2 border-b-2">
          <img
            src={image.img}
            alt={image.alt}
            class="object-cover w-full h-64 mt-3 rounded-md"
          />
          <div class="mt-2">
            <h2 class="text-lg">John Smith</h2>
            <p class="mb-1 text-sm">Lawn Mowing Services</p>
          </div>
        </figure>
        <p class="mt-2 text-sm lg:text-base">{description}</p>
      </div>
      <!-- 
        * Right Side Section 
      -->
      <div class="col-span-1 p-2 m-1">
        <div class="grid grid-cols-3">
          <h1
            class="col-span-3 text-3xl text-center lg:col-span-1 lg:col-start-2"
          >
            Reviews
          </h1>
        </div>

        <div class="flex flex-col mt-2">
          <div class="flex flex-col gap-1 overflow-y-scroll element h-[26rem]">
            {#each reviews as review (review.id)}
              <!-- 
                * Review Cards Component 
              -->
              <ReviewCards
                name={review.name}
                id={review.id}
                rating={review.rating}
                {viewReview}
              />
            {/each}
          </div>
        </div>
      </div>
      <!-- 
        * Action Buttons 
      -->
      <div
        class="flex justify-center w-full col-span-1 col-start-1 mt-2 sm:col-span-2 sm:col-start-1 sm:mt-4 sm:flex-row"
      >
        <button
          class="w-full px-2 py-4 mx-2 text-white bg-teal-500 rounded hover:bg-teal-600 sm:w-2/3"
          on:click={handleAccept}
        >
          <div class="flex justify-center gap-2">
            <i class="mt-[6px] fa-solid fa-check"></i>
            <span class="hidden md:block">Accept</span>
          </div>
        </button>
        <button
          class="w-full px-2 py-4 mx-2 text-white bg-red-500 rounded hover:bg-red-600 sm:w-2/3"
          on:click={handleReject}
        >
          <div class="flex justify-center gap-2">
            <i class="mt-[6px] fa-solid fa-xmark"></i>
            <span class="hidden md:block">Reject</span>
          </div>
        </button>
      </div>
    </div>
  </div>
</div>
