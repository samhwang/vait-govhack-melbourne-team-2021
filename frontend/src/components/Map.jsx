import { useGeolocation } from 'rooks';
import { Alert } from '@material-ui/lab';
import { Grid, Typography } from '@material-ui/core';
import SharedLayout from './SharedLayout';

function Map() {
  const geolocation = useGeolocation();

  return (
    <SharedLayout>
      {geolocation && geolocation.isError && (
        <Alert variant="filled" severity="warning">
          Please enable location services to use this module.
        </Alert>
      )}
      <Grid item container md={12}>
        <Typography variant="h2">Map Page</Typography>
      </Grid>
    </SharedLayout>
  );
}

export default Map;
