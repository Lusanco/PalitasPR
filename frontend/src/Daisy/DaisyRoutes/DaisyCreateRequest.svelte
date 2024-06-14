<script>
  import { state, data } from "../scripts/stores";
  import townsID from "../scripts/townsID";
  import servicesID from "../scripts/servicesID";
  import Button from "../components/Button.svelte";

  let image = null;
  let town = "all";
  let towns;
  let model = "requests";

  let button = {
    name: "Request Service",
    method: "POST",
    url: "api/dashboard/request-service",
    headers: "multipart/form-data",
    twcss: "px-8 py-3 font-semibold bg-stone-200 rounded hover:bg-stone-300",
    misc: { "App Location": "RequestService Form" },
  };

  let title = "";
  let service_id = "";
  let description = "";
  let price_min = "";
  let price_max = "";
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
      price_min,
      price_max,
    };

    data.set($data);
    console.log("Data updated:", $data);
  }

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
</script>

<div class="flex flex-col items-center justify-center h-full min-h-screen bg-base-200 md:bg-none">
  <div class="flex flex-col w-full h-full max-w-2xl gap-4 p-2 my-8 font-semibold rounded-lg md:shadow-lg md:p-8 bg-base-200">
    <h1 class="pt-4 text-2xl text-center md:text-3xl lg:text-4xl">Request Service</h1>
    <div>
      <label for="title">Title</label>
      <input class="w-full input input-bordered" type="text" name="title" id="title" bind:value={title} />
    </div>

    <label for="service">Select Service</label>
    <select bind:value={service_id} name="service" class="block w-full select select-bordered">
      <option value={-1} disabled>---</option>
      {#each Object.entries(servicesID) as [service, id]}
        <option value={id}>{service}</option>
      {/each}
    </select>

    <div class="w-full dropdown">
      <button tabindex="0" class="btn btn-base dropdown-toggle">Select Towns</button>
      <ul tabindex="-1" class="flex flex-wrap w-full h-40 min-w-full gap-4 p-4 overflow-y-auto shadow gap-x-10 dropdown-content bg-base-100 rounded-box">
        {#each Object.entries(townsID) as [town, id]}
          <li class="menu-item" value={id}>
            <input bind:value={id} on:change={handleTownChange} type="checkbox" id={`'${id}'`} class="mr-2 checkbox checkbox-base" />
            {town}
          </li>
        {/each}
      </ul>
    </div>

    <div class="max-h-96">
      <label for="description">Service Description</label>
      <textarea bind:value={description} class="w-full textarea textarea-bordered" name="description" id="description"></textarea>
    </div>
    <div>
      <label for="price-min">Minimum Price (Optional)</label>
      <input class="w-full input input-bordered" type="number" name="price-min" id="price-min" bind:value={price_min} />
    </div>
    <div>
      <label for="price-max">Maximum Price (Optional)</label>
      <input class="w-full input input-bordered" type="number" name="price-max" id="price-max" bind:value={price_max} />
    </div>
    <div class="flex flex-col items-center justify-center w-full m-auto mx-auto space-y-1 text-gray-800">
      <label for="imageInput" class="block text-sm font-medium"></label>
      <div class="flex w-full">
        <input type="file" name="image" id="imageInput" on:change={handleFileChange} class="w-full px-8 py-12 text-gray-600 border-2 border-gray-300 border-dashed rounded-md bg-stone-200" accept="image/*" />
      </div>
      {#if errorMessage}
        <p class="text-red-500">{errorMessage}</p>
      {/if}
    </div>

    <Button {button} {image} />
    <div />
  </div>
</div>