import { Typography, Grid } from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import Chart from './Chart';
import SharedLayout from './SharedLayout';

const useStyles = makeStyles(() => ({
  root: {
    display: 'flex',
  },
}));


// Generate Sales Data
function createData(time, amount) {
  return { time, amount };
}

const dataDay = [
  createData('00:00', 0),
  createData('03:00', 300),
  createData('06:00', 600),
  createData('09:00', 800),
  createData('12:00', 1500),
  createData('15:00', 2000),
  createData('18:00', 2400),
  createData('21:00', 2400),
  createData('24:00', undefined),
];

const dataWeek = [
  createData('Monday', 5),
  createData('Tuesday', 4),
  createData('Wednesday', 2),
  createData('Thursday', 3),
  createData('Friday', 1),
  createData('Saturday', 3),
  createData('Sunday', 5),
];

function Dashboard() {
  const classes = useStyles();
  return (
    <SharedLayout className={classes.root}>
      <Grid item container spacing={3} className={classes.root}>
        <Grid item md={12}>
          <Typography variant="h2" style={{ textAlign:"center" }}>Dashboard</Typography>
        </Grid>
        <Grid item md={12}>
          <Typography>Current safety rating:</Typography>
          <Typography style={{ fontWeight: 'bold' }}>5</Typography>
        </Grid>
        <Grid item md={12}>
          <Chart title="User Space Evaluation by Day" data={dataDay} />
        </Grid>
        <Grid item md={12}>
          <Chart title="User Space Evaluation by Week" data={dataWeek} />
        </Grid>
      </Grid>
    </SharedLayout>
  );
}

export default Dashboard;
