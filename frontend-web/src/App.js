import './App.css';
import Navbar from "./components/Navbar";
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";

import Home from "./pages";
import About from './pages/about.js'; // or About.jsx if using JSX
import SignUp from "./pages/signup";
import Contact from "./pages/contact";
import Success from "./pages/success"; // Import the Success component

function App() {
  return (
      <Router>
          <Navbar />
          <Routes>
              <Route exact path="/" element={<Home />} />
              <Route path="/about" element={<About />} />
              <Route path="/contact" element={<Contact />} />
              <Route path="/sign-up" element={<SignUp />} />
              <Route path="/success" element={<Success />} /> {/* Add this route */}
          </Routes>
      </Router>
  );
}

export default App;


