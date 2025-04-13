const uppy = new window.Uppy.Core()
  .use(window.Uppy.Dashboard, {
    inline: true,
    target: '#drag-drop-area',
    note: 'Envie até 5 fotos por vez',
    proudlyDisplayPoweredByUppy: false
  })
  .use(window.Uppy.Tus, {
    endpoint: 'https://tusd.tusdemo.net/files/' // servidor demo
  });

uppy.on('complete', (result) => {
  alert('Fotos enviadas com sucesso!');
});
