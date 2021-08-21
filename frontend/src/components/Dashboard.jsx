import { Typography, Grid } from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import { gql, useQuery } from 'urql';
import Chart from './Chart';
import SharedLayout from './SharedLayout';

const DashboardQuery = gql`
  query DashboardQuery {
    publicSpaces(limit: 1) {
      public_spaces {
        name
        ratingByHr {
          hr
          rating
        }
        ratingByDay {
          day
          rating
        }
      }
    }
  }
`;

const useStyles = makeStyles(() => ({
  root: {
    display: 'flex',
  },
}));

function DashboardContainer({ children }) {
  const classes = useStyles();

  return (
    <SharedLayout className={classes.root}>
      <Grid item container spacing={3} className={classes.root}>
        <Grid item md={12}>
          <Typography variant="h2" style={{ textAlign: 'center' }}>
            Dashboard
          </Typography>
        </Grid>
        {children}
      </Grid>
    </SharedLayout>
  );
}

function Dashboard() {
  const [result] = useQuery({
    query: DashboardQuery,
  });

  const { data, fetching, error } = result;

  let Content = <></>;
  if (fetching) {
    Content = <Typography>Loading...</Typography>;
  }

  if (!fetching && error) {
    Content = (
      <Typography>Oh no... cannot fetch due to {error.message}</Typography>
    );
  }

  if (!fetching && data) {
    const space = data.publicSpaces.public_spaces[0];
    const currentRating = space.ratingByHr[0].rating;
    const dataDay = space.ratingByHr.map(({ hr, rating }) => ({
      title: hr,
      amount: rating,
    }));
    const dataWeek = space.ratingByDay.map(({ day, rating }) => ({
      title: day,
      amount: rating,
    }));
    Content = (
      <>
        <Grid item md={12}>
          <Typography>
            Current safety rating for <b>{space.name}</b>:
          </Typography>
          <Typography style={{ fontWeight: 'bold' }}>
            {currentRating}
          </Typography>
        </Grid>
        <Grid item md={12}>
          <Chart title="User Space Evaluation by Day" data={dataDay} />
        </Grid>
        <Grid item md={12}>
          <Chart title="User Space Evaluation by Week" data={dataWeek} />
        </Grid>
      </>
    );
  }

  return <DashboardContainer>{Content}</DashboardContainer>;
}

export default Dashboard;
