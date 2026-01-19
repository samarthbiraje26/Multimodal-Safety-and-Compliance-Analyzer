const handleAnalyze = async () => {
  try {
    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch("http://127.0.0.1:8000/api/image/analyze", {
      method: "POST",
      body: formData,
    });

    console.log("HTTP STATUS:", res.status);

    const text = await res.text();
    console.log("RAW RESPONSE:", text);

    const data = JSON.parse(text);
    console.log("PARSED JSON:", data);

    setResult(data.status);
  } catch (err) {
    console.error("❌ FRONTEND ERROR:", err);
    alert("Analysis failed");
  }
};