import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import IconButton from '@material-ui/core/IconButton';
import TextField from '@material-ui/core/TextField';
import SearchIcon from '@material-ui/icons/Search';

const useStyles = makeStyles((theme) => ({
  appBar: {
    zIndex: theme.zIndex.drawer + 1,
    transition: theme.transitions.create(['width', 'margin'], {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.leavingScreen,
    }),
    display: 'flex',
    flexDirection: 'row',
  },
  fullWidth: {
    width: '80vw',
  },
}));

function Searchbar() {
  const classes = useStyles();

  return (
    <AppBar position="relative" className={classes.appBar}>
      <form className={classes['flex-grow-1']}>
        <TextField label="Search something" className={classes.fullWidth} />
      </form>
      <Toolbar>
        <IconButton color="inherit">
          <SearchIcon />
        </IconButton>
      </Toolbar>
    </AppBar>
  );
}
export default Searchbar;
