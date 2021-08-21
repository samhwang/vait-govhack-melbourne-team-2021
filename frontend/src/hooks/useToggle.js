import { useState } from 'react';

export default function useToggle(initialValue = false) {
  const [state, setState] = useState(initialValue);
  const toggleState = (value) => {
    if (value) return setState(value);

    return setState((currentState) => !currentState);
  };

  return [state, toggleState];
}
