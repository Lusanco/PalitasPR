<script>
    import { onMount } from 'svelte';

    let offers = [];
    let acceptedOffers = [];
    let declinedOffers = [];
    let showOffers = [];
    let showAccepted = false;
    let showDeclined = false;
    let user = {
        name: 'John Doe',
        services: ['Jardineria', 'Patio'],
        profilePicture: 'https://via.placeholder.com/150'
    };

    onMount(async () => {
        // Fetch offers from your API and store them in the `offers` array
        // Example data:
        offers = [
    { title: 'Jardinería', description: 'Jardinero en el área Sur, PR', favorite: false, status: 'pending', price: '$50' },
            { title: 'Patio', description: 'Create a modern logo for a tech company.', favorite: false, status: 'pending' },
            { title: 'Mobile App Development', description: 'Develop a new mobile app for a food delivery service.', favorite: false, status: 'pending' },
            { title: 'UX/UI Design', description: 'Design an intuitive user experience and interface for a mobile application.', favorite: false, status: 'pending' },
            { title: 'Database Management', description: 'Design and manage a data solution for an e-commerce company.', favorite: false, status: 'pending' },
            { title: 'Marketing Strategy', description: 'Create a comprehensive marketing strategy for an online store.', favorite: false, status: 'pending' },
            { title: 'Branding', description: 'Develop a cohesive brand identity for a new startup.', favorite: false, status: 'pending' }
        ];
        showOffers = offers;
    });

    function toggleFavorite(offer) {
        offer.favorite = !offer.favorite;
        showOffers = showOffers.sort((a, b) => b.favorite - a.favorite);
    }

    function handleAccept(offer) {
        offer.status = 'accepted';
        updateLists();
    }

    function handleDecline(offer) {
        offer.status = 'declined';
        updateLists();
    }

    function handlePending(offer) {
        offer.status = 'pending';
        updateLists();
    }

    function updateLists() {
        acceptedOffers = offers.filter(offer => offer.status === 'accepted');
        declinedOffers = offers.filter(offer => offer.status === 'declined');
        showOffers = offers.filter(offer => offer.status === 'pending');
    }

    function toggleAccepted() {
        showAccepted = true;
        showDeclined = false;
        showOffers = acceptedOffers;
    }

    function toggleDeclined() {
        showAccepted = false;
        showDeclined = true;
        showOffers = declinedOffers;
    }

    function togglePending() {
        showAccepted = false;
        showDeclined = false;
        updateLists();
    }
</script>


<div class="max-w-md p-2 m-auto lg:max-w-lg xl:max-w-xl md:p-6 md:p-10">
    <div class="text-center mb-7">
        <h1 class="my-3 text-3xl font-bold md:text-5xl">Ofertas de Servicios</h1>
        <p class="text-xs text-teal-600 md:text-sm">Hola {user.name}, consulte las últimas ofertas en su publicación:</p>
        <p class="text-xs text-teal-600 md:text-sm">{user.services.join(', ')}</p>
        <div class="flex items-center justify-center mt-3 space-x-4">
            <button class="px-2 py-1 text-xs font-semibold text-teal-800 bg-teal-200 rounded-md md:px-4 md:py-2 md:text-sm hover:bg-teal-300 focus:outline-none"
                    on:click={() => toggleAccepted()}>Accepted</button>
            <button class="px-2 py-1 text-xs font-semibold text-teal-800 bg-yellow-200 rounded-md md:px-4 md:py-2 md:text-sm hover:bg-yellow-300 focus:outline-none"
                    on:click={() => togglePending()}>Pending</button>
            <button class="px-2 py-1 text-xs font-semibold text-teal-800 bg-red-200 rounded-md md:px-4 md:py-2 md:text-sm hover:bg-red-300 focus:outline-none"
                    on:click={() => toggleDeclined()}>Declined</button>
        </div>
    </div>

    <div class="space-y-12">
        <ul class="space-y-4">
            {#each showOffers as offer, index}
                <li class="relative flex flex-col items-center p-2 border border-teal-300 rounded-md md:flex-row sm:p-4 bg-teal-50">
                    <button class="absolute top-0 right-0 m-2 text-base font-bold text-teal-800 md:text-2xl" on:click={() => toggleFavorite(offer)}>{offer.favorite ? '★' : '☆'}</button>
                    <p class="absolute text-xs font-semibold top-10 right-2 md:top-12 md:right-4 md:text-lg">{offer.price ? offer.price : 'Consultar'}</p>
                    <div class="mr-10 sm:mr-6">
                        <img src="{user.profilePicture}" alt="User Profile Picture" class="rounded-full w-14 h-14 md:w-20 md:h-20">
                    </div>
                    <div class="flex-1">
                        <div class="flex items-start justify-between">
                            <div class="flex-grow">
                                <h3 class="mb-1 text-sm font-bold md:mb-2 md:text-lg">{offer.title}</h3>
                                <p class="mb-2 overflow-hidden text-xs md:mb-4 md:text-sm overflow-ellipsis whitespace-nowrap" style="max-width: 250px;">{offer.description}</p>
                            </div>
                        </div>
                        <!-- Se añade un margen derecho a los botones "Accept" y "Pending" -->
                        <div class="flex mt-4 space-x-2 md:space-x-3">
                            <button on:click={() => handleAccept(offer)}
                                    class="px-2 py-1 text-xs font-semibold text-teal-800 bg-teal-200 rounded-md md:px-4 md:py-2 md:text-sm hover:bg-teal-300 focus:outline-none">Accept</button>
                            <button on:click={() => handlePending(offer)}
                                    class="px-2 py-1 text-xs font-semibold text-teal-800 bg-yellow-200 rounded-md md:px-4 md:py-2 md:text-sm hover:bg-yellow-300 focus:outline-none">Pending</button>
                            <button on:click={() => handleDecline(offer)}
                                    class="px-2 py-1 text-xs font-semibold text-teal-800 bg-red-200 rounded-md md:px-4 md:py-2 md:text-sm hover:bg-red-300 focus:outline-none">Decline</button>
                        </div>
                    </div>
                </li>
            {/each}
        </ul>

        {#if showOffers.length === 0}
            <div class="text-center">
                <p class="text-xs text-teal-600 md:text-sm">No offers available at the moment.</p>
            </div>
        {/if}
    </div>
</div>