<!-- ? ReviewCards.svelte -->
<!--
  TODO:

    * Implement data from backend
    * Implement functions with real logic to handle the buttons
-->
<script>
  export let name;
  export let id;
  export let rating;
  export let viewReview;

  /**
   * ! Test image
   */

  let image = `https://picsum.photos/200/300?random=$Math.floor(Math.random() * 1000)`;
</script>

<!-- 
  * ReviewCards component
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
          <p class="text-sm text-white">
            Rating: <span class=""
              ><i class="text-yellow-400 fa-solid fa-star"></i></span
            >
            {rating}
          </p>
          <!--
            * Action button
          -->
          <button
            on:click={viewReview}
            class="px-2 py-[2px] text-white bg-teal-500 rounded"
          >
            View Review
          </button>
        </div>
      </div>
    </div>
  </div>
</div>

<style>
</style>
