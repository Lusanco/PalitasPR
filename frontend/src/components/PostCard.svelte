<!-- PostCard.svelte -->

<script>
  export let post;
</script>

<div class="shadow-xl card card-side bg-base-100">
  <figure>
    <img
      src="https://daisyui.com/images/stock/photo-1635805737707-575885ab0820.jpg"
      alt="Movie"
      class="h-full"
    />
  </figure>
  <div class="w-full card-body">
    <div class="p-2 pl-4 rounded-lg bg-base-300">
      <h2 class="card-title">
        {post.author}<span class="span">{post.rating}</span>
      </h2>
    </div>
    <div class="flex justify-start p-8 rounded-lg bg-base-300">
      <p>{post.content}</p>
      <div class="justify-end card-actions"></div>
    </div>
    <div class="flex justify-center gap-2 pt-2">
      <button class="btn PostCardBtn bg-[#00B59F] text-gray-50">Offer</button>
      <button class="btn PostCardBtn bg-[#00B59F] text-gray-50"
        >View More</button
      >
    </div>
  </div>
</div>

<style>
  /* Add your custom styles here */
  .span {
    font-size: 0.8rem;
    color: #00b59f;
    opacity: 0.7;
  }

  .PostCardBtn {
    width: 49.7%;
  }
</style>
