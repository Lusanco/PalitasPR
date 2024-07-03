<script>
  import { writable } from "svelte/store";
  import axios from "axios";
  import { onMount } from "svelte";
  import { userSession, data } from "../scripts/stores";
  import Button from "../components/Button.svelte";
  import { navigate } from "svelte-routing";

  let description = "";
  let rating = "";
  let errorMessage = "";
  let id;
  let currentUrl;
  let urlArr;
  let initialContact;
  let image = null;
  let button = {
    name: "Enviar Reseña",
    method: "POST",
    url: "/api/reviews/",
    headers: "application/json", // "application/json"
    twcss: "btn bg-accent text-white hover:bg-white hover:text-secondary",
    misc: { "App Location": "Create Review" },
  };
  function logFormData(data) {
    for (let pair of data.entries()) {
      console.log(pair[0] + ": " + pair[1]);
    }
  }

  onMount(() => {
    console.log("CreateReview Component Has Mounted");
    currentUrl = window.location.href;
    console.log("Current URL: ", currentUrl);
    urlArr = currentUrl.split("/");
    id = urlArr[urlArr.length - 1];
    console.log("CreateReview Component ID: ", id);

    axios
      .get("/api/user/status")
      .then((userStatusRes) => {
        userSession.set(true);
        console.log(userStatusRes.data);
      })
      .catch((userStatusErr) => {
        userSession.set(false);
        console.log(userStatusErr);
        console.log($userSession);
      });
  });

  function handleReviewSubmit() {
    if (description.length > 250) {
      errorMessage = "La descripción no puede exceder los 250 caracteres.";
      return;
    }
    const numericRating = parseInt(rating);
    if (isNaN(numericRating) || numericRating < 1 || numericRating > 5) {
      errorMessage = "La puntuación debe estar entre 1 y 5.";
      return;
    }
  }

  $: {
    $data = {
      description,
      rating,
      task_id: id,
    };

    data.set($data);
    console.log("Data updated:", $data);
  }

  function handleButtonClick() {
    // Navigate to a new route or URL
    navigate("/tasks");
  }

  function handleKeyPress(event) {
    if (event.key === "Enter") {
      handleReviewSubmit();
      handleButtonClick();
    }
  }
</script>

<div class="flex items-center justify-center w-full py-20 min-h-fit bg-primary">
  <div class="w-full max-w-3xl p-4 m-5 bg-white shadow-xl card">
    <div class="w-full card-body">
      <h2 class="card-title">Deja tu reseña</h2>
      <div class="form-control">
        <label for="description" class="label">
          <span class="label-text">Descripción (máximo 250 caracteres):</span>
        </label>
        <textarea
          id="description"
          bind:value={description}
          maxlength="250"
          class="h-36 textarea textarea-bordered border-neutral text-secondary"
          on:keydown={handleKeyPress}
        ></textarea>
      </div>
      <div class="form-control">
        <label class="label" for="rating">
          <span class="label-text">Puntuación (1-5):</span>
        </label>
        <input
          type="number"
          id="rating"
          bind:value={rating}
          min="1"
          max="5"
          class="input input-bordered border-neutral text-secondary"
          on:keydown={handleKeyPress}
        />
      </div>
      {#if errorMessage}
        <p class="text-accent">{errorMessage}</p>
      {/if}
      <div class="mt-5 form-control">
        <Button {image} {button} on:click={handleButtonClick} />
      </div>
    </div>
  </div>
</div>
