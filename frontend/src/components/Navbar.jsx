import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav className="nav">
      <h3>Safety Analyzer</h3>
      <div>
        <Link to="/">Home</Link>
        <Link to="/text">Text</Link>
        <Link to="/image">Image</Link>
        <Link to="/audio">Audio</Link>
        <Link to="/video">Video</Link>
      </div>
    </nav>
  );
}