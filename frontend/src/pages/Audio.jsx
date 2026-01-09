import { useState } from "react";
import { api } from "../services/api";

export default function Audio() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);

  const analyze = async () => {
    const formData = new FormData();
    formData.append("file", file);

    const res = await api.post("/audio/analyze", formData);
    setResult(res.data);
  };

  return (
    <div className="container">
      <h2>Audio Analyzer</h2>
      <input type="file" accept="audio/*" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={analyze}>Analyze</button>

      {result && <pre>{JSON.stringify(result, null, 2)}</pre>}
    </div>
  );
}