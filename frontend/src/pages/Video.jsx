import { useState } from "react";
import { api } from "../services/api";

export default function Video() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);

  const analyze = async () => {
    const formData = new FormData();
    formData.append("file", file);

    const res = await api.post("/video/analyze", formData);
    setResult(res.data);
  };

  return (
    <div className="container">
      <h2>Video Analyzer</h2>
      <input type="file" accept="video/*" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={analyze}>Analyze</button>

      {result && <pre>{JSON.stringify(result, null, 2)}</pre>}
    </div>
  );
}