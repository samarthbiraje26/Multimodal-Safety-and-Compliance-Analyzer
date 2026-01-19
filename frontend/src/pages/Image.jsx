import { useState, useEffect } from "react";

function Image() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

  const handleAnalyze = async () => {
    if (!file) return alert("Please upload an image");

    const formData = new FormData();
    formData.append("file", file);

    setLoading(true);
    setResult("");

    try {
      const res = await fetch("http://127.0.0.1:8000/api/image/analyze", {
        method: "POST",
        body: formData,
      });

      const data = await res.json();
      console.log("BACKEND RESPONSE 👉", data);

      // ✅ IMPORTANT: match backend key
      setResult(data.status || data.result || data.label || "UNKNOWN");

    } catch (err) {
      console.error(err);
      alert("Analysis failed");
    }

    setLoading(false);
  };

  useEffect(() => {
    console.log("RESULT STATE UPDATED 👉", result);
  }, [result]);

  return (
    <div style={{ padding: "30px" }}>
      <h2>Image Safety Analyzer</h2>

      <input
        type="file"
        accept="image/*"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <br /><br />

      <button onClick={handleAnalyze}>Analyze</button>

      {loading && <p>Analyzing...</p>}

      {result && (
        <h1 style={{ marginTop: "20px", color: "red" }}>
          RESULT: {result}
        </h1>
      )}
    </div>
  );
}

export default Image;