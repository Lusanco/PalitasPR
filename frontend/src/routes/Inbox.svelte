<!-- After click it should redirect to Service where the offer was made/tied to -->
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

<div class="max-h-full min-h-screen">
  <h1 class="font-sans text-3xl text-center text-bold">Inbox</h1>
  <br />
  <br />
  <div class="h-screen overflow-scroll overscroll-y-auto">
    {#each offers as offer}
      <div class="flex flex-row items-start w-full p-4 mb-4 border shadow-lg">
        <!-- svelte-ignore a11y-img-redundant-alt -->
        <img
          src={offer.profilePicture}
          alt="Profile Picture"
          class="h-20 mr-4 w-14"
        />
        <div class="flex-1">
          <div class="font-bold">{offer.name}</div>
          <div>{offer.priceRange}</div>
          <div>ID: {offer.id}</div>
          <div>Status: {offer.status}</div>
        </div>
      </div>
    {/each}
  </div>
</div>
