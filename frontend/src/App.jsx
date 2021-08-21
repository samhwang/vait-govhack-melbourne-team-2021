import Main from './components/Main';
import UrqlContext from './components/UrqlContext';
import './App.css';

function App() {
  return (
    <UrqlContext>
      <Main />
    </UrqlContext>
  );
}

export default App;
