<script>
  import UploadImage from "./UploadImage.svelte";
  import { onMount, afterUpdate } from "svelte";
  import { link } from "svelte-routing";
  import axios from "axios";
  import LoadingSpinnerFull from "./LoadingSpinnerFull.svelte";
  import townsID from "../townsID";
  import servicesID from "../servicesID";
  import Button from "./Button.svelte";

  let errorMessage;

  // Data points for data
  let model = "Promotion",
    title,
    town,
    serviceID,
    description,
    priceMin,
    priceMax;

  // For iterating town and service name and ids
  const towns = Object.entries(townsID);
  const services = Object.entries(servicesID);

  let btn = "Create Promotion";
  let location = "/api/dashboard/promotion-request";
  let verb = "POST";
  // let data = [
  //   { name: "model", value: model }, // 0
  //   { name: "title", value: title }, // 1
  //   { name: "town", value: town }, // 2
  //   { name: "service_id", value: serviceID }, // 3
  //   { name: "description", value: description }, // 4
  //   { name: "price_min", value: priceMin }, // 5
  //   { name: "price_max", value: priceMax }, // 6
  // ];
  let data = {
    model: model,
    title: title,
    town: town,
    service_id: serviceID,
    description: description,
    price_min: priceMin,
    price_max: priceMax,
  };
  // console.log(data);
</script>

<div
  class="flex flex-col items-center justify-center h-full min-h-screen bg-teal-50 md:bg-none"
>
  <div
    class="w-full h-full max-w-2xl p-2 font-semibold rounded-lg md:shadow-lg md:p-8 bg-teal-50"
  >
    <h1 class="pt-4 text-2xl text-center md:text-3xl lg:text-4xl">
      Crear Oferta de Servicio
    </h1>
    <!-- Crear Solicitud de Servicio -->
    <div class="">
      <label for="title">Titulo de su Oferta</label>
      <input
        class="w-full"
        type="text"
        name="titulo"
        id=""
        bind:value={data.title}
      />
      <!-- bind:value={data[1].value} -->
    </div>
    <!-- <div class="">
      <label for="service">Tipo de Servicio</label>
      <input class="w-full" type="text" name="service" bind:value={serviceID} />
    </div> -->

    <!-- Service Filter Start -->
    <label for="service">Seleccione Servicio a Brindar</label>
    <!-- bind:value={data[3].value} -->
    <select
      bind:value={data.service_id}
      name="service"
      class="block w-full overflow-y-auto border-slate-600 border-1 focus:border-teal-500 focus:ring-0 disabled:cursor-not-allowed"
    >
      <option value="">---</option>
      {#each services as [service, id]}
        <option value={id}>{service}</option>
      {/each}
    </select>
    <!-- Service Filter End -->

    <!-- Town Filter Start -->
    <label for="town">Seleccione un Pueblo</label>
    <!-- bind:value={data[2].value} -->
    <select
      bind:value={data.town}
      name="town"
      class="block w-full overflow-y-auto border-slate-600 border-1 focus:border-teal-500 focus:ring-0 disabled:cursor-not-allowed"
    >
      <option value="0">---</option>
      {#each towns as [town, id]}
        <option value={id}>{town}</option>
      {/each}
    </select>
    <!-- Town Filter End -->
    <div class="max-h-96">
      <label for="description">Descripcion de su Oferta</label>

      <!-- bind:value={data[4].value} -->
      <textarea
        bind:value={data.description}
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
      />
      <!-- bind:value={data[5].value} -->
    </div>
    <div>
      <label for="price-max">Precio Maximo (Opcional)</label>
      <input
        class="w-full"
        type="number"
        name="price-max"
        id=""
        bind:value={data.price_max}
      />
      <!-- bind:value={data[6].value} -->
    </div>
    <!-- <div>
      <label for="imageInput">Subir Imagenes (Opcional)</label>
      <UploadImage></UploadImage>
    </div> -->
    <!-- <button
      on:click={handleCreate}
      type="button"
      class="w-full px-8 py-3 font-semibold bg-teal-600 rounded-md text-teal-50"
      >Crear</button
    > -->
    <Button
      buttonName={btn}
      crudVERB={verb}
      locationURL={location}
      axiosDATA={data}
    ></Button>
  </div>
</div>
