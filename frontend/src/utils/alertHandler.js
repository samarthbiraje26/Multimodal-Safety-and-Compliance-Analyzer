import { playSiren } from "./sirenController";
import { getLocationMessage } from "./location";

export async function handleAlert(result) {
  if (result.status === "DANGER") {
    playSiren();
    const location = await getLocationMessage();
    console.log("EMERGENCY:", location);
  }
}