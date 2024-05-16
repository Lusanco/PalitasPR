<script>
  import axios from "axios";
  let imageFile;
  const uploadImage = async (event) => {
    const selectedFile = event.target.files[0];

    if (!selectedFile) {
      console.error("No file selected");
      return;
    }

    const formData = new FormData();
    formData.append("image", selectedFile, selectedFile.name); // Use original filename

    // try {
    //   const response = await axios.post("/upload-image", formData, {
    //     headers: {
    //       "Content-Type": "multipart/form-data", // Set appropriate content type
    //     },
    //   });
    //   console.log("Image uploaded successfully:", response.data);
    // } catch (error) {
    //   console.error("Error uploading image:", error);
    // }

    axios
      .post("/upload-image", formData, {
        headers: {
          "Content-Type": "multipart/form-data", // Set appropriate content type
        },
      })
      .then((response) => {
        console.log("Image uploaded successfully:", response.data);
      })
      .catch((error) => {
        console.error("Error uploading image:", error);
      });
  };

  // imageInput.addEventListener("change", uploadImage);
</script>

<div class="flex flex-col min-h-screen">
  <div
    class="flex flex-col items-center justify-center w-full h-full min-h-screen m-auto space-y-1 text-gray-800"
  >
    <label for="files" class="block text-sm font-medium">Attachments</label>
    <div class="flex">
      <input
        type="file"
        name="files"
        id="imageInput"
        bind:files={imageFile}
        class="px-8 py-12 text-gray-600 bg-gray-100 border-2 border-gray-300 border-dashed rounded-md"
      />
    </div>
  </div>
</div>
