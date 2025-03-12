import './App.css';
import Events from "./Events";
import MyCalendar from "./Calendar";

function App() {
  return (
      <div className="App">
          <header className="App-header">
              <h3>Predstojeći događaji</h3>
          </header>
          <div className="App-body">
              <MyCalendar/> {/* Use your Events component here */}
          </div>
    </div>
);
}

export default App;
