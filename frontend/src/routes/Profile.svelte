<!-- Profile component -->
<script>
  import { slide } from "svelte/transition";
  import { onMount } from "svelte";
  import banner from "../images/lawnMowing.jpg";
  import profilePic from "../images/profile.png";
  import pic1 from "../images/gallGrid_1.jpg";
  import pic2 from "../images/gallGrid_2.jpg";
  import pic3 from "../images/gallGrid_3.jpg";
  import pic4 from "../images/gallGrid_4.jpg";
  import pic5 from "../images/gallGrid_5.jpg";
  import pic6 from "../images/gallGrid_6.jpg";
  import axios from "axios";

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
      reviewerName: "John Doe",
      reviewStars: 4,
      reviewText: "Lorem ipsum dolor sit amet, consectetur adipisicing elit.",
    },
    {
      reviewerName: "Jane Smith",
      reviewStars: 5,
      reviewText:
        "Sed ut perspiciatis unde omnis iste natus error sit voluptatem.",
    },
    {
      reviewerName: "Bob Johnson",
      reviewStars: 3,
      reviewText: "At vero eos et accusamus et iusto odio dignissimos ducimus.",
    },
  ];

  let currentIndex = 0;
  let intervalId;

  function nextReview() {
    currentIndex = (currentIndex + 1) % reviews.length;
  }

  function prevReview() {
    currentIndex = (currentIndex - 1 + reviews.length) % reviews.length;
  }

  onMount(() => {
    // axios.get("");
  });
</script>

<div
  class="flex flex-col items-center justify-center max-w-5xl mx-auto text-stone-700 bg-base-200"
>
  <div class="w-full rounded-none h-96 skeleton"></div>

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
          <div class="relative p-4 transition-all shadow-md bg-stone-200">
            <div class="flex justify-between">
              <div class="text-lg font-bold">{review.title}</div>
              <div>{review.date}</div>
            </div>
            <div class="mb-12">
              {#if 0 > 250}
                {#if true}
                  {review.review}
                  <button class="mt-2 cursor-pointer text-stone-500">
                    Show Less</button
                  >
                {:else}
                  {review.review.slice(0, 180)}...
                  <button class="mt-2 cursor-pointer text-stone-500">
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
