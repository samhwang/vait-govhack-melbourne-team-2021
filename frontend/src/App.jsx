import Root from './components/Root';
import UrqlContext from './UrqlContext';
import './App.css';

function App() {
  return (
    <UrqlContext>
      <Root />
    </UrqlContext>
  );
}

export default App;
