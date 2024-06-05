<!-- Alfre: It seems button works correctly 
  and missing towns as an array [] making 
  the api request fail with status: 500 -->
  <script>
    import townsID from "../scripts/townsID";
    import servicesID from "../scripts/servicesID";
    import Button from "../Daisycomponents/DaisyButton.svelte";
  
    // Data points for axiosDATA
    let model = "Promotion",
      title,
      town,
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
      twcss: "btn btn-primary w-full",
    };
  
    let data = {
      model,
      title,
      town,
      service_id,
      description,
      price_min,
      price_max,
    };
  
    function handleFileChange(event) {
      console.log("Selected Image");
      imageFile = event.target.files[0];
      axiosDATA.append("image", imageFile);
    }
  
    function handleInputChange() {
      const allTrue = Object.values(data).every((value) => Boolean(value));
      if (allTrue) {
        console.log("Form Completed");
        for (const [key, value] of Object.entries(data)) {
          axiosDATA.append(key, value);
        }
      }
    }
  </script>
  
  <div
    class="flex flex-col items-center justify-center h-full min-h-screen bg-base-200 md:bg-none"
  >
    <div
      class="w-full h-full max-w-2xl p-2 font-semibold rounded-lg md:shadow-lg md:p-8 bg-base-100"
    >
      <h1 class="pt-4 text-2xl text-center md:text-3xl lg:text-4xl">
        Crear Servicio
      </h1>
      <!-- Crear Solicitud de Servicio -->
      <div class="">
        <label for="title">Titulo</label>
        <input
          class="w-full input input-bordered"
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
        class="w-full select select-bordered"
      >
        <option value={-1} disabled>---</option>
        {#each services as [service, id]}
          <option value={id}>{service}</option>
        {/each}
      </select>
      <!-- Service Filter End -->
  
      <!-- Town Filter Start -->
      <label for="town">Seleccione un Pueblo</label>
      <select
        bind:value={data.town}
        on:change={handleInputChange}
        name="town"
        class="w-full select select-bordered"
      >
        <option value={-1} disabled>---</option>
        {#each towns as [town, id]}
          <option value={id}>{town}</option>
        {/each}
      </select>
      <!-- Town Filter End -->
      <div class="max-h-96">
        <label for="description">Descripcion de su Servicio</label>
        <textarea
          bind:value={data.description}
          on:change={handleInputChange}
          class="w-full textarea textarea-bordered min-h-20 max-h-20"
          name="description"
          id=""
        ></textarea>
      </div>
      <div>
        <label for="price-min">Precio Minimo (Opcional)</label>
        <input
          class="input input-borderedw-full"
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
          class="w-full input input-bordered"
          type="number"
          name="price-max"
          id=""
          bind:value={data.price_max}
          on:change={handleInputChange}
        />
      </div>
      <div
        class="flex flex-col items-center justify-center w-full m-auto mx-auto space-y-1 text-neutral-content"
      >
        <label for="imageInput" class="block text-sm font-medium"></label>
        <div class="flex w-full">
          <input
            type="file"
            name="image"
            id="imageInput"
            on:change={handleFileChange}
            class="w-full px-8 py-12 border-2 border-dashed rounded-md text-neutral-content bg-base-200"
            accept="image/*"
          />
        </div>
        {#if errorMessage}
          <p class="text-error">{errorMessage}</p>
        {/if}
      </div>
      <Button {buttonDATA} {axiosDATA} {miscDATA} />
    </div>
  </div>
  