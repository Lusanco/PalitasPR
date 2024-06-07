export function setHeaders(contentType) {
  if (contentType === "multipart/form-data") {
    return { "Content-Type": "multipart/form-data" };
  } else {
    return { "Content-Type": "application/json" };
  }
}
