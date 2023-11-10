import './App.css';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Video_player from './VideoPlayer';
function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route exact path="/" element={<Video_player/>}></Route>
        </Routes>
      </Router>
    </div>
  );
}

export default App;
