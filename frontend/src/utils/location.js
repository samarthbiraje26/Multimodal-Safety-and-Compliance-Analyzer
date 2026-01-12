export async function getLocationMessage() {
  return new Promise((resolve) => {
    navigator.geolocation.getCurrentPosition(
      (pos) => {
        const { latitude, longitude } = pos.coords;
        resolve(`📍 Location: https://maps.google.com/?q=${latitude},${longitude}`);
      },
      () => resolve("📍 Location unavailable")
    );
  });
}