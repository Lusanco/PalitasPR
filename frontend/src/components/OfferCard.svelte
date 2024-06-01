<!-- ? OffersCards.svelte -->
<!--
  TODO:

    * Implement data from backend
    * Implement functions with real logic to handle the buttons
-->
<script>
  export let name;
  export let id;
  export let viewOffer;

  /**
   * ! Test functions
   */

  function handleAccept() {
    alert("Accept button is working!");
  }

  function handleReject() {
    alert("Reject button is working!");
  }

  /**
   * ! Test image
   */

  let image = `https://picsum.photos/200/300?random=$Math.floor(Math.random() * 1000)`;
</script>

<!--
  * OffersCards component
-->
<div class="p-3 my-1 bg-teal-800 rounded shadow-lg review-card">
  <!--
      * Card content
  -->
  <div class="flex w-full gap-2">
    <!--
        * Card left section
    -->
    <figure>
      <img
        src={image}
        alt="profilePic"
        class="object-cover w-16 h-16 rounded-md"
      />
    </figure>
    <div class="flex flex-col justify-between w-full gap-2 mt-2">
      <div class="flex items-center justify-between">
        <!--
          * User and promotion details
        -->
        <div>
          <h2 class="text-xl text-white">{name}</h2>
          <p class="text-sm text-white">Id: {id}</p>
          <div class="flex items-center gap-2"></div>
        </div>
        <!--
          * Card right section
        -->
        <div class="flex flex-col gap-1">
          <!--
            * Action buttons
          -->
          <button
            on:click={viewOffer}
            class="px-2 py-[2px] text-white hover:bg-teal-600 bg-teal-500 rounded"
          >
            View Offer
          </button>
          <div class="flex gap-2">
            <button
              class="w-full text-white bg-teal-500 rounded hover:bg-teal-600 sm:w-2/3"
              on:click={handleAccept}
            >
              <div class="flex justify-center gap-2 mx-2">
                <i class="my-[4px] fa-solid fa-check"></i>
                <span class="hidden md:block">Accept</span>
              </div>
            </button>
            <button
              class="w-full text-white bg-red-500 rounded hover:bg-red-600 sm:w-2/3"
              on:click={handleReject}
            >
              <div class="flex justify-center gap-2 mx-2">
                <i class="mt-[4px] fa-solid fa-xmark"></i>
                <span class="hidden md:block">Reject</span>
              </div>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<style></style>
