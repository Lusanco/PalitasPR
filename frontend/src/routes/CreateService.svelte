<!-- Alfre: It seems button works correctly 
  and missing towns as an array [] making 
  the api request fail with status: 500 -->
<script>
  import townsID from "../scripts/townsID";
  import servicesID from "../scripts/servicesID";
  import Button from "../components/Button.svelte";

  // Data points for axiosDATA
  let model = "Promotion",
    title,
    service_id,
    description,
    price_min,
    price_max,
    imageFile,
    errorMessage;

  // For iterating town and service name and ids
  const towns = Object.entries(townsID);
  const services = Object.entries(servicesID);

  const axiosDATA = new FormData();
  let miscDATA = { "Create Service": true };
  let buttonDATA = {
    name: "Create Service",
    method: "POST",
    url: "api/dashboard/promotion-request",
    headers: {
      "Content-Type": "multipart/form-data",
    },
    twcss: "px-8 py-3 font-semibold text-teal-100 bg-teal-800 rounded",
  };

  let selectedTowns = []; // Array to store selected town IDs
  let townList = "";
  let data = {
    model,
    title,
    townList,
    service_id,
    description,
    price_min,
    price_max,
  };

  // Update selectedTowns based on checkbox changes
  // (e.g., in checkbox `on:change` event)
  function handleTownChange(event) {
    const townId = event.target.value;
    if (event.target.checked) {
      selectedTowns.push(townId);
    } else {
      selectedTowns = selectedTowns.filter((id) => id !== townId);
    }
    console.log(selectedTowns);
    data.townList = selectedTowns.join(", ");
    console.log(data.townList);
  }

  function handleFileChange(event) {
    console.log("Selected Image");
    imageFile = event.target.files[0];
    axiosDATA.append("image", imageFile);
  }

  function handleInputChange() {
    const allTrue = Object.values(data).every((value) => Boolean(value));
    if (
      data.description ||
      data.price_max ||
      data.price_min ||
      data.service_id ||
      data.selectedTown
    ) {
      console.log(data);
    }

    if (allTrue) {
      console.log("Form Completed");
      for (const [key, value] of Object.entries(data)) {
        axiosDATA.append(key, value);
      }
    }
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
    <!-- Crear Solicitud de Servicio -->
    <div class="">
      <label for="title">Titulo</label>
      <input
        class="w-full"
        type="text"
        name="titulo"
        id=""
        bind:value={data.title}
        on:change={handleInputChange}
      />
    </div>

    <!-- Service Filter Start -->
    <label for="service">Seleccione Servicio a Brindar</label>
    <select
      bind:value={data.service_id}
      on:change={handleInputChange}
      name="service"
      class="block w-full overflow-y-auto border-slate-600 border-1 focus:border-teal-500 focus:ring-0 disabled:cursor-not-allowed"
    >
      <option value={-1} disabled>---</option>
      {#each services as [service, id]}
        <option value={id}>{service}</option>
      {/each}
    </select>
    <!-- Service Filter End -->

    <!-- Town Filter Start -->
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

    <!-- Town Filter End -->
    <div class="max-h-96">
      <label for="description">Descripcion de su Servicio</label>
      <textarea
        bind:value={data.description}
        on:change={handleInputChange}
        class="w-full min-h-20 max-h-20"
        name="description"
        id=""
      ></textarea>
    </div>
    <div>
      <label for="price-min">Precio Minimo (Opcional)</label>
      <input
        class="w-full"
        type="number"
        name="price-min"
        id=""
        bind:value={data.price_min}
        on:change={handleInputChange}
      />
    </div>
    <div>
      <label for="price-max">Precio Maximo (Opcional)</label>
      <input
        class="w-full"
        type="number"
        name="price-max"
        id=""
        bind:value={data.price_max}
        on:change={handleInputChange}
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
    <Button {buttonDATA} {axiosDATA} {miscDATA} />
  </div>
</div>
