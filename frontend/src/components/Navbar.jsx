import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav style={{ padding: "16px", background: "#111827", color: "white" }}>
      <Link to="/" style={{ marginRight: 10 }}>Home</Link>
      <Link to="/text" style={{ marginRight: 10 }}>Text</Link>
      <Link to="/image" style={{ marginRight: 10 }}>Image</Link>
      <Link to="/audio" style={{ marginRight: 10 }}>Audio</Link>
      <Link to="/video">Video</Link>
    </nav>
  );
}