import { useQuery } from 'urql';
import { gql } from '@urql/core';

const HelloQuery = gql`
  query HelloQuery {
    hello {
      success
      message
      errors
    }
  }
`;

const Main = () => {
  const [result] = useQuery({
    query: HelloQuery,
  });
  const { data, fetching, error } = result;

  if (fetching) return <div>Loading...</div>
  if (error) return (
    <div>
      Oh no... Cannot fetch due to {error.message}
    </div>
  );

  return <div>{data.hello.message}</div>;
};

export default Main;
