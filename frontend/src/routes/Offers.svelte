<script>
    let offers = [
      {
        id: 1,
        profilePicture: "https://via.placeholder.com/50",
        name: "John Doe",
        priceRange: "$100 - $200",
        description: "This is a detailed description of the offer.",
        images: ["https://via.placeholder.com/150", "https://via.placeholder.com/150"],
        status: "pending" // status can be "pending", "upcoming", or "promotion"
      },
      {
        id: 2,
        profilePicture: "https://via.placeholder.com/50",
        name: "Jane Smith",
        priceRange: "$150 - $250",
        description: "This is a detailed description of the offer.",
        images: ["https://via.placeholder.com/150", "https://via.placeholder.com/150"],
        status: "upcoming"
      },
      {
        id: 3,
        profilePicture: "https://via.placeholder.com/50",
        name: "Alice Johnson",
        priceRange: "$200 - $300",
        description: "This is a detailed description of the offer.",
        images: ["https://via.placeholder.com/150", "https://via.placeholder.com/150"],
        status: "promotion"
      },
      {
        id: 4,
        profilePicture: "https://via.placeholder.com/50",
        name: "Bob Brown",
        priceRange: "$250 - $350",
        description: "This is a detailed description of the offer.",
        images: ["https://via.placeholder.com/150", "https://via.placeholder.com/150"],
        status: "pending"
      },
      {
        id: 5,
        profilePicture: "https://via.placeholder.com/50",
        name: "Charlie Davis",
        priceRange: "$300 - $400",
        description: "This is a detailed description of the offer.",
        images: ["https://via.placeholder.com/150", "https://via.placeholder.com/150"],
        status: "upcoming"
      },
      {
        id: 6,
        profilePicture: "https://via.placeholder.com/50",
        name: "Eve Wilson",
        priceRange: "$350 - $450",
        description: "This is a detailed description of the offer.",
        images: ["https://via.placeholder.com/150", "https://via.placeholder.com/150"],
        status: "promotion"
      }
    ];
  
    function viewOffer(offer) {
      // Logic to view the full offer
      alert(`Viewing offer for offer ID: ${offer.id}`);
    }
  
    function acceptOffer(offer) {
      // Logic to accept the offer
      alert(`Accepted offer for offer ID: ${offer.id}`);
    }
  
    function declineOffer(offer) {
      // Logic to decline the offer
      alert(`Declined offer for offer ID: ${offer.id}`);
    }
  </script>
  
  <div class="container p-4 mx-auto">
    <h1 class="mb-4 text-2xl font-bold text-center">Offers</h1>
    <div class="w-full mx-auto md:w-3/4">
      {#each offers as offer}
        <div class="flex flex-row items-start p-4 mb-4 border shadow-lg">
          <img src={offer.profilePicture} alt="Profile Picture" class="h-20 mr-4 w-14" />
          <div class="flex-1">
            <div class="font-bold">{offer.name}</div>
            <div>{offer.priceRange}</div>
            <div>ID: {offer.id}</div>
            <div>Status: {offer.status}</div>
          </div>
          <div class="flex flex-col items-end">
            <button
              class="px-4 py-2 mb-2 text-white bg-teal-600 rounded"
              on:click={() => viewOffer(offer)}
            >
              View Offer
            </button>
            <div class="flex justify-between w-full mt-2">
              <button
                class="flex items-center justify-center w-1/2 h-10 mr-2 text-white bg-green-500 rounded"
                on:click={() => acceptOffer(offer)}
              >
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                </svg>
              </button>
              <button
                class="flex items-center justify-center w-1/2 h-10 ml-2 text-white bg-red-500 rounded"
                on:click={() => declineOffer(offer)}
              >
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
                </svg>
              </button>
            </div>
          </div>
        </div>
      {/each}
    </div>
  </div>