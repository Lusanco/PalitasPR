<!-- Same as Offers After click it should redirect to Service itself -->
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
  
  <div class="max-h-full min-h-screen bg-base-200">
    <h1 class="font-sans text-3xl text-center text-bold text-primary">Services</h1>
    <br />
    <br />
    <div class="h-screen overscroll-y-auto">
      {#each offers as offer}
        <div class="flex flex-row items-start w-full p-4 mb-4 border-base-300
          <div class="flex-1">
            <div class="font-bold text-primary">{offer.name}</div>
            <div class="text-neutral">{offer.priceRange}</div>
            <div class="text-neutral">ID: {offer.id}</div>
            <div class="text-neutral">Status: {offer.status}</div>
          </div>
        </div>
      {/each}
    </div>
  </div>
  