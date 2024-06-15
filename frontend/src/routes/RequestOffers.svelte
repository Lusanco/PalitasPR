<!-- Revised: Alfre - Remember to move/rename this where it belongs: Promote from dashboard -->
<script>
  import OfferCard from "../components/OfferCard.svelte";

  /**
   * ! Test data
   */

  let offers = [
    {
      name: "Jane Doe",
      id: Math.floor(Math.random() * 1000000),
    },
    {
      name: "John Doe",
      id: Math.floor(Math.random() * 1000000),
    },
    {
      name: "John Smith",
      id: Math.floor(Math.random() * 1000000),
    },
    {
      name: "Jane Smith",
      id: Math.floor(Math.random() * 1000000),
    },
    {
      name: "John Doe",
      id: Math.floor(Math.random() * 1000000),
    },
    {
      name: "John Smith",
      id: Math.floor(Math.random() * 1000000),
    },
    {
      name: "Jane Smith",
      id: Math.floor(Math.random() * 1000000),
    },
  ];

  /**
   * ? User data
   */

  let image = {
    img: "https://images.pexels.com/photos/1453499/pexels-photo-1453499.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    alt: "Lawn Mowing",
  };

  let service = "Lawn Mowing";

  let description = `Lorem ipsum dolor, sit amet consectetur adipisicing elit. Laudantium,
          magni nisi? Repellendus sequi perspiciatis delectus esse excepturi
          laborum, labore debitis quos sunt doloribus nesciunt quia quibusdam
          sed. Culpa, corrupti nisi.`;

  /**
   * ! Test functions
   */

  function handleCard() {
    alert("Close button is working!");
  }

  function viewOffer() {
    alert("View Review button is working!");
  }

  /**
   * ? Function to toggle the dropdown menu
   */

  function toggleDropdown(event) {
    const menu = event.currentTarget.nextElementSibling;
    menu.classList.toggle("hidden");
  }
</script>

<head>
  <title>PalitasPR | Request Offerts</title>
</head>

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
        <h1 class="text-3xl text-center">Service</h1>
        <figure class="mb-2 border-b-2">
          <img
            src={image.img}
            alt={image.alt}
            class="object-cover w-full h-64 mt-3 rounded-md"
          />
          <div class="flex justify-between mt-2">
            <div>
              <h2 class="text-lg">Jardineria: rr43523454325</h2>
              <p class="mb-1 text-sm">Juan del Pueblo: 11234fsd4421</p>
            </div>
            <div class="relative mt-3 mr-2 dropdown-top">
              <button on:click={toggleDropdown} class="m-1"
                ><i class="fa-solid fa-ellipsis"></i></button
              >
              <ul
                class="absolute z-10 hidden p-2 shadow menu dropdown-content bg-slate-100 rounded-box w-52"
              >
                <li>
                  <a href="/"
                    ><i class="text-yellow-400 fa-solid fa-pencil"></i> Edit</a
                  >
                </li>
                <li>
                  <a href="/"
                    ><i class="text-red-600 fa-solid fa-trash"></i>
                    <span class="">Delete</span></a
                  >
                </li>
              </ul>
            </div>
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
            Offers
          </h1>
        </div>

        <div class="flex flex-col mt-2">
          <div class="flex flex-col gap-1 overflow-y-scroll element h-[26rem]">
            {#each offers as offer (offer.id)}
              <!-- 
                * Offers Cards Component 
              -->
              <OfferCard name={offer.name} id={offer.id} {viewOffer} />
            {/each}
          </div>
        </div>
      </div>
      <!-- 
        * Action Buttons 
      -->
    </div>
  </div>
</div>
