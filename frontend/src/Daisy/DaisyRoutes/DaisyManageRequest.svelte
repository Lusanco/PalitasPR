<script>
  let offers = [
    {
      id: 1,
      profilePicture: "https://via.placeholder.com/50",
      name: "John Doe",
      priceRange: "$100 - $200",
      description: "This is a detailed description of the offer.",
      images: [
        "https://via.placeholder.com/150",
        "https://via.placeholder.com/150",
      ],
      status: "pending", // status can be "pending", "upcoming", or "promotion"
    },
    {
      id: 2,
      profilePicture: "https://via.placeholder.com/50",
      name: "Jane Smith",
      priceRange: "$150 - $250",
      description: "This is a detailed description of the offer.",
      images: [
        "https://via.placeholder.com/150",
        "https://via.placeholder.com/150",
      ],
      status: "upcoming",
    },
    {
      id: 3,
      profilePicture: "https://via.placeholder.com/50",
      name: "Alice Johnson",
      priceRange: "$200 - $300",
      description: "This is a detailed description of the offer.",
      images: [
        "https://via.placeholder.com/150",
        "https://via.placeholder.com/150",
      ],
      status: "promotion",
    },
    {
      id: 4,
      profilePicture: "https://via.placeholder.com/50",
      name: "Bob Brown",
      priceRange: "$250 - $350",
      description: "This is a detailed description of the offer.",
      images: [
        "https://via.placeholder.com/150",
        "https://via.placeholder.com/150",
      ],
      status: "pending",
    },
    {
      id: 5,
      profilePicture: "https://via.placeholder.com/50",
      name: "Charlie Davis",
      priceRange: "$300 - $400",
      description: "This is a detailed description of the offer.",
      images: [
        "https://via.placeholder.com/150",
        "https://via.placeholder.com/150",
      ],
      status: "upcoming",
    },
    {
      id: 6,
      profilePicture: "https://via.placeholder.com/50",
      name: "Eve Wilson",
      priceRange: "$350 - $450",
      description: "This is a detailed description of the offer.",
      images: [
        "https://via.placeholder.com/150",
        "https://via.placeholder.com/150",
      ],
      status: "promotion",
    },
  ];
</script>

<div class="flex justify-center min-h-screen py-8 bg-base-200">
  <div class="w-full max-w-5xl">
    <h1 class="font-sans text-3xl font-bold text-center">Requests</h1>
    <br />
    <br />
    <div class="h-screen overflow-y-scroll">
      {#each offers as offer}
        <a
          href={`/service-details/${offer.id}`}
          class="w-full h-40 mb-4 transition-transform duration-200 ease-in-out transform rounded-sm shadow-xl card card-side bg-base-100 hover:bg-base-300 active:scale-95"
        >
          <div class="flex items-center w-1/4 h-full p-2 rounded-sm md:w-1/4 skeleton">
            <!-- Removed the placeholder image -->
          </div>

          <div class="flex flex-col justify-center w-1/2 h-40 p-2 md:w-1/4 card-body">
            <h2 class="text-md overflow-ellipsis line-clamp-1 md:truncate">
              {offer.name}
            </h2>
            <p class="text-sm md:-mt-2 overflow-ellipsis line-clamp-1 md:truncate">
              {offer.priceRange}
            </p>
            <h3 class="hidden text-lg md:block">Status</h3>
            <p class="text-sm md:-mt-2">{offer.status}</p>
          </div>
          <div class="flex flex-col justify-center w-1/2 h-40 p-2 md:w-2/4 card-body">
            <p class="h-full line-clamp-4 overflow-ellipsis">
              {offer.description}
            </p>
          </div>
        </a>
      {/each}
    </div>
  </div>
</div>