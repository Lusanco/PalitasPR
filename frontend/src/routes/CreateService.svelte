<script>
  import { state, data, image } from "../scripts/stateStores";
  import townsID from "../scripts/townsID";
  import servicesID from "../scripts/servicesID";
  import Button from "../components/Button.svelte";

  let model = "Promotion";
  let title = "";
  let service_id = "";
  let description = "";
  let price_min = "";
  let price_max = "";
  let errorMessage = "";

  const towns = Object.entries(townsID);
  const services = Object.entries(servicesID);

  let selectedTowns = [];
  let townList = "";

  // Reactive block to update $data
  $: {
    $data = {
      model,
      title,
      townList,
      service_id,
      description,
      price_min,
      price_max,
    };

    console.log("Data updated:", $data);
  }

  // Button configuration
  let button = {
    name: "Create Service",
    method: "POST",
    url: "api/dashboard/promotion-request",
    headers: {
      "Content-Type": "multipart/form-data",
    },
    twcss: "px-8 py-3 font-semibold text-teal-100 bg-teal-800 rounded",
    misc: { "Create Service": true },
  };

  // Function to handle town selection changes
  function handleTownChange(event) {
    const townId = event.target.value;
    if (event.target.checked) {
      selectedTowns.push(townId);
    } else {
      selectedTowns = selectedTowns.filter((id) => id !== townId);
    }
    townList = selectedTowns.join(", ");
  }

  // Function to handle image file selection
  function handleFileChange(event) {
    image.set(event.target.files[0]); // Update the store
    console.log("Image file selected:", event.target.files[0]);
  }
</script>

<div
  class="flex flex-col items-center justify-center h-full min-h-screen bg-teal-50 md:bg-none"
>
  <div
    class="flex flex-col w-full h-full max-w-2xl gap-4 p-2 my-8 font-semibold rounded-lg md:shadow-lg md:p-8 bg-teal-50"
  >
    <h1 class="pt-4 text-2xl text-center md:text-3xl lg:text-4xl">
      Crear Servicio
    </h1>
    <div>
      <label for="title">Titulo</label>
      <input
        class="w-full"
        type="text"
        name="titulo"
        id=""
        bind:value={title}
      />
    </div>

    <label for="service">Seleccione Servicio a Brindar</label>
    <select
      bind:value={service_id}
      name="service"
      class="block w-full overflow-y-auto border-slate-600 border-1 focus:border-teal-500 focus:ring-0 disabled:cursor-not-allowed"
    >
      <option value={-1} disabled>---</option>
      {#each services as [service, id]}
        <option value={id}>{service}</option>
      {/each}
    </select>

    <div class="w-full dropdown">
      <button tabindex="0" class="btn btn-base dropdown-toggle"
        >Seleccionar Pueblos</button
      >
      <ul
        tabindex="-1"
        class="flex flex-wrap w-full h-40 min-w-full gap-4 p-4 overflow-y-auto shadow gap-x-10 dropdown-content bg-base-100 rounded-box"
      >
        {#each towns as [town, id]}
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
      <label for="description">Descripcion de su Servicio</label>
      <textarea
        bind:value={description}
        class="w-full min-h-20 max-h-20"
        name="description"
        id=""
      />
    </div>
    <div>
      <label for="price-min">Precio Minimo (Opcional)</label>
      <input
        class="w-full"
        type="number"
        name="price-min"
        id=""
        bind:value={price_min}
      />
    </div>
    <div>
      <label for="price-max">Precio Maximo (Opcional)</label>
      <input
        class="w-full"
        type="number"
        name="price-max"
        id=""
        bind:value={price_max}
      />
    </div>
    <div
      class="flex flex-col items-center justify-center w-full m-auto mx-auto space-y-1 text-gray-800"
    >
      <label for="imageInput" class="block text-sm font-medium"></label>
      <div class="flex w-full">
        <input
          type="file"
          name="image"
          id="imageInput"
          on:change={handleFileChange}
          class="w-full px-8 py-12 text-gray-600 bg-gray-100 border-2 border-gray-300 border-dashed rounded-md"
          accept="image/*"
        />
      </div>
      {#if errorMessage}
        <p class="text-red-500">{errorMessage}</p>
      {/if}
    </div>

    <Button {button} />
    <div />
  </div>
</div>
