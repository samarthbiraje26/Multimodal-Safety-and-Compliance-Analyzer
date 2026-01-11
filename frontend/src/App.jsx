import { BrowserRouter, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import Text from "./pages/Text";
import Image from "./pages/Image";
import Audio from "./pages/Audio";
import Video from "./pages/Video";


export default function App() {
  return <h1>App is rendering</h1>;
}

export default function App() {
  return (
    <BrowserRouter>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/text" element={<Text />} />
        <Route path="/image" element={<Image />} />
        <Route path="/audio" element={<Audio />} />
        <Route path="/video" element={<Video />} />
      </Routes>
    </BrowserRouter>
  );
}