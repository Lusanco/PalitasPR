<script>
  import axios from "axios";
  import { onMount } from "svelte";
  import { writable } from "svelte/store";
  import { userSession } from "../scripts/stores";
  import Button from "./Button.svelte";

  let userDetails = writable();

  let qr_pic = null;
  let image = qr_pic;
  let imageUrl = null;
  let id;
  let fileInput;
  let errMessage;
  let guardarQR;
  let profile;

  export let view;
  export let providerName;

  onMount(() => {
    axios
      .get("/api/user/status")
      .then((userStatusRes) => {
        userSession.set(true);
        userDetails.set(userStatusRes.data);
        console.log("userStatusRes", userStatusRes.data);

        id = userStatusRes.data.profile_id;
        console.log("id", id);

        // Update guardarQR with the correct URL
        guardarQR = {
          name: "Guardar",
          method: "POST",
          url: `/api/user/profile/${id}`,
          headers: "application/json", // "application/json"
          twcss:
            "flex-1 w-full px-4 py-2 text-lg text-white border-none btn bg-accent",
          misc: { "App Location": "Guardar QR" },
        };

        axios
          .get(`/api/user/profile/${id}`)
          .then((response) => {
            profile = response.data.results;
            console.log("profile", profile);
            if (profile.qr_pic) {
              imageUrl = profile.qr_pic;
            }
          })
          .catch((error) => {
            console.error("Error fetching profile data:", error);
          });
      })
      .catch((error) => {
        console.error("Error fetching user status:", error);
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

  function handleSave() {
    if (qr_pic) {
      const formData = new FormData();
      formData.append("qr_pic", qr_pic);

      axios
        .put(`/api/user/profile/${id}`, formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        })
        .then((response) => {
          imageUrl = URL.createObjectURL(qr_pic);
          qr_pic = null;
          fileInput.value = null;
          console.log("Image uploaded successfully:", response);
        })
        .catch((error) => {
          console.error("Error uploading image:", error);
        });
    }
  }

  function handleDelete() {
    axios
      .delete(`/api/user/profile/${id}`)
      .then((response) => {
        qr_pic = null;
        imageUrl = null;
        fileInput.value = null;
      })
      .catch((error) => {
        console.error("Error deleting image:", error);
      });
  }
</script>

<!-- QR Component HTML -->

<!-- <div class="flex items-center justify-center min-h-screen m-5 overflow-x-auto"> -->
{#if view === "provider"}
  <div
    class="flex items-center justify-center w-full m-2 bg-white rounded-md md:m-20 card"
  >
    <h1
      class="text-xl md:text-4xl text-center mb-6 font-semibold text-[#1f1f1f]"
    >
      Sube tu QR de Ath Movil aquí
    </h1>
    {#if imageUrl === null}
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
        <div
          class="flex-1"
          class:opacity-50={!qr_pic}
          class:pointer-events-none={!qr_pic}
        >
          <Button button={guardarQR} {image} on:click={handleSave} />
        </div>

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
      <div class="flex flex-col items-center justify-center">
        <img src={imageUrl} alt="QR Code" class="w-full h-auto rounded-md" />
        <div class="flex w-full gap-2 mt-6">
          <button class="flex-1 px-4 py-2 text-lg btn" on:click={handleSave}>
            <i
              class="flex items-center justify-center text-lg fa-solid fa-pen-to-square"
            ></i>
            <span class="hidden md:block">Guardar</span>
          </button>
          <button class="flex-1 px-4 py-2 text-lg btn" on:click={handleDelete}>
            <i
              class="flex items-center justify-center mt-[3px] text-lg fa-solid fa-trash"
            ></i>
            <span class="hidden md:block">Eliminar</span>
          </button>
        </div>
      </div>
    {/if}
  </div>
{:else if view === "receiver"}
  <div
    class="flex flex-col items-center justify-center w-full p-5 mt-8 bg-opacity-30 card bg-neutral"
  >
    <h1 class="text-lg font-semibold md:text-2xl">QR code de {providerName}</h1>
    <img src={imageUrl} alt="QR Code" class="w-full h-auto my-2 rounded-md" />
    <p class="text-sm font-semibold text-center md:text-md">
      Escanéalo para realizar el pago vía ATH Movil
    </p>
  </div>
{/if}
<!-- </div> -->
