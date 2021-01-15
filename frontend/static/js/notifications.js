const notyf = new Notyf({
    duration: 10000,
    position: {
      x: 'right',
      y: 'top',
    },
    dismissible: true,
    types: [
      {
        type: 'warning',
        background: '#F7A000',
        icon: false
      },
      {
        type: 'info',
        background: '#4281f5',
        icon: false
      },
      {
        type: 'debug',
        background: '#f542ec',
        icon: false
      }
    ]
  });