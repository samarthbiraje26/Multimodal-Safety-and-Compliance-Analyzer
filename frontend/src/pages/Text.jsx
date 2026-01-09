import { useState } from "react";
import { api } from "../services/api";

export default function Text() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);

  const analyze = async () => {
    const res = await api.post("/text/analyze", { text });
    setResult(res.data);
  };

  return (
    <div className="container">
      <h2>Text Analyzer</h2>
      <textarea
        rows="6"
        placeholder="Enter text"
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
      <button onClick={analyze}>Analyze</button>

      {result && <pre>{JSON.stringify(result, null, 2)}</pre>}
    </div>
  );
}