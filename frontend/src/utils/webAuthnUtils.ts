export function base64UrlToArrayBuffer(base64UrlString: string): ArrayBuffer {
  const padding = "=".repeat((4 - (base64UrlString.length % 4)) % 4);
  const base64 = (base64UrlString + padding)
    .replace(/-/g, "+")
    .replace(/_/g, "/");
  const rawData = window.atob(base64);
  const outputArray = new Uint8Array(rawData.length);
  for (let i = 0; i < rawData.length; i++) {
    outputArray[i] = rawData.charCodeAt(i);
  }
  return outputArray.buffer;
} 