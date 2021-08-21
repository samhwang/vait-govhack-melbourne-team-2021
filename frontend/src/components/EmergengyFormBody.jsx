import { Grid, IconButton, Typography } from '@material-ui/core';
import CloseIcon from '@material-ui/icons/Close';

export default function EmergencyFormBody({ closeModal }) {
  return (
    <Grid item container md={12} spacing={3}>
      <Grid item md={12}>
        <IconButton onClick={closeModal}>
          <CloseIcon />
        </IconButton>
      </Grid>
      <Grid item md={12} style={{ margin: '2em' }}>
        <Typography variant="h2">Emergency</Typography>
        <Typography variant="body1">
          For emergency situations, click{' '}
          <a href="tel:000" style={{ fontWeight: 'bold' }}>
            here to dial 000
          </a>
        </Typography>
      </Grid>
    </Grid>
  );
}
