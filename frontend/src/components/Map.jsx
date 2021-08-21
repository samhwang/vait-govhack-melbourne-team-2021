import { useState, useEffect } from 'react';
import { useGeolocation, useEffectOnceWhen } from 'rooks';
import { Alert } from '@material-ui/lab';
import { Grid } from '@material-ui/core';
import ReactMapGL, { Marker } from 'react-map-gl';
import RoomIcon from '@material-ui/icons/Room';
import SharedLayout from './SharedLayout';
import 'mapbox-gl/dist/mapbox-gl.css';

const MAPBOX_TOKEN =
  'pk.eyJ1Ijoic2FtaHdhbmcyMTEyIiwiYSI6ImNrc2xqZXpycDA3d28ydnBuMnFjYWkzdWcifQ.6L8Ejvo0e13O7j5iy01VjQ';

const DEFAULT_GPS_COORDINATES = {
  latitude: -37.8136,
  longitude: 144.9631,
};

function Map() {
  const geolocation = useGeolocation();
  const [viewport, setViewport] = useState({
    width: '100vw',
    height: '80vh',
    zoom: 8,
    ...DEFAULT_GPS_COORDINATES,
  });
  const onViewportChange = (nextViewport) => setViewport(nextViewport);

  useEffectOnceWhen(() => {
    setViewport((currentViewport) => ({
      ...currentViewport,
      zoom: 14,
    }));
  }, geolocation);

  useEffect(() => {
    if (!geolocation) {
      return;
    }

    setViewport((currentViewport) => ({
      ...currentViewport,
      latitude: geolocation.lat,
      longitude: geolocation.lng,
    }));
  }, [geolocation]);

  return (
    <SharedLayout>
      {geolocation && geolocation.isError && (
        <Alert variant="filled" severity="warning">
          Please enable location services to use this module.
        </Alert>
      )}
      <Grid item container md={12}>
        <ReactMapGL
          {...viewport}
          onViewportChange={onViewportChange}
          mapboxApiAccessToken={MAPBOX_TOKEN}
        >
          {geolocation && !geolocation.isError && (
            <Marker latitude={geolocation.lat} longitude={geolocation.lng}>
              <RoomIcon fontSize="large" />
            </Marker>
          )}
        </ReactMapGL>
      </Grid>
    </SharedLayout>
  );
}

export default Map;
