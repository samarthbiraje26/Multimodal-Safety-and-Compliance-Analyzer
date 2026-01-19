import React, { useState, useEffect } from "react";

function ImageAnalyzer() {

  // 🔹 1. STATE (TOP OF COMPONENT)
  const [selectedFile, setSelectedFile] = useState(null);
  const [result, setResult] = useState("");

  // 🔹 2. SIREN SETUP
  const siren = new Audio("/siren.mp3");

  useEffect(() => {
    if (result === "DANGER") {
      siren.play();
      setTimeout(() => siren.pause(), 10000);
    }
  }, [result]);

  // 🔹 3. ANALYZE FUNCTION
  const handleAnalyze = async () => {
    if (!selectedFile) {
      alert("Please upload an image first");
      return;
    }

    const formData = new FormData();
    formData.append("file", selectedFile);

    try {
      const res = await fetch("http://127.0.0.1:8000/api/image/analyze", {
        method: "POST",
        body: formData,
      });

      const data = await res.json();
      setResult(data.status); // ✅ VERY IMPORTANT
    } catch (error) {
      console.error(error);
    }
  };

  // 🔹 4. JSX RETURN (UI)
  return (
    <div style={{ padding: "30px" }}>
      <h2>Image Safety Analyzer</h2>

      {/* File Input */}
      <input
        type="file"
        accept="image/*"
        onChange={(e) => setSelectedFile(e.target.files[0])}
      />

      <br /><br />

      {/* Analyze Button */}
      <button onClick={handleAnalyze}>
        Analyze
      </button>

      {/* 🔴 5. RESULT DISPLAY (ADD HERE) */}
      {result && (
        <div
          style={{
            marginTop: "20px",
            padding: "15px",
            fontSize: "22px",
            fontWeight: "bold",
            color: "white",
            backgroundColor: result === "DANGER" ? "#e53935" : "#43a047",
            borderRadius: "8px",
            textAlign: "center",
            width: "200px"
          }}
        >
          {result}
        </div>
      )}
    </div>
  );
}

export default ImageAnalyzer;