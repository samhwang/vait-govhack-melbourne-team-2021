import { useForm, Controller } from 'react-hook-form';
import { yupResolver } from '@hookform/resolvers/yup';
import * as yup from 'yup';
import { useToggle } from 'rooks';
import { gql, useMutation } from 'urql';
import {
  Grid,
  IconButton,
  Typography,
  TextField,
  Checkbox,
  FormControlLabel,
  Button,
  makeStyles,
  CircularProgress,
} from '@material-ui/core';
import CloseIcon from '@material-ui/icons/Close';

const useStyles = makeStyles(() => ({
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

const subscribeQuery = gql`
  mutation SubcribeMutation($email: String!, $suburb: String!) {
    subscribe(email: $email, suburb: $suburb) {
      message
      success
    }
  }
`;

const validationSchema = yup.object().shape({
  email: yup.string().email().required(),
  suburb: yup.string().required(),
});

export default function SubscribeFormBody({
  closeModal,
  handleDrawerClose,
  openAlert,
}) {
  const [isSubmitting, toggleIsSubmitting] = useToggle(false);
  const [agree, toggleAgree] = useToggle(false);
  const handleAgree = () => toggleAgree();
  const {
    control,
    handleSubmit,
    formState: { errors },
  } = useForm({
    resolver: yupResolver(validationSchema),
  });
  const [_result, subscribe] = useMutation(subscribeQuery);
  const classes = useStyles();
  const onSubmit = ({ email, suburb }) => {
    toggleIsSubmitting(true);
    subscribe({ email, suburb }).then((result) => {
      if (result.error) {
        openAlert({
          type: 'error',
          message: 'There is an error subscribing. Please try again.',
        });
        console.error(result.error);
      } else {
        openAlert({ type: 'success', message: 'Subscribed successfully!' });
      }
      toggleIsSubmitting(false);
      closeModal();
      handleDrawerClose();
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
            name="email"
            control={control}
            defaultValue=""
            render={({ field }) => (
              <TextField {...field} label="Email" disabled={isSubmitting} />
            )}
          />
          <Typography>{errors.email?.message}</Typography>
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
          <Typography>{errors.suburb?.message}</Typography>
        </Grid>

        <Grid item md={12}>
          <FormControlLabel
            control={
              <Checkbox
                name="checkedB"
                color="primary"
                disabled={isSubmitting}
                checked={agree}
                onChange={handleAgree}
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
            disabled={!agree}
          >
            Submit
          </Button>
        </Grid>
      </Grid>
    </form>
  );
}
