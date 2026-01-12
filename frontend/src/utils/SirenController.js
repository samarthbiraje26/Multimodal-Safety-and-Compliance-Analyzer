let siren = null;
let timeoutId = null;

export function playSiren() {
  if (!siren) {
    siren = new Audio("/siren.mp3");
    siren.loop = true;
  }
  siren.play();

  timeoutId = setTimeout(stopSiren, 10000); // auto-stop
}

export function stopSiren() {
  if (siren) {
    siren.pause();
    siren.currentTime = 0;
  }
  if (timeoutId) clearTimeout(timeoutId);
}