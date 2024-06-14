<script>
  import { onMount } from "svelte";

  let name = "Alfredo Santiago";
  let provServ = "Landscaper";
  let userTown = "San Juan, PR";
  let userRating = 4.5;
  let clientsCount = "100 Clients";
  let jobsCount = 20;
  let reviewerName = "John Doe";
  let reviewStars = 4.5;

  let reviews = [
    {
      user_id: "User ID",
      title: "Excelente Servicio",
      review: "Reseña corta 1",
      rating: 4,
      date: "2024-06-13",
    },
    {
      user_id: "User ID",
      title: "Buen Servicio",
      review: "Reseña corta 2",
      rating: 5,
      date: "2024-06-12",
    },
    {
      user_id: "User ID",
      title: "Mal Servicio",
      review:
        "Reseña muy larga que debería mostrar un botón de 'ver más' para expandir y mostrar todo el contenido de la reseña. Esta es una reseña de ejemplo que es lo suficientemente larga como para necesitar truncamiento. Reseña muy larga que debería mostrar un botón de 'ver más' Reseña muy larga que debería mostrar un botón de 'ver más'",
      rating: 3,
      date: "2024-06-11",
    },
    {
      user_id: "User ID",
      title: "Excelente Servicio",
      review: "Reseña corta 4",
      rating: 4,
      date: "2024-06-10",
    },
    {
      user_id: "User ID",
      title: "Buen Servicio",
      review: "Reseña corta 5",
      rating: 5,
      date: "2024-06-09",
    },
    {
      user_id: "User ID",
      title: "Mal Servicio",
      review: "Reseña corta 6",
      rating: 2,
      date: "2024-06-08",
    },
    {
      user_id: "User ID",
      title: "Excelente Servicio",
      review: "Reseña corta 7",
      rating: 4,
      date: "2024-06-07",
    },
  ];

  let expandedReviews = [];

  function toggleReview(index) {
    if (expandedReviews.includes(index)) {
      expandedReviews = expandedReviews.filter((i) => i !== index);
    } else {
      expandedReviews = [...expandedReviews, index];
    }
  }
</script>

<div
  class="profileContainer py-3 px-[5%] text-[#626262] bg-base-200 max-w-1200 mx-auto"
>
  <div
    class="w-full mb-4 bg-gray-200 rounded-md sm:h-80 md:h-96 lg:h-96 xl:h-96"
  >
    <div class="w-full h-full skeleton"></div>
  </div>

  <div class="p-5 mb-4 bg-white rounded-md shadow-md">
    <div class="flex flex-col justify-between md:flex-row md:items-start">
      <div
        class="w-24 h-24 mb-4 mr-4 bg-gray-200 rounded-md skeleton md:mb-0"
      ></div>
      <div class="flex-1 md:mr-4">
        <h3 class="py-2 text-2xl font-semibold">{name}</h3>
        <p class="text-sm">{provServ}</p>
        <p class="text-sm">
          <i class="fa-solid fa-star"></i>
          <span>{userRating} • {jobsCount} Jobs</span>
        </p>
      </div>
      <div class="flex-1 mb-4 md:mb-0">
        <h3 class="text-xl font-bold border-b-2">About me</h3>
        <div class="pt-3">
          <i class="fa-solid fa-location-dot"></i>
          <span>{userTown}</span>
        </div>
        <div>
          <i class="pr-2 fa-solid fa-check"></i>Completed jobs:
          <span>{jobsCount}</span>
        </div>
        <div class="flex mt-4">
          <a
            href="https://www.instagram.com/tuUsuario/"
            class="mr-4"
            target="_blank"
            rel="noopener noreferrer"
          >
            <i class="fab fa-instagram"></i>
          </a>
          <a
            href="https://www.facebook.com/tuUsuario"
            class="mr-4"
            target="_blank"
            rel="noopener noreferrer"
          >
            <i class="fab fa-facebook-f"></i>
          </a>
          <a
            href="https://twitter.com/tuUsuario"
            target="_blank"
            rel="noopener noreferrer"
          >
            <i class="fab fa-twitter"></i>
          </a>
        </div>
      </div>
    </div>

    <div class="mt-4">
      <p class="text-md">
        Soy un apasionado del paisajismo con más de 10 años de experiencia,
        dedicado a transformar espacios exteriores en lugares de belleza y
        tranquilidad. Mi especialidad incluye diseño de jardines, mantenimiento
        de césped y plantación de especies autóctonas. Comprometido con la
        sostenibilidad y la creación de entornos verdes saludables para mis
        clientes.
      </p>
    </div>
  </div>

  <!-- Sección de Reseñas -->
  <div class="flex flex-col gap-4 mb-4 md:flex-row">
    <div class="w-full p-5 bg-white rounded-md shadow-md md:w-1/2">
      <h3 class="mb-3 text-xl font-bold border-b-2">Reseñas</h3>
      <div class="flex flex-col gap-2 overflow-y-scroll min-h-96 h-96">
        {#each reviews as review, index}
          <div
            class="relative p-4 transition-all shadow-md bg-stone-200"
            class:min-h-auto={expandedReviews.includes(index)}
            class:min-h-[150px]={!expandedReviews.includes(index)}
          >
            <div class="flex justify-between">
              <div class="text-lg font-bold">{review.title}</div>
              <div>{review.date}</div>
            </div>
            <div class="mb-12">
              {#if review.review.length > 250}
                {#if expandedReviews.includes(index)}
                  {review.review}
                  <button
                    class="mt-2 cursor-pointer text-stone-500"
                    on:click={() => toggleReview(index)}
                  >
                    Show Less</button
                  >
                {:else}
                  {review.review.slice(0, 180)}...
                  <button
                    class="mt-2 cursor-pointer text-stone-500"
                    on:click={() => toggleReview(index)}
                  >
                    Show More</button
                  >
                {/if}
              {:else}
                {review.review}
              {/if}
            </div>
            <div class="absolute text-sm bottom-2 left-2 text-stone-500">
              {review.user_id}
            </div>
            <div class="absolute text-sm bottom-2 right-2 text-stone-500">
              Rating: {review.rating}
            </div>
          </div>
        {/each}
      </div>
    </div>

    <!-- Galería con scroll vertical, mostrando dos imágenes por fila -->
    <div class="w-full p-5 bg-white rounded-md shadow-md md:w-1/2">
      <h3 class="mb-3 text-xl font-bold border-b-2">Galería</h3>
      <div class="flex flex-col gap-2 overflow-y-scroll min-h-96 h-96">
        <!-- Row 1 -->
        <div class="flex gap-2">
          <div class="w-1/2 h-32 bg-gray-300 rounded-md"></div>
          <div class="w-1/2 h-32 bg-gray-300 rounded-md"></div>
        </div>
        <!-- Row 2 -->
        <div class="flex gap-2">
          <div class="w-1/2 h-32 bg-gray-300 rounded-md"></div>
          <div class="w-1/2 h-32 bg-gray-300 rounded-md"></div>
        </div>
        <!-- Row 3 -->
        <div class="flex gap-2">
          <div class="w-1/2 h-32 bg-gray-300 rounded-md"></div>
          <div class="w-1/2 h-32 bg-gray-300 rounded-md"></div>
        </div>
        <!-- Row 4 -->
        <div class="flex gap-2">
          <div class="w-1/2 h-32 bg-gray-300 rounded-md"></div>
          <div class="w-1/2 h-32 bg-gray-300 rounded-md"></div>
        </div>
      </div>
    </div>
  </div>
</div>
