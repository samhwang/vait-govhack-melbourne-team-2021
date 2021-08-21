import { useForm, Controller } from 'react-hook-form';
import { useToggle } from 'rooks';
import {
  Grid,
  IconButton,
  Typography,
  TextField,
  Checkbox,
  FormControlLabel,
  Button,
  makeStyles,
} from '@material-ui/core';
import CloseIcon from '@material-ui/icons/Close';
import CircularProgress from '@material-ui/core/CircularProgress';

const useStyles = makeStyles((theme) => ({
  overlay: {
    position: 'fixed' /* Sit on top of the page content */,
    display: 'block',
    width: '100%' /* Full width (cover the whole page) */,
    height: '100%' /* Full height (cover the whole page) */,
    top: 0,
    left: 0,
    right: 0,
    bottom: 0,
    backgroundColor: 'rgba(0,0,0,0.5)' /* Black background with opacity */,
    zIndex: 10 /* Specify a stack order in case you're using a different order for other elements */,
  },
  centerSpinning: {
    marginTop: '30%',
    marginLeft: '50%',
  },
}));

export default function SubscribeFormBody({ closeModal }) {
  const [isSubmitting, toggleIsSubmitting] = useToggle(false);
  const { control, handleSubmit } = useForm();
  const classes = useStyles();
  const onSubmit = async (data) => {
    toggleIsSubmitting(false);

    new Promise((resolve) => {
      setTimeout(() => {
        alert('Successful subscription');
        resolve(true);
      }, 1500);
    }).then(() => {
      closeModal();
    });
  };

  return (
    <form
      onSubmit={handleSubmit(onSubmit)}
      style={{
        marginLeft: '5%',
        marginRight: '5%',
      }}
    >
      {isSubmitting && (
        <div className={classes.overlay}>
          <CircularProgress
            className={classes.centerSpinning}
            color="secondary"
          />
        </div>
      )}
      <Grid item container md={12} spacing={3}>
        <Grid item md={12}>
          <IconButton onClick={closeModal}>
            <CloseIcon />
          </IconButton>
          <Typography variant="h2">Subscribe</Typography>
        </Grid>

        <Grid item md={12}>
          <Controller
            name="phoneNumber"
            control={control}
            defaultValue=""
            render={({ field }) => (
              <TextField
                {...field}
                label="Phone Number / Email"
                disabled={isSubmitting}
              />
            )}
          />
        </Grid>

        <Grid item md={12}>
          <Controller
            name="suburb"
            control={control}
            defaultValue=""
            render={({ field }) => (
              <TextField {...field} label="Suburb" disabled={isSubmitting} />
            )}
          />
        </Grid>

        <Grid item md={12}>
          <FormControlLabel
            control={
              <Checkbox
                name="checkedB"
                color="primary"
                disabled={isSubmitting}
              />
            }
            label="Agree to terms and conditions?"
          />
        </Grid>

        <Grid item md={12}>
          <Button
            onClick={handleSubmit(onSubmit)}
            variant="contained"
            color="primary"
          >
            Submit
          </Button>
        </Grid>
      </Grid>
    </form>
  );
}
