import "./App.css";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "../Home/Home";
import About from "../About/About";
import CookBook from "../Cookbook/Cookbook";

function App() {
  return (
    <>
      <Router>
        <div className="links">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/aboutus" element={<About />} />
            <Route path="/CookBook" element={<CookBook />} />
          </Routes>
        </div>
      </Router>
    </>
  );
}

export default App;
