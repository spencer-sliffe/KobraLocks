import { AuthProvider } from './context/AuthContext.js';
import './App.css';
import Navbar from "./components/Navbar/index.js";
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";

import Home from "./pages/index.js";
import About from './pages/about.js'; // or About.jsx if using JSX
import SignUp from "./pages/signup.js";
import Contact from "./pages/contact.js";
import Success from "./pages/success.js"; // Import the Success component
import SignIn from "./pages/signin.js"
import TempDashBoard from "./pages/tempdashboard.js"

function App() {
  return (
      <Router>
         <AuthProvider>
          <Navbar />
          <Routes>
              <Route exact path="/" element={<Home />} />
              <Route path="/about" element={<About />} />
              <Route path="/contact" element={<Contact />} />
              <Route path="/sign-up" element={<SignUp />} />
              <Route path="/sign-in" element={<SignIn />} />
              <Route path="/success" element={<Success />} /> {/* Add this route */}
              <Route path="/tempdashboard" element={<TempDashBoard />} /> {/* Add this route */}
          </Routes>
          </AuthProvider>
      </Router>
  );
}

export default App;


