import { createClient, Provider } from 'urql';
import PropTypes from 'prop-types';

const client = createClient({
  url: 'https://vpq7kicr5i.execute-api.ap-southeast-2.amazonaws.com/dev/graphql',
  fetchOptions: () => ({ headers: {} }),
});

const UrqlContext = ({ children }) => (
  <Provider value={client}>{children}</Provider>
);

UrqlContext.propTypes = {
  children: PropTypes.node,
};

export default UrqlContext;
