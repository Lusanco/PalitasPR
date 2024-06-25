<script>
  import { state, data, userSession } from "../scripts/stores";
  import townsID from "../scripts/townsID";
  import servicesID from "../scripts/servicesID";
  import Button from "../components/Button.svelte";
  import axios from "axios";
  import { onMount } from "svelte";

  let image = null;
  let town = "all";
  let towns;
  let model = "Request";

  let button = {
    name: "Solicitar servicio",
    method: "POST",
    url: "api/dashboard/promotion-request",
    headers: "multipart/form-data",
    twcss:
      "px-8 py-3 font-semibold bg-[#cc2936] text-[#f1f1f1] rounded hover:bg-white hover:text-[#1f1f1f] hover:shadow-md",
    misc: { "App Location": "CreateRequest Form" },
  };

  let title = "";
  let service_id = "";
  let description = "";
  let errorMessage = "";
  let selectedTowns = [];
  let townList = "";

  $: {
    $data = {
      model,
      title,
      town: townList,
      service_id,
      description,
      // price_min,
      // price_max,
    };

    data.set($data);
    console.log("Data updated:", $data);
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
      console.log($userSession)
    })
  })
  
  function handleTownChange(event) {
    const townId = event.target.value;
    if (event.target.checked) {
      selectedTowns.push(townId);
    } else {
      selectedTowns = selectedTowns.filter((id) => id !== townId);
    }
    townList = selectedTowns.join(", ");
  }

  function handleFileChange(event) {
    image = event.target.files[0];
    console.log("Image file selected:", event.target.files[0]);
  }

  function handleButtonClick() {
    document.getElementById("townsDropdown").classList.toggle("hidden");
  }
</script>

<head>
  <title>PalitasPR | Solicitar Servicio</title>
</head>

<div
  class="flex flex-col items-center justify-center h-full min-h-screen bg-[#f1f1f1]"
>
  <div
    class="flex flex-col w-full h-full max-w-2xl gap-4 p-6 my-8 font-semibold bg-white rounded-lg shadow-lg md:p-12"
  >
    <h1
      class="pt-4 text-2xl text-center text-[#1f1f1f] md:text-3xl lg:text-4xl"
    >
      Solicitar Servicio
    </h1>
    <div>
      <label for="title" class="text-[#1f1f1f]">Título</label>
      <input
        class="w-full input input-bordered text-[#cc2936]"
        type="text"
        name="title"
        id="title"
        bind:value={title}
      />
    </div>

    <label for="service" class="text-[#1f1f1f]"
      >Seleccionar servicio
      <select
        bind:value={service_id}
        name="service"
        class="block w-full select select-bordered text-[#cc2936]"
      >
        <option value={-1} disabled>---</option>
        {#each Object.entries(servicesID) as [service, id]}
          <option value={id}>{service}</option>
        {/each}
      </select>
    </label>

    <div class="w-full dropdown">
      <button
        on:click={handleButtonClick}
        tabindex="0"
        class="btn btn-base dropdown-toggle text-[#f1f1f1] bg-[#cc2936] hover:bg-white hover:text-[#1f1f1f] hover:shadow-md"
        >Seleccionar pueblos</button
      >
      <ul
        id="townsDropdown"
        tabindex="-1"
        class="grid w-full h-40 min-w-full grid-cols-1 gap-4 p-4 overflow-y-auto bg-white shadow md:grid-cols-3 text-nowrap dropdown-content rounded-box"
      >
        {#each Object.entries(townsID).filter(([town, id]) => town !== "all") as [town, id]}
          <li class="menu-item" value={id}>
            <input
              bind:value={id}
              on:change={handleTownChange}
              type="checkbox"
              id={`'${id}'`}
              class="mr-2 checkbox checkbox-base"
            />
            {town}
          </li>
        {/each}
      </ul>
    </div>

    <div class="max-h-96">
      <label for="description" class="text-[#1f1f1f]"
        >Descripción del servicio solicitado</label
      >
      <textarea
        bind:value={description}
        class="w-full textarea textarea-bordered text-[#cc2936]"
        name="description"
        id="description"
      ></textarea>
    </div>
    <div>
      <!-- <label for="price-min" class="text-[#1f1f1f]"
        >Precio mínimo (Opcional)</label
      >
      <input
        class="w-full input input-bordered text-[#cc2936]"
        type="number"
        name="price-min"
        id="price-min"
        bind:value={price_min}
      />
    </div>
    <div>
      <label for="price-max" class="text-[#1f1f1f]"
        >Precio máximo (Opcional)</label
      >
      <input
        class="w-full input input-bordered text-[#cc2936]"
        type="number"
        name="price-max"
        id="price-max"
        bind:value={price_max}
      /> -->
    </div>
    <div
      class="flex flex-col items-center justify-center w-full m-auto mx-auto space-y-1 text-[#1f1f1f]"
    >
      <label for="imageInput" class="block text-sm font-medium text-[#1f1f1f]"
      ></label>
      <div class="flex w-full">
        <label for="imageInput" class="w-full mb-2">
          Subir imagen
          <input
            type="file"
            name="image"
            id="imageInput"
            on:change={handleFileChange}
            class="w-full px-8 py-12 text-[#1f1f1f] bg-[#f1f1f1] border-2 border-[#cc2936] border-dashed rounded-md"
            accept="image/*"
          /></label
        >
      </div>
      {#if errorMessage}
        <p class="text-[#cc2936]">{errorMessage}</p>
      {/if}
    </div>

    <Button {button} {image} />
    <div />
  </div>
</div>
