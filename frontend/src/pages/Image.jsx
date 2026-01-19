const [result, setResult] = useState("");

const handleAnalyze = async () => {
  const formData = new FormData();
  formData.append("file", selectedFile);

  try {
    const res = await fetch("http://127.0.0.1:8000/api/image/analyze", {
      method: "POST",
      body: formData,
    });

    const data = await res.json();
    setResult(data.status);   // 🔴 THIS WAS MISSING
  } catch (err) {
    console.error(err);
  }
};