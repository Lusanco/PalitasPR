<script>
  import { writable } from "svelte/store";
  import axios from "axios";
  import { onMount } from "svelte";
  import { userSession, data } from "../scripts/stores";
  import Button from "../components/Button.svelte";
  export let taskId;

  let description = "";
  let rating = "";
  let errorMessage = "";

  let image = null;
  let button = {
    name: "Enviar Reseña",
    method: "POST",
    url: "/api/reviews/",
    headers: "application/json", // "application/json"
    twcss: "btn bg-[#cc2936] text-white hover:text-[#1f1f1f] hover:bg-white",
    misc: { "App Location": "Create Review" },
  };
  function logFormData(data) {
    for (let pair of data.entries()) {
      console.log(pair[0] + ": " + pair[1]);
    }
  }

  onMount(() => {
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
      task_id: taskId,
    };

    data.set($data);
    console.log("Data updated:", $data);
  }

  function handleKeyPress(event) {
    if (event.key === "Enter") {
      handleReviewSubmit();
    }
  }
</script>
<div class="flex items-center justify-center min-h-screen bg-base">
  <div class="w-full max-w-lg p-4 bg-white shadow-xl card">
    <div class="card-body">
      <h2 class="card-title">Deja tu reseña</h2>
      <div class="form-control">
        <label for="description" class="label">
          <span class="label-text">Descripción (máximo 250 caracteres):</span>
        </label>
        <textarea
          id="description"
          bind:value={description}
          maxlength="250"
          class="textarea textarea-bordered"
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
          class="input input-bordered text-[#cc2936]"
          on:keydown={handleKeyPress}
        />
      </div>
      {#if errorMessage}
        <p class="text-red-500">{errorMessage}</p>
      {/if}
      <div class="mt-4 form-control">
        <Button {image} {button}/>
      </div>
    </div>
  </div>
</div>