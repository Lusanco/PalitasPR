<script>
  import axios from "axios";
  import { onMount } from "svelte";
  import { writable } from "svelte/store";
  import { userSession } from "../scripts/stores";
  import Button from "./Button.svelte";

  let userDetails = writable();
  let qr_pic = null;
  let id;
  let fileInput;
  let profile;

  let button = {
    name: "Guardar",
    method: "PUT",
    url: "",
    headers: "multipart/form-data",
    twcss:
      "flex-1 w-full px-4 py-2 text-lg text-white border-none btn bg-accent",
    misc: { "App Location": "Guardar QR" },
  };

  export let view;
  export let providerName;
  export let imageUrl;

  onMount(() => {
    axios
      .get("/api/user/status")
      .then((userStatusRes) => {
        userSession.set(true);
        userDetails.set(userStatusRes.data);
        id = userStatusRes.data.profile_id;
        console.log("User ID:", id);

        // Update button.url with the correct ID
        button.url = `/api/user/profile/${id}`;

        return axios.get(`/api/user/profile/${id}`);
      })
      .then((response) => {
        profile = response.data.results;
        console.log("Profile data:", profile);
      })
      .catch((error) => {
        console.error("Error fetching profile data:", error);
        userSession.set(false);
      });
  });

  function handleFileChange(event) {
    qr_pic = event.target.files[0];
  }

  function handleCancel() {
    qr_pic = null;
    imageUrl = null;
    fileInput.value = null;
  }

  /* function handleEdit() {
    if (qr_pic) {
      const formData = new FormData();
      formData.append("qr_pic", qr_pic);

      axios
        .put(button.url, formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        })
        .then((response) => {
          imageUrl = URL.createObjectURL(qr_pic);
          console.log("Image uploaded successfully:", response);
        })
        .catch((error) => {
          console.error("Error uploading image:", error);
        });
    }
  } */

  /* function handleDelete() {
    axios
      .put(`/api/user/profile/${id}`)
      .then((response) => {
        qr_pic = null;
        console.log("QR code deleted successfully:", qr_pic);
        imageUrl = null;
        console.log("Image deleted successfully:", response);
      })
      .catch((error) => {
        console.error("Error deleting image:", error);
      });
  } */
</script>

{#if view === "provider"}
  <div
    class="flex items-center justify-center w-full h-full p-8 m-2 rounded-md bg-neutral bg-opacity-30 md:m-12 card"
  >
    {#if imageUrl === null}
      <h1
        class="text-xl md:text-4xl text-center mb-6 font-semibold text-[#1f1f1f]"
      >
        Sube tu QR de Ath Movil aquí
      </h1>
      <input
        type="file"
        name="image"
        id="imageInput"
        bind:this={fileInput}
        on:change={handleFileChange}
        class="w-full px-8 py-20 border-[3px] border-dashed rounded-md text-secondary bg-primary border-accent flex items-center justify-center cursor-pointer"
        accept="image/*"
      />
      <div class="flex w-full gap-2 mt-6">
        <Button {button} image={qr_pic} />
        <button
          class="flex-1 px-4 py-2 text-lg border-2 btn border-accent text-accent"
          class:opacity-50={!qr_pic}
          class:pointer-events-none={!qr_pic}
          on:click={handleCancel}
        >
          <i
            class="flex items-center justify-center mt-[2px] text-lg fa-solid fa-xmark"
          ></i>
          <span class="hidden md:block">Cancelar</span>
        </button>
      </div>
    {:else}
      <!--* View QR -->
      <div class="flex flex-col items-center justify-center">
        <h1
          class="text-xl md:text-4xl text-center mb-6 font-semibold text-[#1f1f1f]"
        >
          Tu QR de Ath Movil
        </h1>
        <img
          src={imageUrl}
          alt="QR Code"
          class="h-40 rounded-md w-80 md:h-80"
        />
        <!-- <div class="flex w-full gap-2 mt-6">
          <button class="flex-1 px-4 py-2 text-lg btn" on:click={handleEdit}>
            <i
              class="flex items-center justify-center text-lg fa-solid fa-pen-to-square"
            ></i>
            <span class="hidden md:block">Editar</span>
          </button>
          <button class="flex-1 px-4 py-2 text-lg btn" on:click={handleDelete}>
            <i
              class="flex items-center justify-center mt-[3px] text-lg fa-solid fa-trash"
            ></i>
            <span class="hidden md:block">Eliminar</span>
          </button>
        </div> -->
      </div>
    {/if}
  </div>
{:else if view === "receiver"}
  <div
    class="flex flex-col items-center justify-center w-full p-5 mt-4 bg-opacity-30 card bg-neutral"
  >
    <h1 class="text-lg font-semibold md:text-2xl">QR code de {providerName}</h1>
    <img
      src={imageUrl}
      alt="QR Code"
      class="my-2 rounded-md h-52 w-96 md:h-80"
    />
    <p class="text-sm font-semibold text-center md:text-md">
      Escanéalo para realizar el pago vía ATH Movil
    </p>
  </div>
{/if}
