import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Map from './components/Map';
import Dashboard from './components/Dashboard';
import ErrorPage from './components/ErrorPage';
import UrqlContext from './components/UrqlContext';
import './App.css';

function App() {
  return (
    <UrqlContext>
      <Router>
        <Switch>
          <Route exact path="/">
            <Dashboard />
          </Route>
          <Route path="/map">
            <Map />
          </Route>
          <Route path="*">
            <ErrorPage />
          </Route>
        </Switch>
      </Router>
    </UrqlContext>
  );
}

export default App;
