<script>
  import axios from "axios";
  import { onMount } from "svelte";
  import { writable } from "svelte/store";
  import { userSession } from "../scripts/stores";
  import Button from "./Button.svelte";

  let userDetails = writable();

  let qr_pic = null;
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
        id = userStatusRes.data.profile_id;
        console.log("User ID:", id);

        /* // Update guardarQR with the correct URL
        guardarQR = {
          name: "Guardar",
          method: "POST",
          url: `/api/user/profile/${id}`,
          headers: "application/json",
          twcss:
            "flex-1 w-full px-4 py-2 text-lg text-white border-none btn bg-accent",
          misc: { "App Location": "Guardar QR" },
        }; */

        return axios.get(`/api/user/profile/${id}`);
      })
      .then((response) => {
        profile = response.data.results;
        if (profile.qr_pic) {
          imageUrl = profile.qr_pic;
        }
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

  /* function handleSave() {
    if (image) {
      const formData = new FormData();
      formData.append("qr_pic", image);

      axios
        .put(`/api/user/profile/${id}`, formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        })
        .then((response) => {
          imageUrl = URL.createObjectURL(image);
          image = null;
          fileInput.value = null;
          console.log("Image uploaded successfully:", response);
        })
        .catch((error) => {
          console.error("Error uploading image:", error);
        });
    }
  } */

  function handleEdit() {
    qr_pic = null;
    imageUrl = null;
    fileInput.value = null;

    axios
      .put(`/api/user/profile/${id}`, { qr_pic: imageUrl })
      .then((response) => {
        console.log("Image URL updated successfully:", response);
      })
      .catch((error) => {
        console.error("Error updating image URL:", error);
      });
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
          <!-- <Button button={guardarQR} {image} on:click={handleSave} /> -->
          <button
            class="flex-1 px-4 py-2 text-lg border-2 btn border-accent text-accent"
            class:opacity-50={!qr_pic}
            class:pointer-events-none={!qr_pic}
            on:click={() => {
              if (qr_pic) {
                console.log("Uploading image:", qr_pic);

                axios
                  .put(`/api/user/profile/${id}`, qr_pic, {
                    headers: {
                      "Content-Type": qr_pic.type,
                    },
                  })
                  .then((response) => {
                    imageUrl = URL.createObjectURL(qr_pic);
                    /* qr_pic = null;
                    fileInput.value = null; */
                    console.log("Image uploaded successfully:", response);
                  })
                  .catch((error) => {
                    console.error("Error uploading image:", error);
                  });
              }
            }}>Guardar</button
          >
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
          <button class="flex-1 px-4 py-2 text-lg btn" on:click={handleEdit}>
            <i
              class="flex items-center justify-center text-lg fa-solid fa-pen-to-square"
            ></i>
            <span class="hidden md:block">Edit</span>
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
