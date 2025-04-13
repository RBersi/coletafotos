const uppy = new Uppy.Core()
  .use(Uppy.Dashboard, {
    inline: true,
    target: '#drag-drop-area'
  })
  .use(Uppy.Tus, { endpoint: 'https://tusd.tusdemo.net/files/' });

uppy.on('complete', (result) => {
  alert('Fotos enviadas com sucesso!');
});
