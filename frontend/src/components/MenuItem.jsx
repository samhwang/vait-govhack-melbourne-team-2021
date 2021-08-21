import { ListItem, ListItemText } from '@material-ui/core';
import { useMemo, forwardRef } from 'react';
import { Link, useLocation } from 'react-router-dom';

function ListItemLink({ to, children }) {
  const CustomLink = useMemo(
    () =>
      forwardRef((linkProps, ref) => <Link ref={ref} to={to} {...linkProps} />),
    [to]
  );

  return (
    <ListItem button component={CustomLink}>
      {children}
    </ListItem>
  );
}

export default function MenuItem({ item, path }) {
  const location = useLocation();
  const isAtPath = location.pathname === path;

  return (
    <ListItemLink to={path}>
      <ListItemText primary={item} style={{ color: isAtPath && 'red' }} />
    </ListItemLink>
  );
}
