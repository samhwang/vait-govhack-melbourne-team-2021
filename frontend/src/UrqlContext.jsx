import { createClient, Provider } from 'urql';
import PropTypes from 'prop-types';

const client = createClient({
  url: 'http://localhost:5000/graphql',
  fetchOptions: () => ({ headers: {} }),
});

const UrqlContext = ({ children }) => (
  <Provider value={client}>{children}</Provider>
);

UrqlContext.propTypes = {
  children: PropTypes.node,
};

export default UrqlContext;
